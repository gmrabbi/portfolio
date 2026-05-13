from app import create_app, db
from app.config import DevelopmentConfig
from app.models.user import User
from app.models.skill import Skill
from app.models.education import Education
from app.models.training import Training
from app.models.certification import Certification
from app.models.project import Project
from app.models.leadership_activity import LeadershipActivity

app = create_app(DevelopmentConfig)
with app.app_context():
    user = User.query.first()
    print(f'✓ User: {user.name}')
    print(f'  Email: {user.email}')
    print(f'  Phone: {user.phone}')
    print()
    print(f'✓ Skills: {Skill.query.count()} total')
    print(f'✓ Education: {Education.query.count()} entries')
    print(f'✓ Training: {Training.query.count()} courses')
    print(f'✓ Certifications: {Certification.query.count()} certifications')
    print(f'✓ Projects: {Project.query.count()} projects')
    print(f'✓ Leadership: {LeadershipActivity.query.count()} activities')
    print()
    edu = Education.query.order_by(Education.order).first()
    if edu:
        print(f'First Education: {edu.degree}')
        print(f'Institution: {edu.institution}')
        print(f'CGPA: {edu.cgpa}/{edu.cgpa_scale}')
