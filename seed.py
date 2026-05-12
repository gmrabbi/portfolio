from app import create_app, db
from app.models.user import User
from app.models.skill import Skill
from app.models.project import Project
from app.models.publication import Publication
from app.models.certification import Certification
from app.models.leadership_activity import LeadershipActivity
from app.config import ProductionConfig
from datetime import date

def seed_database():
    app = create_app(ProductionConfig)

    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if data already exists
        if User.query.first():
            print("Database already seeded!")
            return

        # Create admin user
        admin = User(
            username='admin',
            email='golam.mostafa.rabby@example.com',
            name='Golam Mostafa Rabby',
            title='Machine Learning & AI Engineer',
            phone='+880 1234-567890',
            location='Dhaka, Bangladesh',
            github='https://github.com/golammostrabby',
            linkedin='https://linkedin.com/in/golammostrabby',
            kaggle='https://kaggle.com/golammostrabby',
            scholar='https://scholar.google.com/citations?user=golammostrabby',
            about='''Passionate Machine Learning and AI Engineer with expertise in Computer Vision, Deep Learning, and IoT systems.
            Currently pursuing Computer Science & Engineering at Dhaka University of Engineering & Technology (DUET).
            Experienced in developing intelligent systems and conducting research in artificial intelligence.'''
        )
        admin.set_password('admin123')  # Change this in production!
        db.session.add(admin)

        # Create skills
        skills_data = [
            # Machine Learning
            ('Machine Learning', 'Python', 90),
            ('Machine Learning', 'Scikit-learn', 85),
            ('Machine Learning', 'TensorFlow', 80),
            ('Machine Learning', 'PyTorch', 75),

            # Deep Learning
            ('Deep Learning', 'Neural Networks', 85),
            ('Deep Learning', 'CNN', 80),
            ('Deep Learning', 'RNN', 75),
            ('Deep Learning', 'Transformers', 70),

            # Computer Vision
            ('Computer Vision', 'OpenCV', 85),
            ('Computer Vision', 'Image Processing', 80),
            ('Computer Vision', 'Object Detection', 75),

            # IoT
            ('IoT', 'Arduino', 80),
            ('IoT', 'Raspberry Pi', 75),
            ('IoT', 'Sensor Networks', 70),

            # Web Development
            ('Web Development', 'Flask', 85),
            ('Web Development', 'HTML/CSS', 80),
            ('Web Development', 'JavaScript', 70),

            # Research
            ('Research', 'Academic Writing', 85),
            ('Research', 'IEEE Publications', 80),

            # Tools
            ('Tools', 'Git', 90),
            ('Tools', 'Docker', 75),
            ('Tools', 'Jupyter', 85),
        ]

        for category, name, proficiency in skills_data:
            skill = Skill(category=category, name=name, proficiency=proficiency)
            db.session.add(skill)

        # Create projects
        projects_data = [
            {
                'title': 'GPS-Based Autonomous Tractor Navigation',
                'description': 'Developed an autonomous navigation system for agricultural tractors using GPS, computer vision, and machine learning algorithms. The system enables precision farming with automated path planning and obstacle avoidance.',
                'technologies': 'Python, OpenCV, GPS, Machine Learning, IoT',
                'github_link': 'https://github.com/golammostrabby/autonomous-tractor',
                'demo_link': 'https://demo.autonomous-tractor.com',
                'featured': True
            },
            {
                'title': 'Plant Disease Detection Mobile App',
                'description': 'Created a mobile application that uses deep learning to identify plant diseases from leaf images. The app helps farmers diagnose crop diseases early and take preventive measures.',
                'technologies': 'Python, TensorFlow, Flutter, Firebase, CNN',
                'github_link': 'https://github.com/golammostrabby/plant-disease-detection',
                'demo_link': 'https://play.google.com/store/apps/plant-disease',
                'featured': True
            },
            {
                'title': 'Few-Shot Learning Research',
                'description': 'Conducted research on few-shot learning techniques for image classification. Implemented and compared various meta-learning approaches including MAML and Prototypical Networks.',
                'technologies': 'PyTorch, Meta-Learning, Computer Vision, Research',
                'github_link': 'https://github.com/golammostrabby/few-shot-learning',
                'featured': True
            },
            {
                'title': 'Portable IoT Juice Maker',
                'description': 'Designed and built a portable IoT-enabled juice maker with smart inventory management and recipe recommendations using machine learning.',
                'technologies': 'Arduino, IoT, Machine Learning, Mobile App',
                'github_link': 'https://github.com/golammostrabby/iot-juice-maker',
                'featured': False
            }
        ]

        for project_data in projects_data:
            project = Project(**project_data)
            db.session.add(project)

        # Create publications
        publications_data = [
            {
                'title': 'Deep Learning Approaches for Agricultural Automation',
                'journal': 'IEEE International Conference on Robotics and Automation',
                'authors': 'Golam Mostafa Rabby, Dr. Ahmed Hossain',
                'link': 'https://ieeexplore.ieee.org/document/9876543',
                'status': 'Published',
                'publication_date': date(2024, 3, 15)
            },
            {
                'title': 'Computer Vision in Precision Farming: A Comprehensive Review',
                'journal': 'Journal of Artificial Intelligence Research',
                'authors': 'Golam Mostafa Rabby, Prof. Mohammad Rahman',
                'link': 'https://www.jair.org/index.php/jair/article/view/12345',
                'status': 'Published',
                'publication_date': date(2023, 11, 20)
            },
            {
                'title': 'IoT-Based Smart Agriculture: Challenges and Solutions',
                'journal': 'International Journal of Computer Applications',
                'authors': 'Golam Mostafa Rabby, Dr. Karim Ahmed',
                'link': 'https://www.ijcaonline.org/archives/volume180/number12/12345-6789',
                'status': 'In Review',
                'publication_date': None
            }
        ]

        for pub_data in publications_data:
            publication = Publication(**pub_data)
            db.session.add(publication)

        # Create certifications
        certifications_data = [
            {
                'title': 'TensorFlow Developer Certificate',
                'issuer': 'Google',
                'issue_date': date(2024, 1, 15),
                'expiry_date': date(2027, 1, 15),
                'credential_id': 'TF123456789',
                'credential_url': 'https://www.credential.net/tf123456789'
            },
            {
                'title': 'AWS Machine Learning Specialty',
                'issuer': 'Amazon Web Services',
                'issue_date': date(2023, 8, 10),
                'expiry_date': date(2026, 8, 10),
                'credential_id': 'AWS-ML-987654',
                'credential_url': 'https://aws.amazon.com/verification'
            }
        ]

        for cert_data in certifications_data:
            certification = Certification(**cert_data)
            db.session.add(certification)

        # Create leadership activities
        activities_data = [
            {
                'title': 'Math Club President',
                'organization': 'Dhaka University of Engineering & Technology',
                'role': 'President',
                'description': 'Led the Math Club with 200+ members, organized weekly seminars and competitive programming contests.',
                'start_date': date(2023, 1, 1),
                'end_date': date(2024, 12, 31),
                'current': True
            },
            {
                'title': 'IEEE Student Branch Volunteer',
                'organization': 'IEEE DUET Student Branch',
                'role': 'Technical Volunteer',
                'description': 'Volunteered at IEEE conferences and workshops, assisted in organizing technical events and seminars.',
                'start_date': date(2022, 6, 1),
                'end_date': date(2023, 12, 31),
                'current': False
            }
        ]

        for activity_data in activities_data:
            activity = LeadershipActivity(**activity_data)
            db.session.add(activity)

        # Commit all changes
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()