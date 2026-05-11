# AI/ML Engineer Portfolio - Golam Mostafa Rabby

A modern, production-ready portfolio website for Golam Mostafa Rabby, showcasing his expertise in Machine Learning, AI, Computer Vision, and IoT systems.

## 🚀 Features

- **Modern Design**: Dark futuristic AI/ML theme with glassmorphism effects
- **Responsive**: Mobile-first design that works on all devices
- **Dynamic Resume**: Auto-generated PDF resume from database content
- **Admin Dashboard**: Secure admin panel for content management
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Fast Loading**: Optimized assets and efficient code

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: Tailwind CSS, Jinja2 Templates
- **Database**: SQLite (production-ready for PostgreSQL/MySQL)
- **PDF Generation**: ReportLab
- **Authentication**: Flask-Login with password hashing
- **File Uploads**: Secure image upload handling

## 📁 Project Structure

```
portfolio/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── uploads/
│   ├── templates/
│   │   ├── admin/
│   │   └── *.html
│   ├── models/
│   ├── routes/
│   ├── forms/
│   ├── utils/
│   ├── __init__.py
│   └── config.py
├── migrations/
├── requirements.txt
├── run.py
├── seed.py
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Seed database with sample data**
   ```bash
   python seed.py
   ```

7. **Run the application**
   ```bash
   python run.py
   ```

8. **Access the application**
   - Portfolio: http://localhost:5000
   - Admin: http://localhost:5000/auth/login (admin/admin123)

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///portfolio.db
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### Database Configuration

The application uses SQLite by default. For production:

- **PostgreSQL**: `postgresql://user:password@localhost/portfolio`
- **MySQL**: `mysql://user:password@localhost/portfolio`

## 📊 Admin Features

### Login Credentials
- **Username**: admin
- **Password**: admin123

### Admin Capabilities
- ✅ Manage profile information
- ✅ Add/Edit/Delete projects
- ✅ Add/Edit/Delete skills
- ✅ Add/Edit/Delete publications
- ✅ Upload project images
- ✅ View contact messages
- ✅ Update certifications
- ✅ Manage leadership activities

## 🌐 Deployment

### Render Deployment

1. **Create Render account** and connect your GitHub repository

2. **Create Web Service**:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python run.py`

3. **Environment Variables**:
   - Add all variables from `.env`
   - Set `DATABASE_URL` to Render PostgreSQL URL

4. **Deploy**

### Railway Deployment

1. **Create Railway account** and connect repository

2. **Add PostgreSQL database**

3. **Set environment variables**

4. **Deploy automatically**

### Local Production

```bash
export FLASK_ENV=production
python run.py
```

## 📄 Dynamic Resume Generation

The portfolio automatically generates professional PDF resumes using ReportLab:

- **Dynamic Content**: All data comes from the database
- **Professional Layout**: Clean, ATS-friendly design
- **Auto-Update**: Resume updates when portfolio content changes
- **Download**: One-click PDF download for recruiters

## 🎨 Customization

### Colors
- Primary: `#00F5FF` (Cyan)
- Secondary: `#7C3AED` (Purple)
- Accent: `#00FFA3` (Green)
- Background: `#050816` (Dark)

### Fonts
- Primary: System fonts with JetBrains Mono for code

### Styling
- Tailwind CSS for responsive design
- Custom CSS for animations and effects

## 🔒 Security Features

- CSRF protection
- Password hashing
- Secure file uploads
- Input validation
- SQL injection prevention

## 📱 Mobile Responsiveness

- Mobile-first design approach
- Touch-friendly interactions
- Optimized for all screen sizes
- Fast loading on mobile networks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support or questions:
- Email: golam.mostafa.rabby@example.com
- LinkedIn: https://linkedin.com/in/golammostrabby
- GitHub: https://github.com/golammostrabby

---

**Built with ❤️ by Golam Mostafa Rabby**