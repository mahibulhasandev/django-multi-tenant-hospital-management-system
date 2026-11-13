# Architecture Decisions

## 1. Control Plane and Data Plane
The control plane owns platform identities, hospital registry, domains, and tenant database metadata. Each hospital's operational data belongs in its own PostgreSQL database.

## 2. Identity and membership
Django has one project-wide `AUTH_USER_MODEL`. This foundation uses `PlatformUser` as the central identity. Each tenant database stores `HospitalMembership.global_user_id` as a UUID, not a foreign key. Authorization must verify both the central identity and the membership in the currently resolved tenant.

## 3. Tenant resolution
Resolve a normalized request hostname against a verified `HospitalDomain` in the control database. Only active hospitals with READY tenant databases may resolve. Never accept a database name or alias from request input.

## 4. Database boundaries
No cross-database foreign keys. No assumption of cross-database atomic transactions. Use explicit service boundaries and idempotent workflows for operations spanning control and tenant databases.

## 5. Production requirements
Add secrets management, tenant provisioning orchestration, migration orchestration, connection limits/pooling, tenant backups, audit logging, monitoring, and security tests before production use.
