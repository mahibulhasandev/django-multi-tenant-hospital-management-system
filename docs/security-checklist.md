# Security Checklist Before Production

- Use a strong secret key and secrets manager; never commit `.env`.
- Use TLS for database and web connections.
- Use least-privilege PostgreSQL roles.
- Enforce verified-host tenant resolution and active tenant checks.
- Enforce tenant membership and role authorization on every tenant endpoint.
- Never accept tenant database aliases/names from user input.
- Add rate limiting, CSRF protection, secure cookies, and audit events.
- Add tenant isolation tests for reads, writes, admin, background jobs, and exports.
- Define tenant backup, restore, retention, and deletion policies.
- Use controlled migration orchestration and monitor schema versions.
