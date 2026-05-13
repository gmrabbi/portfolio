from app.config import DevelopmentConfig
from datetime import date

def seed_database(app=None, force=False):
    if app is None:
        from app import create_app, db
        app = create_app(DevelopmentConfig)
    else:
        from app import db

    from app.models.user import User
    from app.models.skill import Skill
    from app.models.project import Project
    from app.models.publication import Publication
    from app.models.certification import Certification
    from app.models.leadership_activity import LeadershipActivity
    from app.models.education import Education
    from app.models.training import Training

    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if data already exists
        if User.query.first() and not force:
            print("Database already seeded! Use --force to reseed.")
            return

        # Clear existing data if force flag is set
        if force:
            print("Clearing existing data...")
            User.query.delete()
            Skill.query.delete()
            Project.query.delete()
            Publication.query.delete()
            Certification.query.delete()
            LeadershipActivity.query.delete()
            Education.query.delete()
            Training.query.delete()
            db.session.commit()
            print("Data cleared.")

        # Create admin user
        admin = User(
            username='admin',
            email='gmrabbi91221@gmail.com',
            name='Golam Mostafa Rabby',
            title='Machine Learning & AI Engineer (Fresher)',
            phone='+880 1753 547782',
            location='Naogaon, Rajshahi, Bangladesh',
            github='https://github.com/gmrabbi',
            linkedin='https://www.linkedin.com/in/golammostafarabby/',
            kaggle='https://www.kaggle.com/golammostafarabby',
            scholar='https://scholar.google.com/citations?user=zvpv-lwAAAAJ',
            school='Mohishbathan High School, Naogaon',
            college='Graphic Arts Institute, Dhaka',
            university='Dhaka University of Engineering & Technology (DUET), Gazipur',
            years_of_experience=0,
            about='''Computer Science and Engineering undergraduate specializing in Machine Learning, Artificial Intelligence, and IoT automation. Experienced in developing real-world ML-powered applications, including a mobile app for plant disease detection with solution recommendation. Skilled in Python, CNN/ANN modeling, data preprocessing, and deployment-oriented development. Versatile in WordPress web development, creative design, and project management for academic and club events. Passionate about applying innovative technologies to solve practical problems and contribute effectively in dynamic engineering and IT teams.'''
        )
        admin.set_password('admin123')  # Change this in production!
        db.session.add(admin)

        # Create skills
        skills_data = [
            # Programming
            ('Programming', 'Python', 95),
            ('Programming', 'C/C++', 80),
            ('Programming', 'PHP', 75),
            ('Programming', 'SQL', 85),
            
            # Machine Learning & AI
            ('Machine Learning & AI', 'Supervised Learning', 90),
            ('Machine Learning & AI', 'Unsupervised Learning', 85),
            ('Machine Learning & AI', 'Neural Networks (ANN)', 90),
            ('Machine Learning & AI', 'CNN', 90),
            ('Machine Learning & AI', 'RNN', 85),
            ('Machine Learning & AI', 'Computer Vision', 85),
            ('Machine Learning & AI', 'Image Classification', 90),
            ('Machine Learning & AI', 'Feature Engineering', 85),
            ('Machine Learning & AI', 'Transfer Learning', 80),
            ('Machine Learning & AI', 'Few-Shot Learning', 85),
            
            # Libraries & Frameworks
            ('Libraries & Frameworks', 'TensorFlow', 90),
            ('Libraries & Frameworks', 'Keras', 90),
            ('Libraries & Frameworks', 'Scikit-learn', 85),
            ('Libraries & Frameworks', 'Pandas', 90),
            ('Libraries & Frameworks', 'NumPy', 90),
            ('Libraries & Frameworks', 'Matplotlib', 85),
            ('Libraries & Frameworks', 'Plotly', 80),
            ('Libraries & Frameworks', 'Django', 85),
            ('Libraries & Frameworks', 'Flask', 85),
            ('Libraries & Frameworks', 'Tkinter', 75),
            ('Libraries & Frameworks', 'Android Studio', 75),
            
            # Data Science
            ('Data Science', 'Data Cleaning & Preprocessing', 90),
            ('Data Science', 'Exploratory Data Analysis', 85),
            ('Data Science', 'Data Visualization', 85),
            
            # IoT & Embedded Systems
            ('IoT & Embedded Systems', 'Arduino', 85),
            ('IoT & Embedded Systems', 'ESP32', 85),
            ('IoT & Embedded Systems', 'ESP8266', 85),
            ('IoT & Embedded Systems', 'Sensors', 80),
            ('IoT & Embedded Systems', 'Motors & Relay Control', 80),
            ('IoT & Embedded Systems', 'Bluetooth', 85),
            ('IoT & Embedded Systems', 'WiFi Communication', 85),
            
            # Web & Design
            ('Web & Design', 'WordPress', 85),
            ('Web & Design', 'HTML', 90),
            ('Web & Design', 'CSS', 90),
            ('Web & Design', 'JavaScript', 80),
            ('Web & Design', 'Banner & Poster Design', 80),
            ('Web & Design', 'Social Media Design', 80),
            
            # Tools & Systems
            ('Tools & Systems', 'Git', 90),
            ('Tools & Systems', 'GitHub', 90),
            ('Tools & Systems', 'Jupyter Notebook', 90),
            ('Tools & Systems', 'Google Colab', 90),
            ('Tools & Systems', 'LaTeX', 85),
            ('Tools & Systems', 'Windows', 90),
            ('Tools & Systems', 'Linux', 85),
            ('Tools & Systems', 'SSH', 80),
            ('Tools & Systems', 'Telnet', 75),
        ]

        for category, name, proficiency in skills_data:
            skill = Skill(category=category, name=name, proficiency=proficiency)
            db.session.add(skill)

        # Create projects
        projects_data = [
            {
                'title': 'An Efficient GPS-Based Path Planning Method for Autonomous Tractor Navigation',
                'description': 'Developed and analyzed Spiral and S-shaped path planning strategies for efficient autonomous field coverage. Implemented GPS-based coordinate acquisition and real-time navigation using ESP32 and NEO-6M module. Designed mathematical models to evaluate path length, overlap distance, and cultivation time. Achieved optimized performance with Spiral pattern, reducing overlap and improving operational efficiency.',
                'technologies': 'Python, GPS, ESP32, NEO-6M, Path Planning, Mathematics',
                'github_link': '',
                'demo_link': 'https://scholar.google.com/citations?user=zvpv-lwAAAAJ',
                'featured': True
            },
            {
                'title': 'ML-Based Mobile App for Leaf Disease Detection & Solution Recommendation',
                'description': 'Developed a mobile application integrated with a CNN-based model for real-time leaf disease classification. Implemented image preprocessing, prediction pipeline, and automated solution suggestions. Focused on practical agricultural deployment for crop health monitoring.',
                'technologies': 'Python, TensorFlow, Keras, CNN, Android Studio, Image Processing',
                'github_link': 'https://github.com/gmrabbi',
                'demo_link': '',
                'featured': True
            },
            {
                'title': 'Real-Time Plant Disease Classification Using Few-Shot Learning',
                'description': 'Designed an ML system to detect crop diseases using few-shot learning techniques. Optimized performance with limited labeled data. Integrated deployment feasibility for mobile platforms. Currently under review for publication.',
                'technologies': 'Python, TensorFlow, Few-Shot Learning, Computer Vision, Mobile Deployment',
                'github_link': 'https://github.com/gmrabbi',
                'demo_link': '',
                'featured': True
            },
            {
                'title': 'Neural Network Model Development (ANN & CNN)',
                'description': 'Built and trained ANN and CNN models for classification tasks. Applied normalization, StandardScaler, and hyperparameter tuning. Evaluated models using validation metrics and achieved optimal performance.',
                'technologies': 'Python, TensorFlow, Keras, Scikit-learn, NumPy, Pandas',
                'github_link': 'https://github.com/gmrabbi',
                'demo_link': '',
                'featured': False
            },
            {
                'title': 'Portable IoT-Based Smart Juice Maker',
                'description': 'Designed an ESP8266-based automated juice preparation system. Integrated motors, relays, Bluetooth, and IoT connectivity for remote control. Conducted technical and business feasibility analysis. Currently under review.',
                'technologies': 'ESP8266, Arduino, Bluetooth, IoT, Circuit Design, Motors, Relays',
                'github_link': 'https://github.com/gmrabbi',
                'demo_link': '',
                'featured': False
            }
        ]

        for project_data in projects_data:
            project = Project(**project_data)
            db.session.add(project)

        # Create publications
        publications_data = [
            {
                'title': 'An Efficient GPS-Based Path Planning Method for Autonomous Tractor Navigation',
                'journal': 'Published Research',
                'authors': 'Golam Mostafa Rabby',
                'link': 'https://scholar.google.com/citations?user=zvpv-lwAAAAJ',
                'status': 'Published',
                'publication_date': date(2024, 1, 1)
            },
            # Add more publications as they are completed
        ]

        for pub_data in publications_data:
            publication = Publication(**pub_data)
            db.session.add(publication)

        # Create certifications
        certifications_data = [
            {
                'title': 'Digital Security Essentials',
                'issuer': 'Digital Security Agency',
                'issue_date': date(2023, 1, 1),
                'expiry_date': None,
                'credential_id': '',
                'credential_url': ''
            },
            {
                'title': 'Problem Solving (Basic)',
                'issuer': 'HackerRank',
                'issue_date': date(2023, 6, 1),
                'expiry_date': None,
                'credential_id': '',
                'credential_url': 'https://www.hackerrank.com'
            },
            {
                'title': 'Complete Python Course',
                'issuer': 'Kaggle',
                'issue_date': date(2023, 9, 1),
                'expiry_date': None,
                'credential_id': '',
                'credential_url': 'https://www.kaggle.com'
            },
            {
                'title': 'Certificate in Python (Data Analysis)',
                'issuer': 'EDGE Project, Bangladesh Computer Council (ICT Division)',
                'issue_date': date(2023, 1, 1),
                'expiry_date': None,
                'credential_id': '',
                'credential_url': ''
            },
        ]

        for cert_data in certifications_data:
            certification = Certification(**cert_data)
            db.session.add(certification)

        # Create leadership activities
        activities_data = [
            {
                'title': 'General Secretary & Senior Vice President',
                'organization': 'Math Club, DUET',
                'role': 'General Secretary & Senior Vice President',
                'description': 'Led organizational activities, coordinated academic events and competitions, and contributed to increasing student engagement and participation.',
                'start_date': date(2023, 1, 1),
                'end_date': date(2025, 12, 31),
                'current': True
            },
            {
                'title': 'Vice President',
                'organization': 'RANGDHANU',
                'role': 'Vice President',
                'description': 'Organized cultural and extracurricular programs, managing event planning, team coordination, and execution.',
                'start_date': date(2023, 1, 1),
                'end_date': date(2025, 12, 31),
                'current': True
            },
            {
                'title': 'Member',
                'organization': 'DUET Computer Society',
                'role': 'Member',
                'description': 'Participated in technical events, workshops, and collaborative activities focused on programming and innovation.',
                'start_date': date(2022, 6, 1),
                'end_date': None,
                'current': True
            },
            {
                'title': 'Volunteer',
                'organization': 'IUPC 2025 (May 9–10, 2025)',
                'role': 'Technical Volunteer',
                'description': 'Assisted in organizing inter-university programming contest operations, including participant coordination and event logistics.',
                'start_date': date(2025, 5, 9),
                'end_date': date(2025, 5, 10),
                'current': False
            },
            {
                'title': 'Volunteer',
                'organization': 'NCIM 2nd International Conference (June 27–28, 2025)',
                'role': 'Conference Volunteer',
                'description': 'Supported international conference management, including guest handling, session coordination, and technical arrangements.',
                'start_date': date(2025, 6, 27),
                'end_date': date(2025, 6, 28),
                'current': False
            },
            {
                'title': 'Volunteer',
                'organization': 'ICSHSD 2025 (October 23–24, 2025)',
                'role': 'Conference Volunteer',
                'description': 'Contributed to conference execution through logistics support, participant assistance, and session facilitation.',
                'start_date': date(2025, 10, 23),
                'end_date': date(2025, 10, 24),
                'current': False
            },
        ]

        for activity_data in activities_data:
            activity = LeadershipActivity(**activity_data)
            db.session.add(activity)

        # Create education
        education_data = [
            {
                'institution': 'Dhaka University of Engineering & Technology (DUET), Gazipur',
                'degree': 'B.Sc. in Computer Science and Engineering',
                'field_of_study': 'Computer Science and Engineering',
                'start_date': date(2022, 9, 1),
                'end_date': date(2026, 6, 30),
                'cgpa': 3.78,
                'cgpa_scale': '4.00',
                'current': True,
                'order': 1
            },
            {
                'institution': 'Graphic Arts Institute, Dhaka',
                'degree': 'Diploma in Computer Technology',
                'field_of_study': 'Computer Technology',
                'start_date': date(2020, 1, 1),
                'end_date': date(2022, 6, 30),
                'cgpa': 3.89,
                'cgpa_scale': '4.00',
                'current': False,
                'order': 2
            },
            {
                'institution': 'Mohishbathan High School, Naogaon',
                'degree': 'SSC (Science)',
                'field_of_study': 'Science',
                'start_date': date(2015, 1, 1),
                'end_date': date(2017, 6, 30),
                'cgpa': 4.82,
                'cgpa_scale': '5.00',
                'current': False,
                'order': 3
            },
        ]

        for edu_data in education_data:
            education = Education(**edu_data)
            db.session.add(education)

        # Create training & courses
        training_data = [
            {
                'title': 'Certificate in Python (Data Analysis)',
                'provider': 'EDGE Project, Bangladesh Computer Council (ICT Division)',
                'date': date(2022, 6, 1),
                'order': 1
            },
        ]

        for train_data in training_data:
            training = Training(**train_data)
            db.session.add(training)

        # Commit all changes
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    import sys
    force = '--force' in sys.argv or '-f' in sys.argv
    seed_database(force=force)