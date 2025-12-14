# Biz Vendor – Vendor Management System

Biz Vendor is a web-based Vendor Management System built using Django. It allows vendors and users to register, manage profiles, add menu/food items, handle franchise details, and manage business-related operations with role-based access.

---

## 🚀 Features

* Vendor & User Registration and Login
* Role-based Dashboard (Vendor/User)
* Vendor Profile Management
* Add, Update, Delete Menu/Food Items
* Franchise Details Management
* Secure Authentication
* Image Upload Support
* Responsive UI

---

## 🛠 Tech Stack Used

### Backend

* Python 3.x
* Django Framework

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Database

* SQLite (Default)

### Other Tools

* Git & GitHub
* VS Code

---

## 📂 Project Structure

```
biz_vendor/
│── vendorapp/
│── templates/
│── static/
│── media/
│── manage.py
│── db.sqlite3
│── requirements.txt
```

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/biz-vendor.git
cd biz-vendor
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Activate:**

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux / Mac:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 🔐 Login Details

* **Admin Panel:**

```
http://127.0.0.1:8000/admin/
```

* Vendor and User logins are handled through the main application interface.

---

## 📸 Media & Static Files

Ensure `MEDIA_ROOT` and `STATIC_ROOT` are properly configured in `settings.py` for image uploads.

---

## 📌 Future Enhancements

* Payment Integration
* Order Management System
* Vendor Analytics Dashboard
* Email Notifications
* REST API Integration

---

## 🤝 Contribution

Contributions are welcome. Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Logesh N**
GitHub: [https://github.com/Logesh0108](https://github.com/Logesh0108)

---

⭐ If you like this project, don’t forget to star the repository!
