# 🚀 RAG Web Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)
![Vue](https://img.shields.io/badge/Vue-3.4+-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**A modern Retrieval-Augmented Generation (RAG) web application with document management and intelligent chat capabilities.**

[Demo](#) · [Report Bug](https://github.com/Myrythm/rag-web-gpt/issues) · [Request Feature](https://github.com/Myrythm/rag-web-gpt/issues)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🎯 Core Functionality

- **📄 Document Upload & Management** - Upload PDF documents and automatically chunk them for RAG
- **💬 Intelligent Chat** - Ask questions and get answers based on your uploaded documents
- **🔍 Vector Search** - Powered by ChromaDB for semantic similarity search
- **📊 Admin Dashboard** - Manage users, documents, and system settings
- **🔐 Authentication & Authorization** - Secure login with role-based access control (Admin/User)
- **📱 Responsive Design** - Beautiful, modern UI that works on all devices

### 🛠️ Advanced Features

- **Pagination** - Efficient data browsing for large datasets
- **Search & Filter** - Find users and documents quickly
- **Chat History** - Persistent conversation storage with session management
- **Real-time Updates** - Dynamic content loading without page refresh

---

## 🛠️ Tech Stack

### Backend

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[LangChain](https://python.langchain.com/)** - LLM orchestration framework (v1.0)
- **[ChromaDB](https://www.trychroma.com/)** - Vector database for embeddings
- **[SQLite](https://www.sqlite.org/)** - Lightweight database for user & metadata storage
- **[OpenAI API](https://openai.com/)** - GPT models for chat completion

### Frontend

- **[Vue 3](https://vuejs.org/)** - Progressive JavaScript framework
- **[Pinia](https://pinia.vuejs.org/)** - State management
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Vue Router](https://router.vuejs.org/)** - Official router for Vue.js
- **[Axios](https://axios-http.com/)** - HTTP client

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** - [Download](https://www.python.org/downloads/)
- **Node.js 16+** - [Download](https://nodejs.org/)
- **npm or yarn** - Comes with Node.js
- **OpenAI API Key** - [Get one here](https://platform.openai.com/api-keys)

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Myrythm/rag-web-gpt.git
cd rag-web-gpt
```

### 2️⃣ Backend Setup

#### Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Initialize Database & Create Admin User

```bash
python create_admin.py
```

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Database
SQLITE_DB_PATH=./rag_web.db

# Security (Generate a secure random string)
SECRET_KEY=your_secret_key_here
```

**Generate a secure SECRET_KEY:**

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🎮 Usage

### Running the Application

#### Start Backend Server

```bash
# Make sure you're in the root directory with venv activated
uvicorn backend.main:app --reload
```

The backend API will be available at: **http://localhost:8000**

API Documentation: **http://localhost:8000/docs**

#### Start Frontend Development Server

```bash
cd frontend
npm run dev
```

The frontend will be available at: **http://localhost:5173**

### Default Admin Credentials

After running `create_admin.py`, you can log in with:

- **Username**: `admin` (or the one you created)
- **Password**: (the one you set)

---

## 📁 Project Structure

```
rag-web-gpt/
├── backend/
│   ├── chains/              # LangChain RAG logic
│   ├── routes/              # API endpoints
│   ├── services/            # Business logic (DB, embedding, chunking)
│   ├── utils/               # Utilities (auth, security, config)
│   └── main.py              # FastAPI app entry point
├── frontend/
│   ├── src/
│   │   ├── components/      # Vue components (admin, chat, common)
│   │   ├── pages/           # Page components
│   │   ├── router/          # Vue Router configuration
│   │   ├── stores/          # Pinia state management
│   │   └── utils/           # Frontend utilities
│   └── index.html           # Main HTML file
├── chroma/                  # ChromaDB vector storage (auto-generated)
├── .env                     # Environment variables (create this)
├── .env.example             # Example environment file
├── create_admin.py          # Script to create admin user
├── requirements.txt         # Python dependencies
└── README.md                # You are here!
```

---

## 🎯 Features Roadmap

- [x] Document upload and processing
- [x] RAG-based Q&A
- [x] User authentication
- [x] Admin dashboard
- [x] Search and filtering
- [ ] Multi-file format support (DOCX, TXT, etc.)
- [ ] Export chat history
- [ ] Dark/Light theme toggle
- [ ] API rate limiting
- [ ] Docker deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **OpenAI** for GPT models
- **LangChain** for RAG framework
- **ChromaDB** for vector storage
- **FastAPI** and **Vue.js** communities

---

## 📧 Contact

**GitHub**: [@Myrythm](https://github.com/Myrythm)

**Repository**: [rag-web-gpt](https://github.com/Myrythm/rag-web-gpt)

---

<div align="center">
  
**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Myrythm](https://github.com/Myrythm)

</div>
