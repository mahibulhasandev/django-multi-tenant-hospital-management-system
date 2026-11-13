from contextvars import ContextVar

current_tenant_db = ContextVar("current_tenant_db", default=None)
current_hospital = ContextVar("current_hospital", default=None)
