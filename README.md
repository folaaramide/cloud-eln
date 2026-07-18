# Cloud ELN (Electronic Laboratory Notebook)

A cloud-based Electronic Laboratory Notebook (ELN) built with Flask and SQLAlchemy. The project demonstrates full-stack application development and will evolve into a production-ready cloud-native application deployed on AWS using Docker, Terraform, CI/CD and Kubernetes.

---

## Features

### Authentication
- User registration
- Secure login/logout
- Password hashing
- Protected routes

### Experiment Management
- Create experiments
- View experiment details
- Edit experiments
- Delete experiments

### Dashboard
- Live experiment statistics
- Recent experiments

### Database
- SQLAlchemy ORM
- SQLite database
- Flask-Migrate support

---

## Technology Stack

### Backend
- Python 3
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Migrate

### Frontend
- HTML5
- Bootstrap 5
- Jinja2

### Database
- SQLite (Current)
- PostgreSQL (Planned)

### Cloud & DevOps Roadmap
- Docker
- Docker Compose
- AWS EC2
- Terraform
- GitHub Actions
- Kubernetes
- Cloud Monitoring

---

## Project Structure

```
cloud-eln/
│
├── app/
├── migrations/
├── instance/
├── static/
├── templates/
│
├── run.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/folaaramide/cloud-eln.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Current Status

✔ Authentication

✔ Dashboard

✔ Complete Experiment CRUD

✔ SQLite Database

✔ Bootstrap UI

---

## Next Milestones

- Docker
- PostgreSQL
- AWS Deployment
- Terraform
- GitHub Actions CI/CD
- Kubernetes
- Monitoring

---

## Author

**Afolabi Aramide**

Graduate Cloud Engineer | AWS | Terraform | Python | DevOps
