from django.conf import settings
from .context import current_tenant_db

class TenantDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in settings.TENANT_APP_LABELS:
            return current_tenant_db.get()
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in settings.TENANT_APP_LABELS:
            return current_tenant_db.get()
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        labels = {obj1._meta.app_label, obj2._meta.app_label}
        if labels <= settings.TENANT_APP_LABELS:
            return True
        if labels <= settings.CONTROL_APP_LABELS:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in settings.TENANT_APP_LABELS:
            return db != "default"
        if app_label in settings.CONTROL_APP_LABELS:
            return db == "default"
        return db == "default"
