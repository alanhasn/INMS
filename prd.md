# Product Requirements Document (PRD) – Internal Network Management System (INMS)

**Document Version:** 1.0
**Last Updated:** 22-Aug-2025

---

## 1. Introduction

### 1.1 Purpose

This document defines the requirements, features, and specifications for the **Internal Network Management System (INMS)** MVP. The goal is to provide a centralized system for managing network devices, tracking user actions, logging system events, and generating reports. This document serves as a guide for stakeholders and the development team to ensure alignment on project objectives.

### 1.2 Background

Organizations managing internal IT infrastructure need tools to track devices, monitor events, and manage user roles securely. Existing enterprise solutions can be overly complex or costly. INMS provides a lightweight yet robust Django-based solution for small to mid-sized organizations.

### 1.3 Scope

**In Scope:**

* User authentication and role-based permissions (Admin, Manager, Employee).
* Device management (CRUD operations for network devices).
* Event logging (system events, user actions, device status changes).
* Basic reports and dashboards.
* Simple web interface with Django Templates (Bootstrap).

**Out of Scope (for MVP):**

* Advanced threat intelligence integrations (e.g., IP reputation APIs).
* AI/ML analytics.
* Real-time monitoring or alerting systems.
* Mobile application support.

---

## 2. Goals and Objectives

### 2.1 Business Goals

* Provide a cost-effective internal system to manage devices and user access.
* Improve visibility into user actions and system events.
* Reduce time required to track network issues.

### 2.2 User Goals

* Admins: Manage users, roles, and permissions.
* Managers: Oversee devices and generate reports.
* Employees: Access devices relevant to their role.

### 2.3 Success Metrics

* System adoption by at least **80% of internal staff** in the first month.
* Ability to generate reports in under **5 seconds** for datasets < 10k records.
* Zero unauthorized access to restricted device data.

---

## 3. User Stories

### 3.1 User Personas

* **Admin**: IT administrator responsible for configuring the system and managing users.
* **Manager**: Department head overseeing device inventory and monitoring activity.
* **Employee**: Regular user with limited access to view assigned devices.

### 3.2 User Scenarios

* *As an Admin, I want to create users and assign roles so that access is properly controlled.*
* *As a Manager, I want to see a list of all active devices so that I can track infrastructure status.*
* *As an Employee, I want to view my assigned devices so that I can perform my daily tasks.*
* *As a Manager, I want to generate reports on events so that I can identify unusual activity.*

---

## 4. Functional Requirements

### 4.1 Core Features

1. **User Management**

   * Create, edit, and delete users.
   * Assign roles: Admin, Manager, Employee.
   * Enforce role-based permissions.

2. **Device Management**

   * CRUD operations for devices.
   * Fields: IP Address, MAC Address, Hostname, Device Type, Status.
   * Link devices to users (optional for MVP).

3. **Event Logging**

   * Log user actions (login, logout, failed login).
   * Log device actions (creation, update, deletion).
   * Store event type, user, device, timestamp.

4. **Reports**

   * Generate device summary (active vs inactive).
   * Generate event summary (logins, errors, device changes).
   * Export reports to CSV (PDF optional for later).

### 4.2 Supporting Features

* Dashboard displaying:

  * Number of users, devices, and events.
  * Recent activity log.
* Simple search and filters for devices and events.

---

## 5. Non-Functional Requirements

### 5.1 Performance

* Must handle up to **10,000 devices** and **100,000 events** without major performance issues.
* Reports should generate within **5 seconds**.

### 5.2 Security

* Role-based access control enforced at the model and view level.
* Encrypted password storage (Django default).
* Secure session handling (HTTPS recommended).

### 5.3 Usability

* Simple, responsive UI (Bootstrap + Django Templates).
* Accessible on desktop browsers.

### 5.4 Compatibility

* Supported browsers: Chrome, Firefox, Edge (latest versions).
* Platform: Web-based, runs on Linux server with PostgreSQL backend.

---

## 6. Technical Specifications

### 6.1 Architecture

* **MVC (Django CBVs)** structure with modular apps:

  * `users/`
  * `devices/`
  * `events/`
  * `reports/`

### 6.2 Technology Stack

* **Frontend:** Django Templates + Bootstrap.
* **Backend:** Django (Python).
* **Database:** PostgreSQL.
* **Other:** Django Admin for quick management.

### 6.3 Data Requirements

* **Users:** username, password, role, email.
* **Devices:** IP, MAC, hostname, type, status.
* **Events:** user, device, type, timestamp.

---

## 7. Project Timeline

### 7.1 Milestones

* **Week 1:** Project setup, user authentication & role system.
* **Week 2:** Device management module.
* **Week 3:** Event logging module.
* **Week 4:** Reporting module + dashboard.
* **Week 5:** Testing, bug fixes, documentation.

### 7.2 Release Plan

* **Version 1.0 (MVP):** Core features (Users, Devices, Events, Reports).
* **Future Versions:** Threat intelligence integrations, advanced analytics, alerting.

---

## 8. Risks and Assumptions

### 8.1 Risks

* **Risk 1:** Scope creep by adding too many advanced features early.

  * *Mitigation:* Stick to MVP core features only.
* **Risk 2:** Performance issues with large datasets.

  * *Mitigation:* Optimize queries and add indexes.

### 8.2 Assumptions

* Internal network environment is controlled.
* Users have basic technical literacy.
* Organization already maintains device information that can be imported.

---

## 9. Approval

### 9.1 Stakeholders

* **Project Owner:** IT Department.
* **Developers:** Internal software team.
* **End Users:** Admins, Managers, Employees.

### 9.2 Sign-off

* Stakeholders will review and approve before development begins.
