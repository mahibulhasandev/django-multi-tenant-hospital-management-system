from django.http import Http404
from apps.platform_apps.hospitals.models import HospitalDomain
from apps.platform_apps.tenants.models import TenantDatabase
from .context import current_hospital, current_tenant_db
from .database import register_tenant_database

class TenantResolutionMiddleware:
    """
    Hostname -> verified HospitalDomain -> TenantDatabase.
    Unknown hosts remain on the control plane; tenant routes should
    explicitly require request.tenant before accessing tenant data.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.tenant = None
        request.tenant_db = None
        host = request.get_host().split(":")[0].lower()

        hospital = None
        tenant_alias = None
        try:
            domain = HospitalDomain.objects.select_related("hospital").get(
                hostname=host, is_verified=True, hospital__status="active"
            )
            tenant = TenantDatabase.objects.get(
                hospital=domain.hospital, status=TenantDatabase.Status.READY
            )
            hospital = domain.hospital
            tenant_alias = f"tenant_{hospital.pk.hex}"
            register_tenant_database(tenant_alias, tenant.database_name)
        except (HospitalDomain.DoesNotExist, TenantDatabase.DoesNotExist):
            pass

        request.tenant = hospital
        request.tenant_db = tenant_alias
        token_h = current_hospital.set(hospital)
        token_db = current_tenant_db.set(tenant_alias)
        try:
            response = self.get_response(request)
        finally:
            current_tenant_db.reset(token_db)
            current_hospital.reset(token_h)
        return response
