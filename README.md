# Django Multi-Tenant Hospital Management System

A Django-based **Multi-Tenant Hospital Management SaaS Platform** designed to manage multiple hospitals through a centralized platform while maintaining separate databases for each hospital.

The system aims to digitize hospital operations, simplify administrative management, and provide scalable healthcare management solutions.

**Project Status:** 🚧 Under Development

---

## Project Overview

This project is designed as a Software as a Service (SaaS) platform where multiple hospitals can operate independently within a centralized management system.

Each hospital will have its own isolated PostgreSQL database, ensuring data separation, security, and independent hospital management.

The platform follows a **Control Plane + Hospital Data Plane** architecture.

### Core Architecture

- **Control Plane:** Manages the overall platform, hospitals, platform administrators, and tenant configurations.
- **Hospital Data Plane:** Handles each hospital's operational data through its own dedicated database.
- **Multi-Tenancy:** Supports multiple hospitals within one application.
- **Database Isolation:** Each hospital maintains a separate PostgreSQL database.

---

## Key Features

### 1. Platform Management
- Platform Administrator Management
- Hospital Registration and Creation
- Hospital Configuration
- Hospital Activation and Deactivation
- Tenant Database Management
- Platform-Level Monitoring

### 2. Hospital Management
- Hospital Dashboard
- Hospital Staff Management
- Department Management
- Role-Based Access Control
- Hospital Profile Management

### 3. Department Management

The system is designed to support independently configurable hospital departments.

- Doctor Department
- Nurse Department
- Clinic / OPD Department
- Pharmacy Department
- Diagnostic / Laboratory Department
- Accounts Department
- Admission Department
- Blood Bank Department
- Management Department

### 4. Healthcare Operations
- Patient Management
- Doctor Management
- Nurse Management
- Appointment Management
- OPD Management
- Medical Records
- Prescription Management
- Pharmacy Management
- Laboratory Management
- Billing and Payment
- Admission and Discharge
- Inventory Management

### 5. Multi-Tenant Database Architecture
- Separate PostgreSQL Database for Each Hospital
- Tenant Database Provisioning
- Dynamic Database Connection Management
- Tenant Resolution
- Database Migration Management
- Hospital Data Isolation

---

## System Architecture

```text
                    SaaS Platform
                          |
                   Control Plane
                          |
                Platform Administration
                          |
                  Hospital Management
                          |
                   Tenant Resolver
                          |
             +------------+------------+
             |            |            |
          Hospital A   Hospital B   Hospital C
             |            |            |
          Database A  Database B  Database C
             |            |            |
          Hospital     Hospital     Hospital
          Operations   Operations   Operations
```

Each hospital operates independently with its own database while sharing the central application infrastructure.

---

## Technology Stack

### Backend
- Python
- Django
- Django REST Framework

### Database
- PostgreSQL

### Frontend
- HTML5
- CSS3
- JavaScript
- Django Templates
- Tailwind CSS

### Development Tools
- Git
- GitHub
- VS Code
- Linux

---

## Architecture Approach

The project follows a **Modular Monolith Architecture** initially, with a clear separation between platform-level and hospital-level responsibilities.

### Control Plane Applications
- Platform Accounts
- Hospital Registry
- Tenant Management
- Department Templates
- Subscription Management
- Platform Audit Logs

### Hospital Applications
- Accounts
- Departments
- Doctors
- Nurses
- Patients
- Appointments
- Clinic
- Pharmacy
- Diagnostics
- Accounts Management
- Admission
- Blood Bank
- Inventory

---

## Database Strategy

The project uses a separate PostgreSQL database for each hospital.

| Database | Responsibility |
|---|---|
| Control Plane DB | Platform and hospital configuration |
| Hospital A DB | Hospital A operational data |
| Hospital B DB | Hospital B operational data |
| Hospital C DB | Hospital C operational data |

**Important:** Hospital databases remain isolated. Cross-database relationships will be handled through application-level identifiers and controlled integration mechanisms.

---

## Project Goals

- Build a scalable Hospital Management SaaS platform.
- Support multiple hospitals from one centralized platform.
- Maintain hospital-level database isolation.
- Provide configurable hospital departments.
- Implement secure authentication and authorization.
- Simplify hospital administration and healthcare operations.
- Build a maintainable and extensible Django architecture.

---

## Development Roadmap

- [ ] Project Foundation and Configuration
- [ ] Control Plane Architecture
- [ ] Platform Authentication and Authorization
- [ ] Hospital Registry and Management
- [ ] Tenant Database Architecture
- [ ] Dynamic Database Connection Management
- [ ] Automated Tenant Provisioning
- [ ] Hospital Authentication and Membership
- [ ] Department Configuration
- [ ] Doctor and Nurse Management
- [ ] Patient Management
- [ ] Appointment and Clinic Management
- [ ] Pharmacy Management
- [ ] Diagnostic and Laboratory Management
- [ ] Accounts and Billing Management
- [ ] Admission and Blood Bank Management
- [ ] Reporting and Analytics
- [ ] Security and Audit Logging
- [ ] Testing and Deployment

---

## Installation

Installation instructions will be added as the project structure and environment configuration are finalized.

---

## Project Status

🚧 This project is currently under active development. Features, architecture, and implementation details may evolve throughout development.

---

## Author

**Mahibul Hasan**

GitHub: [@mahibulhasandev](https://github.com/mahibulhasandev)

---

## License

License information will be added later.
