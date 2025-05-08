from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .static_data import PROJECTS, SKILLS, TOPICS, CERTIFICATES, DEMOS, RECOMMENDATIONS, get_image_display_path
from datetime import datetime

# Helper to find an item in a list of dictionaries by id or slug
def find_item(item_list, identifier, key='id'):
    try:
        identifier = int(identifier) if key == 'id' else str(identifier)
    except ValueError:
        return None # Invalid identifier format for 'id'

    for item in item_list:
        if item.get(key) == identifier:
            return item
    return None

def index_view(request):
    featured_projects = [p for p in PROJECTS if p.get('is_featured')][:3]
    featured_skills = [s for s in SKILLS if s.get('is_featured')][:10]
    featured_topics = [t for t in TOPICS if t.get('is_featured')][:10]
    featured_certificates = [c for c in CERTIFICATES if c.get('is_featured')][:3]
    featured_demos = [d for d in DEMOS if d.get('is_featured')][:3]
    featured_recommendations = [r for r in RECOMMENDATIONS if r.get('is_featured')][:3]

    # Add image paths using the helper
    for project in featured_projects:
        project['image_url_template'] = get_image_display_path(project, "Project+Image")
    for demo_item in featured_demos:
        demo_item['image_url_template'] = get_image_display_path(demo_item, "Demo+Preview")
    for rec_item in featured_recommendations:
        rec_item['image_url_template'] = get_image_display_path(rec_item, "Image")


    context = {
        'page_title': "Julian Stone - ML & AI Portfolio",
        'featured_projects': featured_projects,
        'featured_skills': featured_skills,
        'featured_topics': featured_topics,
        'featured_certificates': featured_certificates,
        'featured_demos': featured_demos,
        'featured_recommendations': featured_recommendations,
    }
    return render(request, 'portfolio/index.html', context)

def about_me_view(request):
    context = {
        'page_title': "About Julian Stone"
    }
    return render(request, 'portfolio/about_me_page.html', context)

def all_projects_view(request):
    # Add image paths using the helper
    processed_projects = []
    for project_data in PROJECTS:
        temp_project = project_data.copy() # Avoid modifying original data
        temp_project['image_url_template'] = get_image_display_path(temp_project, "Project+Image")
        processed_projects.append(temp_project)

    context = {
        'projects': processed_projects,
        'page_title': "All Projects"
    }
    return render(request, 'portfolio/all_projects.html', context)

def project_detail_view(request, project_slug_or_id):
    # Try finding by ID first, then by slug for flexibility
    project = find_item(PROJECTS, project_slug_or_id, key='id')
    if not project:
        project = find_item(PROJECTS, project_slug_or_id, key='slug')

    if not project:
        raise Http404("Project not found")

    # Prepare project data for template
    project_data = project.copy()
    project_data['image_url_template'] = get_image_display_path(project_data, "Project+Image")
    
    # Convert date string to datetime object for template formatting if needed
    try:
        project_data['date_created_obj'] = datetime.strptime(project_data.get('date_created', ''), "%Y-%m-%d")
    except ValueError:
        project_data['date_created_obj'] = None


    context = {
        'project': project_data,
        'page_title': project_data['title']
    }
    return render(request, 'portfolio/project_detail.html', context)

def skill_list_view(request):
    context = {
        'skills': sorted(SKILLS, key=lambda x: x['name']),
        'page_title': "Skills"
    }
    return render(request, 'portfolio/skill_list.html', context)

def all_demos_list_view(request):
    processed_demos = []
    for demo_data in DEMOS:
        temp_demo = demo_data.copy()
        temp_demo['image_url_template'] = get_image_display_path(temp_demo, "Demo+Preview")
        processed_demos.append(temp_demo)
    context = {
        'demos': processed_demos,
        'page_title': "All Demos"
    }
    return render(request, 'portfolio/all_demos_list.html', context)

def demo_detail_view(request, demo_slug_or_id):
    demo = find_item(DEMOS, demo_slug_or_id, key='id')
    if not demo:
        demo = find_item(DEMOS, demo_slug_or_id, key='slug')

    if not demo:
        raise Http404("Demo not found")
    
    demo_data = demo.copy()
    demo_data['image_url_template'] = get_image_display_path(demo_data, "Demo+Preview")

    context = {
        'demo': demo_data,
        'page_title': demo_data['title']
    }
    # For a simple demo, you might redirect to demo_data['demo_live_url']
    # or render a detail page like this:
    return render(request, 'portfolio/demo_detail.html', context)


def topic_list_view(request):
    context = {
        'topics': sorted(TOPICS, key=lambda x: x['name']),
        'page_title': "Topics"
    }
    return render(request, 'portfolio/topic_list.html', context)

def certificates_view(request):
    processed_certs = []
    for cert_data in CERTIFICATES:
        temp_cert = cert_data.copy()
        try:
            temp_cert['date_issued_obj'] = datetime.strptime(temp_cert.get('date_issued', ''), "%Y-%m-%d")
        except ValueError:
            temp_cert['date_issued_obj'] = None
        processed_certs.append(temp_cert)

    context = {
        'certificates': sorted(processed_certs, key=lambda x: (x.get('date_issued_obj') is None, x.get('date_issued_obj')), reverse=True),
        'page_title': "Certificates"
    }
    return render(request, 'portfolio/certificates.html', context)

def contact_view(request):
    context = {
        'page_title': "Contact Me"
    }
    return render(request, 'portfolio/contact.html', context) # You'll need a contact.html template

def search_results_view(request):
    query = request.GET.get('q', '').lower()
    project_results = []
    skill_results = []
    topic_results = []

    if query:
        project_results = [
            p for p in PROJECTS if query in p['title'].lower() or query in p['description'].lower()
        ]
        skill_results = [s for s in SKILLS if query in s['name'].lower()]
        topic_results = [t for t in TOPICS if query in t['name'].lower()]
        
        for project in project_results: # Add image path for search results
            project['image_url_template'] = get_image_display_path(project, "Project+Image")


    context = {
        'query': query,
        'project_results': project_results,
        'skill_results': skill_results,
        'topic_results': topic_results,
        'page_title': f"Search Results for '{query}'" if query else "Search"
    }
    return render(request, 'portfolio/search_results.html', context) # You'll need search_results.html

# Static Pages
def privacy_policy_view(request):
    return render(request, 'portfolio/privacy_policy.html', {'page_title': "Privacy Policy"})

def accessibility_view(request):
    return render(request, 'portfolio/accessibility.html', {'page_title': "Accessibility Statement"})

def terms_view(request):
    return render(request, 'portfolio/terms.html', {'page_title': "Terms and Conditions"})

def colophon_view(request):
    return render(request, 'portfolio/colophon.html', {'page_title': "Colophon"})

def cv_view(request):
    return render(request, 'portfolio/cv.html', {'page_title': "CV / Resume"})

def hire_me_view(request):
    return render(request, 'portfolio/hire_me.html', {'page_title': "Hire Me"})

def recommendation_list_view(request):
    processed_recs = []
    for rec_data in RECOMMENDATIONS:
        temp_rec = rec_data.copy()
        temp_rec['image_url_template'] = get_image_display_path(temp_rec, "Image")
        processed_recs.append(temp_rec)
    context = {
        'recommendations': sorted(processed_recs, key=lambda x: (x.get('category', ''), x['name'])),
        'page_title': "Recommendations"
    }
    return render(request, 'portfolio/recommendation_list.html', context)
