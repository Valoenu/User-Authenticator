# 🔐 Flask Authentication System

A beginner-friendly user authentication system built using **Flask**, **SQLAlchemy**, and **Flask-Login**. This project was developed as part of my learning from **The Complete 2024 Web Development Bootcamp by App Brewery on Udemy**.

## 📚 About the Project

This project includes full authentication functionality:
- ✅ User registration with hashed passwords
- ✅ Secure login system using Flask-Login
- ✅ Session-based authentication
- ✅ Protected routes and file downloads
- ✅ Flash messages for real-time feedback

I built this app to practice backend concepts such as database integration, user authentication, password hashing, and route protection.

## 🛠️ Technologies Used

- Python 3
- Flask
- Flask-Login
- SQLAlchemy ORM
- SQLite
- Werkzeug (for password hashing)
- HTML5 (Jinja Templates)
- Bootstrap (optional for styling)

## 🚀 Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🔒 User Registration   | Users can create accounts with hashed & salted passwords                    |
| 🔐 Login System        | Validates credentials and starts a secure session                           |
| 🔑 Protected Pages     | Pages like `/secrets` and `/download` are only accessible to logged-in users |
| 📄 File Download       | Authenticated users can download a file from the server                     |
| 🔁 Logout              | Ends the user session and redirects to homepage                             |
| ⚡ Flash Feedback      | Real-time alerts on login/register errors                                   |

## 📂 Folder Structure
