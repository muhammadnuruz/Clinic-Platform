# 🏥 Clinic Platform – Django-based Medical Service System

> 🌐 Multilingual Support

---

## 🔎 Project Overview

**Clinic Platform** is a real-world, production-grade medical management system built using Django. It is designed for clinics with multiple branches and currently supports **6 active locations**. The system allows administrators and users to manage medical tests, branch services, and digital communications efficiently.

### ✅ Key Features

- 🏥 Overview of 6 active clinic branches
- 💸 Comprehensive lab analysis catalog with up-to-date pricing
- 📤 User-friendly interface to submit complaints and suggestions
- 📃 Online access to laboratory results for patients
- 🧑‍⚕️ Powerful Django admin panel for full system control

---

## 🧰 Technology Stack

| Technology       | Purpose                            |
|------------------|-------------------------------------|
| Python + Django  | Backend logic and admin interface  |
| PostgreSQL       | Relational database engine         |
| HTML / CSS       | Page templates and layout          |
| Bootstrap        | Responsive frontend styling        |
| Docker (optional)| Environment containerization       |

---

## 🗂️ Project Structure

```bash
Clinic-Platform/
├── apps/
│   ├── analysis/       # Lab test models, results, and views
│   ├── branches/       # Branch locations and contact info
│   ├── complaints/     # Suggestions and complaints handling
│   └── users/          # Authentication and user roles
├── templates/          # HTML template files
├── static/             # CSS, JavaScript, image assets
└── manage.py           # Django management command entry point
```

---

## 🖥️ Admin Panel Capabilities

- Full CRUD for users, branches, and services
- Upload and view lab test results
- Manage incoming feedback (complaints/suggestions)
- Assign roles and manage access levels securely

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/muhammadnuruz/Clinic-Platform.git
cd Clinic-Platform

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create an admin user
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

---

## 📸 Screenshots

### 🧾 Admin Panel
![Admin panel screenshot](https://github.com/user-attachments/assets/65ba6278-c335-429a-94f7-16c249f42af1)

### 🧾 Sample — Store Request via Telegram
![Request screenshot](https://github.com/user-attachments/assets/0bc483c5-daa3-44c7-b704-24e463b8658b)

---

## 📈 Future Improvements

- [ ] SMS or Email notifications for ready lab results
- [ ] Role-based dashboards for patients, doctors, and branch managers
- [ ] Telegram bot integration for result delivery
- [ ] Mobile app version (React Native or Flutter)

---

## 👨‍💻 Developed By

**Muhammad Nur Suxbatullayev**  
🎓 Back-End Developer with 1+ years of hands-on experience  
🏫 Full Scholarship Recipient at PDP University  
🧠 Skilled in building scalable and secure back-end systems using:  

🔗 **GitHub:** [github.com/muhammadnuruz](https://github.com/muhammadnuruz)  
📬 **Telegram:** [@TheMuhammadNur](https://t.me/TheMuhammadNur)

---

## ⭐ Support the Project

If this project helped you, inspired you, or you simply liked it — please consider giving it a **⭐ on GitHub**.  
Your support boosts the project's visibility and motivates continued improvements and future updates.

Thank you for being part of the journey!
