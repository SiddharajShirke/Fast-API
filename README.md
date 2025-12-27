# 🚀 Simple Social - FastAPI + Streamlit Social Media Platform

A modern, full-stack social media application built with **FastAPI** backend and **Streamlit** frontend. Features user authentication, media uploads, feed functionality, and real-time image processing with ImageKit integration.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.124.2-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.52.2-FF4B4B.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red.svg)

## 📑 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🔧 Configuration](#-configuration)
- [📚 API Documentation](#-api-documentation)
- [💻 Usage Guide](#-usage-guide)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

## ✨ Features

### 🔐 **Authentication & User Management**
- ✅ User registration and login
- ✅ JWT token-based authentication
- ✅ Password hashing with Argon2/Bcrypt
- ✅ Secure session management
- ✅ User profile management

### 📸 **Media Management**
- ✅ Image and video uploads
- ✅ ImageKit integration for cloud storage
- ✅ Real-time image transformations
- ✅ Caption overlay on media
- ✅ Automatic file type detection
- ✅ Optimized media delivery

### 🏠 **Social Feed**
- ✅ Chronological post feed
- ✅ Real-time post updates
- ✅ Post deletion (owner only)
- ✅ Media preview with captions
- ✅ User attribution
- ✅ Responsive design

### 🎨 **Modern UI**
- ✅ Clean Streamlit interface
- ✅ Mobile-responsive design
- ✅ Dark/Light theme support
- ✅ Interactive file uploads
- ✅ Real-time notifications

## 🛠️ Tech Stack

### **Backend**
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework
- **[FastAPI Users](https://fastapi-users.github.io/)** - User authentication
- **[SQLAlchemy](https://sqlalchemy.org/)** - Database ORM with async support
- **[SQLite](https://sqlite.org/)** - Lightweight database
- **[Pydantic](https://pydantic.dev/)** - Data validation
- **[ImageKit](https://imagekit.io/)** - Image processing and CDN

### **Frontend**
- **[Streamlit](https://streamlit.io/)** - Interactive web application framework
- **[Requests](https://requests.readthedocs.io/)** - HTTP client

### **Security & Authentication**
- **[PyJWT](https://pyjwt.readthedocs.io/)** - JSON Web Token implementation
- **[Argon2-CFFI](https://argon2-cffi.readthedocs.io/)** - Password hashing
- **[Bcrypt](https://github.com/pyca/bcrypt/)** - Password hashing
- **[Cryptography](https://cryptography.io/)** - Cryptographic recipes

## 📁 Project Structure

```
Fast-API/
├── 📁 app/                     # FastAPI backend application
│   ├── 📄 app.py              # Main FastAPI application
│   ├── 📄 db.py               # Database models and connection
│   ├── 📄 schema.py           # Pydantic schemas
│   ├── 📄 Users.py            # User authentication logic
│   ├── 📄 image.py            # ImageKit configuration
│   └── 📁 __pycache__/        # Python cache
├── 📁 venv/                   # Virtual environment
├── 📄 frontend.py             # Streamlit frontend application
├── 📄 main.py                 # Alternative entry point
├── 📄 requirements.txt        # Python dependencies
├── 📄 .env                    # Environment variables
├── 📄 .gitignore             # Git ignore file
├── 📄 test.db                # SQLite database
├── 📄 FIXES_DOCUMENTATION.md # Development fixes log
└── 📄 README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.11+** installed
- **Git** installed
- **ImageKit account** (for media processing)

### 1. Clone the Repository
```bash
git clone https://github.com/SiddharajShirke/Fast-API.git
cd Fast-API
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Create .env file
echo "IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key" > .env
```

### 5. Start the Applications
```bash
# Terminal 1: Start FastAPI backend
uvicorn app.app:app --reload --port 8000

# Terminal 2: Start Streamlit frontend
streamlit run frontend.py
```

### 6. Access the Application
- **Frontend**: http://localhost:8501
- **Backend API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs

## ⚙️ Installation & Setup

### Detailed Installation Steps

#### 1. **System Requirements**
```bash
# Check Python version
python --version  # Should be 3.11+

# Check pip version
pip --version
```

#### 2. **Clone and Navigate**
```bash
git clone https://github.com/SiddharajShirke/Fast-API.git
cd Fast-API
```

#### 3. **Virtual Environment Setup**
```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows Command Prompt
python -m venv venv
venv\Scripts\activate.bat

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 4. **Install Dependencies**
```bash
# Install all requirements
pip install -r requirements.txt

# Or install individually
pip install fastapi[standard] fastapi-users[sqlalchemy] streamlit
pip install sqlalchemy aiosqlite imagekitio
pip install python-dotenv python-multipart
```

#### 5. **Database Setup**
```bash
# The database will be created automatically on first run
# SQLite file: test.db
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# ImageKit Configuration (Required for media uploads)
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key_here

# Optional: Custom configuration
IMAGEKIT_PUBLIC_KEY=your_public_key  # Not used in current version
IMAGEKIT_URL=your_imagekit_url       # Not used in current version

# Database (Optional - defaults to SQLite)
DATABASE_URL=sqlite+aiosqlite:///./test.db
```

### ImageKit Setup

1. **Create ImageKit Account**
   - Visit [ImageKit.io](https://imagekit.io/)
   - Sign up for a free account
   - Get your private key from the dashboard

2. **Configure ImageKit**
   - Copy your private key
   - Add it to the `.env` file
   - The application will handle the rest automatically

### Advanced Configuration

#### Database Configuration
```python
# app/db.py - Modify database URL if needed
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
```

#### Authentication Settings
```python
# app/Users.py - Modify JWT settings
SECRET = "your_secret_key_here"  # Change in production
```

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Body |
|--------|----------|-------------|------|
| `POST` | `/auth/register` | Register new user | `{"email": "user@example.com", "password": "password123"}` |
| `POST` | `/auth/jwt/login` | Login user | `username=user@example.com&password=password123` |
| `GET` | `/users/me` | Get current user info | Requires: `Authorization: Bearer <token>` |

### Content Endpoints

| Method | Endpoint | Description | Body/Params |
|--------|----------|-------------|-------------|
| `POST` | `/upload` | Upload media file | `file`: File, `caption`: String |
| `GET` | `/feed` | Get all posts | Requires: `Authorization: Bearer <token>` |
| `DELETE` | `/posts/{post_id}` | Delete a post | Requires: Post ownership |

### API Response Examples

#### Registration Response
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```

#### Login Response
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer"
}
```

#### Feed Response
```json
{
  "posts": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "user_id": "456e7890-e89b-12d3-a456-426614174001",
      "caption": "Beautiful sunset!",
      "url": "https://ik.imagekit.io/demo/sunset.jpg",
      "file_type": "image",
      "file_name": "sunset.jpg",
      "created_at": "2025-12-28T10:30:00.000Z",
      "is_owner": true,
      "email": "user@example.com"
    }
  ]
}
```

## 💻 Usage Guide

### 1. **User Registration & Login**
```python
# Frontend automatically handles this through Streamlit interface
# 1. Enter email and password
# 2. Click "Sign Up" to register
# 3. Click "Login" to authenticate
# 4. JWT token is stored in session
```

### 2. **Uploading Media**
```python
# Through Streamlit interface:
# 1. Navigate to "📸 Upload" tab
# 2. Choose image/video file
# 3. Add caption (optional)
# 4. Click "Share"
```

### 3. **Viewing Feed**
```python
# Automatic on login:
# 1. Posts displayed in chronological order
# 2. View images/videos with captions
# 3. Delete your own posts with 🗑️ button
```

### 4. **API Usage Examples**

#### Using cURL
```bash
# Register user
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'

# Login
curl -X POST "http://127.0.0.1:8000/auth/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=test123"

# Get feed
curl -X GET "http://127.0.0.1:8000/feed" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### Using Python Requests
```python
import requests

# Login
login_data = {"username": "test@example.com", "password": "test123"}
response = requests.post("http://127.0.0.1:8000/auth/jwt/login", data=login_data)
token = response.json()["access_token"]

# Get feed
headers = {"Authorization": f"Bearer {token}"}
feed_response = requests.get("http://127.0.0.1:8000/feed", headers=headers)
posts = feed_response.json()["posts"]
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. **Application Won't Start**
```bash
# Problem: ModuleNotFoundError
# Solution: Install dependencies
pip install -r requirements.txt

# Problem: Port already in use
# Solution: Kill existing processes or use different ports
uvicorn app.app:app --reload --port 8001
streamlit run frontend.py --server.port 8502
```

#### 2. **Database Issues**
```bash
# Problem: Database locked or corrupted
# Solution: Delete and recreate database
rm test.db
# Restart the FastAPI server to recreate database
```

#### 3. **Authentication Problems**
```bash
# Problem: Login fails
# Solution: Check if user exists, verify password
# Check FastAPI logs for detailed error messages
```

#### 4. **Image Upload Issues**
```bash
# Problem: Upload fails
# Solution: Verify ImageKit configuration
# Check .env file has correct IMAGEKIT_PRIVATE_KEY
```

#### 5. **Frontend Not Connecting to Backend**
```bash
# Problem: Connection refused
# Solution: Ensure FastAPI is running on correct port
# Check URLs in frontend.py match backend address
```

### Debug Mode

#### Enable FastAPI Debug Logging
```python
# Add to app/app.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Enable Streamlit Debug Mode
```bash
streamlit run frontend.py --logger.level debug
```

### Performance Optimization

#### Database Optimization
```python
# Add database indexes for better performance
# Consider PostgreSQL for production use
```

#### Image Optimization
```python
# ImageKit automatically optimizes images
# Configure additional transformations as needed
```

## 🤝 Contributing

### Development Setup

1. **Fork the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/Fast-API.git
cd Fast-API
```

2. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Make Changes and Test**
```bash
# Run tests
python -m pytest tests/  # If tests exist

# Check code style
flake8 app/ frontend.py

# Format code
black app/ frontend.py
```

4. **Commit and Push**
```bash
git add .
git commit -m "Add your feature description"
git push origin feature/your-feature-name
```

5. **Create Pull Request**

### Code Style Guidelines

- **Python**: Follow PEP 8
- **FastAPI**: Use type hints and async/await
- **Streamlit**: Keep components modular
- **Comments**: Document complex logic

### Testing Guidelines

```python
# Example test structure
def test_user_registration():
    # Test user registration endpoint
    pass

def test_media_upload():
    # Test file upload functionality
    pass
```

## 📊 Performance & Scaling

### Current Limitations
- **Database**: SQLite (single-file, not suitable for high concurrency)
- **File Storage**: ImageKit dependency
- **Sessions**: In-memory (not persistent across restarts)

### Production Recommendations
- **Database**: PostgreSQL with connection pooling
- **File Storage**: Multiple CDN providers
- **Deployment**: Docker containers with load balancer
- **Monitoring**: Application performance monitoring
- **Caching**: Redis for session storage

## 🔒 Security Considerations

### Current Security Features
- ✅ Password hashing with Argon2/Bcrypt
- ✅ JWT token authentication
- ✅ Input validation with Pydantic
- ✅ SQL injection protection (SQLAlchemy ORM)
- ✅ File type validation

### Production Security Checklist
- [ ] Environment variable validation
- [ ] Rate limiting implementation
- [ ] CORS configuration
- [ ] HTTPS enforcement
- [ ] Security headers
- [ ] Input sanitization
- [ ] File size limits
- [ ] User permissions system

## 📝 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Siddharaj Shirke

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Support & Contact

- **GitHub Issues**: [Create an Issue](https://github.com/SiddharajShirke/Fast-API/issues)
- **Documentation**: Check this README and API docs at `/docs`
- **Email**: [Contact via GitHub](https://github.com/SiddharajShirke)

---

## 🎯 Roadmap

### Short Term (v2.0)
- [ ] Real-time notifications
- [ ] User profiles with avatars
- [ ] Post likes and comments
- [ ] Search functionality
- [ ] Mobile responsive improvements

### Medium Term (v3.0)
- [ ] Private messaging
- [ ] Group creation
- [ ] Story features
- [ ] Video streaming
- [ ] Advanced analytics

### Long Term (v4.0)
- [ ] AI-powered content moderation
- [ ] Machine learning recommendations
- [ ] Multi-language support
- [ ] Enterprise features
- [ ] Mobile app

---

**⭐ Star this repository if you found it helpful!**

*Built with ❤️ using FastAPI and Streamlit*