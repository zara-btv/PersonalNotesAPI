# 📒 Personal Notes API

Simple API for managing personal notes, built with **Django Rest Framework**.

## ✨ Features

- 🔐 User registration & login
- 📝 Create, edit & delete notes

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip
  
## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register user |
| POST | `/api/login/` | Login (get token) |
| GET | `/api/notes/` | List all notes |
| POST | `/api/notes/` | Create note |
| PUT | `/api/notes/<id>/` | Update note |
| DELETE | `/api/notes/<id>/` | Delete note |

> 🔑 For protected endpoints, send token in header: `Authorization: Token your-token`

Author
zara-btv 
