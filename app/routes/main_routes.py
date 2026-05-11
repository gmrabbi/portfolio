from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file
from app import db
from app.models.user import User
from app.models.project import Project
from app.models.skill import Skill
from app.models.publication import Publication
from app.models.certification import Certification
from app.models.leadership_activity import LeadershipActivity
from app.models.contact_message import ContactMessage
from app.forms.contact_form import ContactForm
from app.utils.pdf_generator import generate_resume_pdf
import io

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home page with hero section"""
    user = User.query.first()
    skills = Skill.query.all()
    projects = Project.query.filter_by(featured=True).all()
    return render_template('index.html', user=user, skills=skills, projects=projects, title='Home')

@main.route('/about')
def about():
    """About page"""
    user = User.query.first()
    return render_template('about.html', user=user, title='About')

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
    skills = Skill.query.all()
    projects = Project.query.all()
    publications = Publication.query.all()
    certifications = Certification.query.all()
    activities = LeadershipActivity.query.all()

    # Generate PDF
    pdf_buffer = generate_resume_pdf(user, skills, projects, publications, certifications, activities)

    return send_file(
        io.BytesIO(pdf_buffer),
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f"{user.name.replace(' ', '_')}_Resume.pdf"
    )