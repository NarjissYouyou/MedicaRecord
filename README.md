
# MedicaRecord

**MedicaRecord** is a project designed for managing electronic health records (EHR) using Django microservices architecture. This document outlines how to set up the development environment, use Docker, and follow naming conventions throughout the project.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
   - [Virtual Environment](#virtual-environment)
   - [Dependency Management](#dependency-management)
3. [Naming Conventions](#naming-conventions)
4. [Docker Usage](#docker-usage)
5. [Database Migrations via Docker](#database-migrations-via-docker)

---

## Prerequisites

Before setting up the project, ensure the following software is installed:

- Docker: For containerized development.

---

## Project Setup

### Virtual Environment

To create and activate the virtual environment using Poetry (this is for running one of the services manually otherwise docker handles it):

```bash
poetry shell
```

### Dependency Management

To install all project dependencies:

```bash
poetry install
```

To add a new package dependency:

```bash
poetry add <package_name>
```

---

## Naming Conventions

Ensure the following naming conventions are followed consistently across the project:

- **Model Names**: Use `CamelCase`. Example: `PatientRecord`, `Appointment`.
- **Field Names**: Use `snake_case` (all lowercase with underscores). Example: `patient_name`, `appointment_date`.

---

## Docker Usage

Below are some common Docker commands used in the development workflow:

- **Build Docker containers**:

    ```bash
    sudo docker compose build
    ```

- **Start Docker containers in detached mode**:

    ```bash
    sudo docker compose up -d
    ```

- **Stop and remove containers**:

    ```bash
    sudo docker compose down
    ```

- **Prune unused Docker resources**:

    ```bash
    sudo docker system prune -a
    ```

- **Stop running containers**:

    ```bash
    sudo docker stop $(sudo docker ps -q)
    ```

- **Remove stopped containers**:

    ```bash
    sudo docker container prune
    ```

---

## Database Migrations via Docker

To manage database migrations from within Docker containers:

- **Make migrations**:

    ```bash
    sudo docker compose exec <service_name> python manage.py makemigrations
    ```

- **Apply migrations**:

    ```bash
    sudo docker compose exec <service_name> python manage.py migrate
    ```

---

This document should guide you through the setup and basic usage of the MedicaRecord project. For further assistance, refer to the official documentation of [Django](https://docs.djangoproject.com/) and [Poetry](https://python-poetry.org/docs/).