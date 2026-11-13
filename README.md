# Django Multi-Tenant Hospital Management System

A Django-based multi-tenant Hospital Management SaaS foundation. The platform uses a central Control Plane database and a dedicated PostgreSQL database for each hospital tenant.

**Status:** Foundation / early development.

## Architecture

- **Control Plane (`default` database):** Platform identities, hospital registry, verified domains, tenant database metadata.
- **Hospital Data Plane:** Hospital-specific data in isolated PostgreSQL databases.
- **Identity:** One central `PlatformUser`; tenant databases store memberships using the central user's UUID. No cross-database foreign keys.
- **Application style:** Modular monolith.

## Current foundation apps

- `platform_accounts`: central platform identity.
- `hospitals`: hospital registry and hostname mapping.
- `tenants`: tenant database metadata.
- `hospital_accounts`: hospital membership model, intended for tenant databases.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements/development.txt`.
3. Copy `.env.example` to `.env` and set a strong `DJANGO_SECRET_KEY` and PostgreSQL credentials.
4. Create the control-plane PostgreSQL database.
5. Run `python manage.py check`.
6. Run `python manage.py makemigrations platform_accounts hospitals tenants hospital_accounts`.
7. Run `python manage.py migrate`.
8. Create a platform superuser: `python manage.py createsuperuser`.

Set `DJANGO_SETTINGS_MODULE=config.settings.development` when running management commands if needed.

## Important tenant database notes

- Tenant database credentials are not stored in application tables. This starter assumes a shared PostgreSQL service account supplied through environment configuration; production deployments should use a secrets manager and least-privilege database roles.
- Tenant database provisioning, migrations, backups, connection lifecycle, tenant-aware authentication/authorization, and operational monitoring must be completed before production.
- The included hostname middleware is a minimal resolver foundation, not a complete security boundary. Tenant views must enforce a resolved, active tenant and membership authorization.
- Do not expose arbitrary database aliases or let request parameters choose a database.
- Do not use cross-database foreign keys or assume transactions span databases.

## Development

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Roadmap

- [x] Initial project and settings separation
- [x] Central platform identity model
- [x] Hospital registry and domain model
- [x] Tenant database metadata model
- [x] Tenant routing/context foundation
- [ ] Secure tenant provisioning service and command
- [ ] Tenant migration orchestration
- [ ] Hospital invitation and membership authentication
- [ ] Department templates and configuration
- [ ] Healthcare modules
- [ ] Tenant isolation/security test suite
- [ ] Production deployment and operations

## License

MIT
