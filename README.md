# 🚀 DevOps CI/CD Microservice

<p align="center">
  <strong>A containerized full-stack microservice with automated CI, REST APIs, Redis persistence, and Docker Compose.</strong>
</p>

<p align="center">
  <a href="https://github.com/shaikumar11/devops-cicd-microservice">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <a href="https://github.com/shaikumar11/devops-cicd-microservice/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/shaikumar11/devops-cicd-microservice/ci.yml?branch=main&style=for-the-badge&logo=githubactions&logoColor=white&label=CI" alt="CI Status">
  </a>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Redis-Data%20Store-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
</p>

---

## 📌 Overview

**DevOps CI/CD Microservice** is a Dockerized full-stack application designed to demonstrate practical DevOps and backend engineering concepts.

The application consists of a frontend, a Python backend API, and Redis for persistent application data. The complete stack can be started with a single Docker Compose command.

The project also includes a **GitHub Actions CI pipeline** that automatically tests the backend and builds the Docker environment whenever changes are pushed to the `main` branch.

### 🎯 What this project demonstrates

* 🐳 Containerized application development
* 🔗 Frontend-to-backend API communication
* ⚡ REST API development with FastAPI
* 🗄️ Redis-based persistence
* 🧩 Multi-container orchestration with Docker Compose
* 🧪 Automated backend testing
* 🔄 GitHub Actions CI
* 📦 Dependency management
* 🌐 Production-oriented project structure

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🖥️ Frontend

Interactive web interface for adding and viewing items.

</td>
<td width="50%">

### ⚡ REST API

Python-based backend exposing API endpoints for application data.

</td>
</tr>

<tr>
<td width="50%">

### 🗄️ Redis Persistence

Application data is stored in Redis and remains available after browser refreshes.

</td>
<td width="50%">

### 🐳 Docker

Frontend, backend, and Redis run as containerized services.

</td>
</tr>

<tr>
<td width="50%">

### 🔄 CI Pipeline

GitHub Actions automatically installs dependencies, executes tests, and builds Docker services.

</td>
<td width="50%">

### 🧪 Automated Testing

Backend tests are executed automatically during CI.

</td>
</tr>
</table>

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │      Browser        │
                         │                     │
                         │   Frontend :3000    │
                         └──────────┬──────────┘
                                    │
                                    │ HTTP
                                    ▼
                         ┌─────────────────────┐
                         │       Backend       │
                         │                     │
                         │     FastAPI :5000   │
                         └──────────┬──────────┘
                                    │
                                    │ Redis protocol
                                    ▼
                         ┌─────────────────────┐
                         │        Redis        │
                         │                     │
                         │    Persistent Data  │
                         └─────────────────────┘


                    CI/CD FLOW
                         
                         Git Push
                            │
                            ▼
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
               Install/Test      Docker Build
                    │                 │
                    └────────┬────────┘
                             ▼
                          CI Result
                       ✅ Pass / ❌ Fail
```

---

## 🛠️ Technology Stack

| Layer            | Technology       |
| ---------------- | ---------------- |
| Frontend         | React + Vite     |
| Backend          | Python + FastAPI |
| Database / Cache | Redis            |
| Containerization | Docker           |
| Orchestration    | Docker Compose   |
| Testing          | Pytest           |
| CI               | GitHub Actions   |
| Version Control  | Git + GitHub     |
| Web Server       | Nginx            |

---

## 📂 Project Structure

```text
devops-cicd-microservice/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   └── test_app.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── docker-compose.yml
└── .gitignore
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have the following installed:

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Git
* A GitHub account if you want to use the CI pipeline

Verify Docker:

```powershell
docker --version
docker compose
```
