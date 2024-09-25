# MedicaRecord

MedicaRecord is a project for managing electronic health records (EHR) using Django microservices. This README provides instructions on setting up the development environment and guidelines for naming conventions.

## Getting Started

### Prerequisites

Make sure you have [Poetry](https://python-poetry.org/docs/) installed on your machine to manage dependencies and virtual environments.

### Setting Up the Virtual Environment

To activate the virtual environment, run:

```bash
poetry shell
```

To install dependencies


```bash
poetry install
```
To add a dependency 


```bash
poetry add package_name
```

# Naming conventions

. Model Names: Use CamelCase (e.g., PatientRecord, Appointment).

. Field Names: Use lowercase (e.g., patient_name, appointment_date).


