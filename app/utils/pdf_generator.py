from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.colors import HexColor
from io import BytesIO
from datetime import datetime

def generate_resume_pdf(user, skills, projects, publications, certifications, activities):
    """Generate professional resume PDF"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#00F5FF'),
        spaceAfter=12
    )

    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#7C3AED'),
        spaceAfter=8
    )

    normal_style = styles['Normal']
    normal_style.fontSize = 10

    story = []

    # Header
    story.append(Paragraph(user.name, title_style))
    story.append(Paragraph(user.title, styles['Heading3']))
    story.append(Spacer(1, 0.1*inch))

    # Contact Info
    contact_info = []
    if user.email:
        contact_info.append(user.email)
    if user.phone:
        contact_info.append(user.phone)
    if user.location:
        contact_info.append(user.location)
    if user.linkedin:
        contact_info.append(f"LinkedIn: {user.linkedin}")
    if user.github:
        contact_info.append(f"GitHub: {user.github}")

    story.append(Paragraph(" | ".join(contact_info), normal_style))
    story.append(Spacer(1, 0.2*inch))

    # About Section
    if user.about:
        story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
        story.append(Paragraph(user.about, normal_style))
        story.append(Spacer(1, 0.15*inch))

    # Skills Section
    if skills:
        story.append(Paragraph("SKILLS", section_style))
        skill_categories = {}
        for skill in skills:
            if skill.category not in skill_categories:
                skill_categories[skill.category] = []
            skill_categories[skill.category].append(skill.name)

        for category, skill_list in skill_categories.items():
            story.append(Paragraph(f"<b>{category}:</b> {', '.join(skill_list)}", normal_style))
        story.append(Spacer(1, 0.15*inch))

    # Projects Section
    if projects:
        story.append(Paragraph("PROJECTS", section_style))
        for project in projects:
            story.append(Paragraph(f"<b>{project.title}</b>", styles['Heading4']))
            if project.technologies:
                story.append(Paragraph(f"<i>Technologies:</i> {project.technologies}", normal_style))
            story.append(Paragraph(project.description, normal_style))
            links = []
            if project.github_link:
                links.append(f"GitHub: {project.github_link}")
            if project.demo_link:
                links.append(f"Demo: {project.demo_link}")
            if links:
                story.append(Paragraph(" | ".join(links), normal_style))
            story.append(Spacer(1, 0.1*inch))

    # Publications Section
    if publications:
        story.append(Paragraph("RESEARCH & PUBLICATIONS", section_style))
        for pub in publications:
            story.append(Paragraph(f"<b>{pub.title}</b>", styles['Heading4']))
            story.append(Paragraph(f"<i>{pub.journal}</i>", normal_style))
            if pub.authors:
                story.append(Paragraph(f"Authors: {pub.authors}", normal_style))
            if pub.publication_date:
                story.append(Paragraph(f"Published: {pub.publication_date.strftime('%B %Y')}", normal_style))
            if pub.link:
                story.append(Paragraph(f"Link: {pub.link}", normal_style))
            story.append(Spacer(1, 0.1*inch))

    # Certifications Section
    if certifications:
        story.append(Paragraph("CERTIFICATIONS", section_style))
        for cert in certifications:
            story.append(Paragraph(f"<b>{cert.title}</b>", styles['Heading4']))
            story.append(Paragraph(f"Issued by: {cert.issuer}", normal_style))
            if cert.issue_date:
                date_str = f"Issued: {cert.issue_date.strftime('%B %Y')}"
                if cert.expiry_date:
                    date_str += f" | Expires: {cert.expiry_date.strftime('%B %Y')}"
                story.append(Paragraph(date_str, normal_style))
            if cert.credential_id:
                story.append(Paragraph(f"Credential ID: {cert.credential_id}", normal_style))
            story.append(Spacer(1, 0.1*inch))

    # Leadership Activities Section
    if activities:
        story.append(Paragraph("LEADERSHIP & ACTIVITIES", section_style))
        for activity in activities:
            story.append(Paragraph(f"<b>{activity.title}</b>", styles['Heading4']))
            story.append(Paragraph(f"<i>{activity.organization}</i>", normal_style))
            if activity.role:
                story.append(Paragraph(f"Role: {activity.role}", normal_style))
            date_str = f"{activity.start_date.strftime('%B %Y')}"
            if activity.end_date:
                date_str += f" - {activity.end_date.strftime('%B %Y')}"
            elif activity.current:
                date_str += " - Present"
            story.append(Paragraph(date_str, normal_style))
            if activity.description:
                story.append(Paragraph(activity.description, normal_style))
            story.append(Spacer(1, 0.1*inch))

    # Education (placeholder - can be made dynamic later)
    story.append(Paragraph("EDUCATION", section_style))
    story.append(Paragraph("<b>Bachelor of Science in Computer Science & Engineering</b>", styles['Heading4']))
    story.append(Paragraph("Dhaka University of Engineering & Technology (DUET)", normal_style))
    story.append(Paragraph("Expected Graduation: 2025", normal_style))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()