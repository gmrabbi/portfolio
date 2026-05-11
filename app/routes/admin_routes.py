from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models.user import User
from app.models.project import Project
from app.models.skill import Skill
from app.models.publication import Publication
from app.models.certification import Certification
from app.models.leadership_activity import LeadershipActivity
from app.models.contact_message import ContactMessage
from app.forms.profile_form import ProfileForm
from app.forms.project_form import ProjectForm
from app.forms.skill_form import SkillForm
from app.forms.publication_form import PublicationForm
from app.forms.certification_form import CertificationForm
from app.forms.leadership_form import LeadershipForm
from app.utils.image_handler import save_image
import os

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    """Admin dashboard"""
    user = User.query.first()
    projects_count = Project.query.count()
    skills_count = Skill.query.count()
    publications_count = Publication.query.count()
    messages_count = ContactMessage.query.filter_by(read=False).count()

    return render_template('admin/dashboard.html',
                         user=user,
                         projects_count=projects_count,
                         skills_count=skills_count,
                         publications_count=publications_count,
                         messages_count=messages_count,
                         title='Admin Dashboard')

# Profile Management
@admin.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Edit profile"""
    user = User.query.first()
    form = ProfileForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('admin.profile'))

    return render_template('admin/profile.html', form=form, user=user, title='Edit Profile')

# Projects Management
@admin.route('/projects')
@login_required
def projects():
    """List all projects"""
    projects = Project.query.all()
    return render_template('admin/projects.html', projects=projects, title='Manage Projects')

@admin.route('/projects/new', methods=['GET', 'POST'])
@login_required
def new_project():
    """Create new project"""
    form = ProjectForm()

    if form.validate_on_submit():
        image_filename = None
        if form.image.data:
            image_filename = save_image(form.image.data, 'projects')

        project = Project(
            title=form.title.data,
            description=form.description.data,
            technologies=form.technologies.data,
            github_link=form.github_link.data,
            demo_link=form.demo_link.data,
            image=image_filename,
            featured=form.featured.data
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('admin.projects'))

    return render_template('admin/project_form.html', form=form, title='New Project')

@admin.route('/projects/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    """Edit project"""
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        if form.image.data:
            # Delete old image if exists
            if project.image:
                old_image_path = os.path.join('app/static/uploads/projects', project.image)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

            project.image = save_image(form.image.data, 'projects')

        form.populate_obj(project)
        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin.projects'))

    return render_template('admin/project_form.html', form=form, project=project, title='Edit Project')

@admin.route('/projects/<int:id>/delete', methods=['POST'])
@login_required
def delete_project(id):
    """Delete project"""
    project = Project.query.get_or_404(id)

    # Delete image file if exists
    if project.image:
        image_path = os.path.join('app/static/uploads/projects', project.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin.projects'))

# Skills Management
@admin.route('/skills')
@login_required
def skills():
    """List all skills"""
    skills = Skill.query.all()
    return render_template('admin/skills.html', skills=skills, title='Manage Skills')

@admin.route('/skills/new', methods=['GET', 'POST'])
@login_required
def new_skill():
    """Create new skill"""
    form = SkillForm()

    if form.validate_on_submit():
        skill = Skill(
            category=form.category.data,
            name=form.name.data,
            proficiency=form.proficiency.data
        )
        db.session.add(skill)
        db.session.commit()
        flash('Skill added successfully!', 'success')
        return redirect(url_for('admin.skills'))

    return render_template('admin/skill_form.html', form=form, title='New Skill')

@admin.route('/skills/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_skill(id):
    """Edit skill"""
    skill = Skill.query.get_or_404(id)
    form = SkillForm(obj=skill)

    if form.validate_on_submit():
        form.populate_obj(skill)
        db.session.commit()
        flash('Skill updated successfully!', 'success')
        return redirect(url_for('admin.skills'))

    return render_template('admin/skill_form.html', form=form, skill=skill, title='Edit Skill')

@admin.route('/skills/<int:id>/delete', methods=['POST'])
@login_required
def delete_skill(id):
    """Delete skill"""
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill deleted successfully!', 'success')
    return redirect(url_for('admin.skills'))

# Publications Management
@admin.route('/publications')
@login_required
def publications():
    """List all publications"""
    publications = Publication.query.all()
    return render_template('admin/publications.html', publications=publications, title='Manage Publications')

@admin.route('/publications/new', methods=['GET', 'POST'])
@login_required
def new_publication():
    """Create new publication"""
    form = PublicationForm()

    if form.validate_on_submit():
        publication = Publication(
            title=form.title.data,
            journal=form.journal.data,
            authors=form.authors.data,
            link=form.link.data,
            status=form.status.data,
            publication_date=form.publication_date.data
        )
        db.session.add(publication)
        db.session.commit()
        flash('Publication added successfully!', 'success')
        return redirect(url_for('admin.publications'))

    return render_template('admin/publication_form.html', form=form, title='New Publication')

@admin.route('/publications/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_publication(id):
    """Edit publication"""
    publication = Publication.query.get_or_404(id)
    form = PublicationForm(obj=publication)

    if form.validate_on_submit():
        form.populate_obj(publication)
        db.session.commit()
        flash('Publication updated successfully!', 'success')
        return redirect(url_for('admin.publications'))

    return render_template('admin/publication_form.html', form=form, publication=publication, title='Edit Publication')

@admin.route('/publications/<int:id>/delete', methods=['POST'])
@login_required
def delete_publication(id):
    """Delete publication"""
    publication = Publication.query.get_or_404(id)
    db.session.delete(publication)
    db.session.commit()
    flash('Publication deleted successfully!', 'success')
    return redirect(url_for('admin.publications'))

# Messages Management
@admin.route('/messages')
@login_required
def messages():
    """List all contact messages"""
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('admin/messages.html', messages=messages, title='Contact Messages')

@admin.route('/messages/<int:id>')
@login_required
def view_message(id):
    """View message details"""
    message = ContactMessage.query.get_or_404(id)
    if not message.read:
        message.read = True
        db.session.commit()
    return render_template('admin/message_detail.html', message=message, title='Message Details')

@admin.route('/messages/<int:id>/delete', methods=['POST'])
@login_required
def delete_message(id):
    """Delete message"""
    message = ContactMessage.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    flash('Message deleted successfully!', 'success')
    return redirect(url_for('admin.messages'))