from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file
from app import db
from app.models.user import User
from app.models.project import Project
from app.models.skill import Skill
from app.models.publication import Publication
from app.models.certification import Certification
from app.models.leadership_activity import LeadershipActivity
from app.models.education import Education
from app.models.training import Training
from app.models.contact_message import ContactMessage
from app.forms.contact_form import ContactForm
from app.utils.pdf_generator import generate_resume_pdf
import io

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home page with hero section"""
    try:
        user = User.query.first()
        skills = Skill.query.all()
        projects = Project.query.filter_by(featured=True).order_by(Project.created_at.desc()).all()
        publications = Publication.query.order_by(Publication.publication_date.desc()).limit(3).all()
        
        # Get stats
        total_projects = Project.query.count()
        total_publications = Publication.query.count()
        total_leadership = LeadershipActivity.query.count()
        years_experience = user.years_of_experience if user and user.years_of_experience is not None else 0
    except:
        # DB not ready, return basic page
        return render_template('index.html', user=None, skills=[], projects=[], publications=[], 
                             total_projects=0, total_publications=0, total_leadership=0, years_experience=0)
    
    return render_template(
        'index.html',
        user=user,
        skills=skills,
        projects=projects,
        publications=publications,
        total_projects=total_projects,
        total_publications=total_publications,
        total_leadership=total_leadership,
        years_experience=years_experience,
        title='Home'
    )

@main.route('/about')
def about():
    """About page"""
    user = User.query.first()
    leadership_activities = LeadershipActivity.query.order_by(LeadershipActivity.start_date.desc()).all()
    education_entries = Education.query.order_by(Education.order).all()
    return render_template('about.html', user=user, leadership_activities=leadership_activities, education_entries=education_entries, title='About')

@main.route('/projects')
def projects():
    """Projects page"""
    projects = Project.query.all()
    return render_template('projects.html', projects=projects, title='Projects')

@main.route('/research')
def research():
    """Research & Publications page"""
    publications = Publication.query.all()
    return render_template('research.html', publications=publications, title='Research & Publications')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    form = ContactForm()
    user = User.query.first()

    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('main.contact'))

    return render_template('contact.html', form=form, user=user, title='Contact')

@main.route('/download-resume')
def download_resume():
    """Generate and download resume PDF"""
    user = User.query.first()
    if not user:
        return "Resume data not available. Please contact administrator.", 503
    
    skills = Skill.query.all()
    projects = Project.query.all()
    publications = Publication.query.all()
    certifications = Certification.query.all()
    activities = LeadershipActivity.query.all()
    education = Education.query.all()
    training = Training.query.all()

    # Generate PDF
    pdf_buffer = generate_resume_pdf(user, skills, projects, publications, certifications, activities, education, training)

    return send_file(
        io.BytesIO(pdf_buffer),
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f"{user.name.replace(' ', '_')}_Resume.pdf"
    )

@main.route('/sitemap.xml')
def sitemap():
    """Generate sitemap.xml"""
    from flask import Response
    from datetime import datetime

    base_url = request.url_root.rstrip('/')
    pages = [
        {'loc': f'{base_url}/', 'lastmod': datetime.now().strftime('%Y-%m-%d'), 'changefreq': 'weekly', 'priority': '1.0'},
        {'loc': f'{base_url}/about', 'lastmod': datetime.now().strftime('%Y-%m-%d'), 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': f'{base_url}/projects', 'lastmod': datetime.now().strftime('%Y-%m-%d'), 'changefreq': 'weekly', 'priority': '0.9'},
        {'loc': f'{base_url}/research', 'lastmod': datetime.now().strftime('%Y-%m-%d'), 'changefreq': 'weekly', 'priority': '0.8'},
        {'loc': f'{base_url}/contact', 'lastmod': datetime.now().strftime('%Y-%m-%d'), 'changefreq': 'monthly', 'priority': '0.7'},
    ]

    sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    for page in pages:
        sitemap_xml += f'''  <url>
    <loc>{page['loc']}</loc>
    <lastmod>{page['lastmod']}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>
'''
    sitemap_xml += '</urlset>'

    return Response(sitemap_xml, mimetype='application/xml')

@main.route('/robots.txt')
def robots():
    """Serve robots.txt"""
    return send_file('static/robots.txt')