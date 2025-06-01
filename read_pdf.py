import PyPDF2
import pdfplumber
import os

def read_pdf_with_pypdf2(pdf_path):
    """
    Read PDF using PyPDF2
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                # Extract text and clean it
                page_text = page.extract_text()
                if page_text:
                    # Remove special characters
                    page_text = ''.join(c for c in page_text if c.isprintable() or c.isspace())
                    text += page_text + '\n'
            return text
    except Exception as e:
        print(f"Error reading PDF with PyPDF2: {e}")
        return None

def read_pdf_with_pdfplumber(pdf_path):
    """
    Read PDF using pdfplumber (more accurate for tables and layouts)
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                # Extract text using pdfplumber's more accurate method
                words = page.extract_words()
                page_text = ' '.join(word['text'] for word in words)
                if page_text:
                    # Remove special characters
                    page_text = ''.join(c for c in page_text if c.isprintable() or c.isspace())
                    text += page_text + '\n'
            return text
    except Exception as e:
        print(f"Error reading PDF with pdfplumber: {e}")
        return None

def read_pdf_with_pdfplumber(pdf_path):
    """
    Read PDF using pdfplumber (more accurate for tables and layouts)
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading PDF with pdfplumber: {e}")
        return None

def extract_key_info(text):
    """Extract key information from the PDF text"""
    info = {}
    
    # Split text into lines
    lines = text.split('\n')
    
    # Extract name from the first line
    if lines:
        name = lines[0].strip()
        if name and name != 'Contact':
            info['name'] = name
    
    # Extract contact information
    contact_info = {}
    in_contact = False
    for line in lines:
        if "Contact" in line:
            in_contact = True
            continue
        if in_contact:
            if line.strip():
                # Split by spaces and take the first word as key
                parts = line.strip().split()
                if parts:
                    key = parts[0]
                    value = ' '.join(parts[1:])
                    contact_info[key] = value
            else:
                in_contact = False
    info['contact'] = contact_info
    
    # Extract skills
    skills = []
    in_skills = False
    for line in lines:
        if "Skills" in line:
            in_skills = True
            continue
        if in_skills:
            if line.strip():
                # Split by commas to get individual skills
                skill_line = line.strip()
                skills.extend([skill.strip() for skill in skill_line.split(',') if skill.strip()])
            else:
                in_skills = False
    if skills:
        info['skills'] = skills
    
    # Extract projects
    projects = []
    in_projects = False
    for line in lines:
        if "Projects" in line:
            in_projects = True
            continue
        if in_projects:
            if line.strip():
                projects.append(line.strip())
            else:
                in_projects = False
    if projects:
        info['projects'] = projects
    
    return info

def update_website(info):
    """Update website content based on extracted information"""
    # Read current HTML content
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Update name
    if 'name' in info:
        name_pattern = r'<!-- NAME -->.*?<!-- /NAME -->'
        new_name = f'<!-- NAME -->{info["name"]}<!-- /NAME -->'
        html_content = re.sub(name_pattern, new_name, html_content)
    
    # Update skills
    if 'skills' in info and info['skills']:
        skills_section = html_content.split('<!-- Skills Content -->')[1].split('<!-- /Skills Content -->')[0]
        skill_tags = ''.join([f'<span>{skill}</span>' for skill in info['skills']])
        html_content = html_content.replace(skills_section, skill_tags)
    
    # Update projects
    if 'projects' in info and info['projects']:
        projects_section = html_content.split('<!-- Projects Content -->')[1].split('<!-- /Projects Content -->')[0]
        project_cards = ''
        for project in info['projects']:
            project_cards += f'''
            <div class="project-card">
                <h3>{project}</h3>
                <p>Description of {project}</p>
                <div class="project-links">
                    <a href="#" class="btn">View Code</a>
                    <a href="#" class="btn">Live Demo</a>
                </div>
            </div>
            '''
        html_content = html_content.replace(projects_section, project_cards)
    
    # Update contact information
    if 'contact' in info:
        contact_section = html_content.split('<div class="social-links">')[1].split('</div>')[0]
        social_links = ''
        for key, value in info['contact'].items():
            if key.lower() == 'linkedin':
                social_links += f'<a href="{value}" class="social-icon"><i class="fab fa-linkedin"></i></a>'
            elif key.lower() == 'github':
                social_links += f'<a href="{value}" class="social-icon"><i class="fab fa-github"></i></a>'
        html_content = html_content.replace(contact_section, social_links)
    
    # Write updated content back to file
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print("\nWebsite updated successfully!")

def main():
    pdf_path = "Profile.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"PDF file not found: {pdf_path}")
        return
    
    print("\nReading PDF with PyPDF2:")
    text_pypdf2 = read_pdf_with_pypdf2(pdf_path)
    if not text_pypdf2:
        text_pypdf2 = read_pdf_with_pdfplumber(pdf_path)
    
    if text_pypdf2:
        print("\nExtracted text:")
        print(text_pypdf2[:500])  # Print first 500 characters
        
        # Extract key information
        info = extract_key_info(text_pypdf2)
        print("\nExtracted Information:")
        print("Name:", info.get('name', 'Not found'))
        print("Skills:", info.get('skills', []))
        print("Projects:", info.get('projects', []))
        
        # Update website content
        update_website(info)

if __name__ == "__main__":
    main()
