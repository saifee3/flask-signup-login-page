# 🚀 Flask Signup & Login Page
<img src="https://github.com/user-attachments/assets/4fd697f8-83d8-4331-b47b-926aa7a07839" alt="Custom Icon" width="1050" height="700">

[![Flask](https://img.shields.io/badge/Framework-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-blue.svg)](https://www.sqlite.org/)

## 🌟 Features

- 📝 User registration with username, email, and password
- 🔑 Secure user login with email and password authentication
- 🔄 Password strength validation
- 📱 Fully responsive design for all devices
- 📄 SQLite database integration
- 🛡️ CORS support for API security
- 📦 Modular code structure for easy maintenance

## 🛠 Technologies Used

- **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-CORS
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Version Control**: Git, GitHub

---

## 🧩 Backend Implementation

### Database Model (`models.py`)
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
```

### Routes (`routes.py`)
- **Signup**: Handles user registration.
  ```python
  @app.route('/signup', methods=['POST'])
  def signup():
      data = request.get_json()
      if not all([data.get('username'), data.get('email'), data.get('password')]):
          return jsonify({"error": "All fields are required"}), 400
      if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
          return jsonify({"error": "Username or email already exists"}), 400
      user = User(username=data['username'], email=data['email'], password=data['password'])
      db.session.add(user)
      db.session.commit()
      return jsonify({"message": "User registered successfully"}), 201
  ```

- **Login**: Handles user authentication.
  ```python
  @app.route('/login', methods=['POST'])
  def login():
      data = request.get_json()
      if not all([data.get('email'), data.get('password')]):
          return jsonify({"error": "Email and password are required"}), 400
      user = User.query.filter_by(email=data['email'], password=data['password']).first()
      if not user:
          return jsonify({"error": "Invalid email or password"}), 400
      return jsonify({"message": "Login successful", "username": user.username}), 200
  ```

---
## 📥 Installation Guide

### Prerequisites
- Python 3.6+
- Git
- Basic command-line knowledge

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/saifee3/signup-login-project.git
   cd signup-login-project
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your browser and visit `http://127.0.0.1:5000/`

## 📖 Usage Instructions

### User Registration
1. Click the "Sign Up" button on the home page
2. Fill in the required fields:
   - Username (must contain at least one number)
   - Email
   - Password (must be at least 8 characters and contain uppercase, lowercase, number, and special character)
3. Click "Sign Up" to create your account

### User Login
1. Click the "Log In" button on the home page
2. Enter your registered email and password
3. Click "Log In" to access your account

## 📁 Folder Structure

```
signup-login-project/
│
├── app.py              # Main application file
├── models.py           # Database models
├── routes.py           # Route definitions
│
├── templates/          # HTML templates
│   ├── index.html      # Home page
│   ├── login.html      # Login page
│   └── signup.html     # Signup page
│
├── static/             # Static files
│   ├── css/            # CSS styles
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
│
├── requirements.txt    # Project dependencies
├── README.md           # This documentation file
└── LICENSE             # Project license
```

## 📲 API Endpoints

| Method | Endpoint         | Description               |
|--------|------------------|---------------------------|
| GET    | `/`              | Home page                 |
| POST   | `/signup`        | User registration         |
| POST   | `/login`         | User authentication       |

## 🛠️ Future Enhancements
1. Google OAuth Integration: Add Google Sign-In functionality.
2. Password Hashing: Implement bcrypt for secure password storage.
3. Email Verification: Send confirmation emails for new signups.
4. Profile Management: Allow users to update their profiles.
5. Forgot Password: Add a password reset feature.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

- **Flask Development Team** - [@pallets](https://github.com/pallets/flask)
- Python Development Community 

[![Open in GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/saifee3/covid19_eda) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/saifee3/covid19_eda/main)



