from django.conf import settings
from django.db import connections

def register_tenant_database(alias: str, database_name: str) -> None:
    """
    Register a tenant DB alias using the deployment's shared PostgreSQL
    service credentials. Credentials are never stored in TenantDatabase.
    """
    if alias in connections.databases:
        return
    default = connections.databases["default"].copy()
    default["NAME"] = database_name
    connections.databases[alias] = default
