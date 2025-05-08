# portfolio/static_data.py
# This file will hold the content for your portfolio when not using a database.

# Note: For image_path, use paths relative to your app's static directory,
# e.g., 'portfolio/images/project_image.jpg' which becomes {% static 'portfolio/images/project_image.jpg' %} in templates.
# Or use full external URLs if images are hosted elsewhere.

SKILLS = [
    {'id': 1, 'name': 'Python', 'is_featured': True, 'description': 'Advanced proficiency in Python for web development, data science, and scripting.'},
    {'id': 2, 'name': 'Django', 'is_featured': True, 'description': 'Building robust web applications with the Django framework.'},
    {'id': 3, 'name': 'JavaScript', 'is_featured': True, 'description': 'Front-end development and interactivity.'},
    {'id': 4, 'name': 'AI/Machine Learning', 'is_featured': True, 'description': 'Developing and implementing ML models.'},
    {'id': 5, 'name': 'TensorFlow / Keras', 'is_featured': False, 'description': 'Deep learning frameworks.'},
    {'id': 6, 'name': 'PyTorch', 'is_featured': False, 'description': 'Deep learning framework.'},
    {'id': 7, 'name': 'Hugging Face Transformers', 'is_featured': False, 'description': 'NLP models and tools.'},
    {'id': 8, 'name': 'Scikit-learn', 'is_featured': False, 'description': 'Classical machine learning algorithms.'},
    {'id': 9, 'name': 'Pandas & NumPy', 'is_featured': False, 'description': 'Data manipulation and analysis.'},
    {'id': 10, 'name': 'SQL / NoSQL', 'is_featured': False, 'description': 'Database management and querying.'},
    {'id': 11, 'name': 'Git / Docker', 'is_featured': False, 'description': 'Version control and containerization.'},
    {'id': 12, 'name': 'Cloud (AWS, GCP)', 'is_featured': False, 'description': 'Cloud computing platforms.'},
    {'id': 13, 'name': 'HTML & CSS', 'is_featured': True, 'description': 'Structuring and styling web pages.'},
    {'id': 14, 'name': 'Tailwind CSS', 'is_featured': True, 'description': 'Utility-first CSS framework.'},
]

TOPICS = [
    {'id': 1, 'name': 'Web Development', 'slug': 'web-development', 'is_featured': True, 'description': 'Projects related to building websites and web applications.'},
    {'id': 2, 'name': 'Machine Learning', 'slug': 'machine-learning', 'is_featured': True, 'description': 'Applications of AI and machine learning techniques.'},
    {'id': 3, 'name': 'Data Science', 'slug': 'data-science', 'is_featured': True, 'description': 'Analyzing and interpreting complex data.'},
    {'id': 4, 'name': 'Computer Vision', 'slug': 'computer-vision', 'is_featured': False, 'description': 'Projects involving image analysis and understanding.'},
    {'id': 5, 'name': 'NLP', 'slug': 'nlp', 'is_featured': False, 'description': 'Natural Language Processing projects.'},
]

PROJECTS = [
    {
        'id': 1,
        'slug': 'portfolio-website-django', # Used for URL generation
        'title': 'Personal Portfolio (This Site)',
        'description': 'A dynamic portfolio website built with Django and Tailwind CSS to showcase my projects, skills, and thoughts. Features a responsive design and dark mode.',
        'image_path': 'portfolio/images/project_portfolio.jpg', # Example path
        'github_url': 'https://github.com/JPStone2022/my-django-portfolio', # Replace with your actual repo
        'demo_url': None, # Link to this site itself if deployed
        'paper_url': None,
        'date_created': '2024-05-01', # YYYY-MM-DD format
        'skills': ['Django', 'Python', 'HTML & CSS', 'Tailwind CSS', 'JavaScript'],
        'topics': ['Web Development'],
        'is_featured': True,
        'long_description': """This portfolio website itself is a key project, designed to demonstrate my web development capabilities using Python, Django, and modern front-end technologies like Tailwind CSS.
        Key features include:
        - Dynamic project, skill, and topic display (though hardcoded in this Heroku demo version).
        - Responsive design for optimal viewing on all devices.
        - Dark mode theme toggle.
        - Clear navigation and information architecture.
        The goal was to create a clean, professional, and easily maintainable platform to share my work.
        """
    },
    {
        'id': 2,
        'slug': 'ml-sentiment-analyzer',
        'title': 'Sentiment Analyzer App',
        'description': 'A web application that analyzes the sentiment of user-provided text using a pre-trained NLP model. Built with Flask and deployed as a microservice.',
        'image_path': 'portfolio/images/project_sentiment.jpg', # Example path
        'github_url': 'https://github.com/yourusername/sentiment-analyzer', # Replace
        'demo_url': 'https://your-sentiment-demo.example.com', # Replace
        'paper_url': None,
        'date_created': '2023-11-10',
        'skills': ['Python', 'Flask', 'NLP', 'Hugging Face Transformers', 'Docker'],
        'topics': ['Machine Learning', 'NLP', 'Web Development'],
        'is_featured': True,
        'long_description': """This project involved building a simple web interface where users can input text, which is then processed by a sentiment analysis model (e.g., from Hugging Face Transformers).
        The backend was developed using Flask, and the application was containerized with Docker for easy deployment.
        It demonstrates skills in integrating ML models into web applications and basic microservice architecture.
        """
    },
    {
        'id': 3,
        'slug': 'image-classifier-cnn',
        'title': 'CNN Image Classifier',
        'description': 'Developed a Convolutional Neural Network (CNN) to classify images from the CIFAR-10 dataset. Achieved X% accuracy using TensorFlow/Keras.',
        'image_path': 'portfolio/images/project_cnn.jpg', # Example path
        'github_url': 'https://github.com/yourusername/cnn-image-classifier', # Replace
        'demo_url': None,
        'paper_url': None,
        'date_created': '2023-08-20',
        'skills': ['Python', 'TensorFlow / Keras', 'Computer Vision', 'NumPy'],
        'topics': ['Machine Learning', 'Computer Vision'],
        'is_featured': True,
        'long_description': """This was a deep learning project focused on image classification. I implemented a Convolutional Neural Network from scratch (and also experimented with transfer learning) using TensorFlow and Keras.
        The model was trained on the CIFAR-10 dataset. The project involved data preprocessing, model architecture design, training, evaluation, and hyperparameter tuning.
        It showcases my understanding of CNNs and the deep learning workflow.
        """
    },
    # Add more projects here
]

CERTIFICATES = [
    {
        'id': 1,
        'title': 'Machine Learning Specialization',
        'issuer': 'Coursera / Stanford University',
        'date_issued': '2023-05-15', # YYYY-MM-DD
        'certificate_url_or_file': 'https://www.coursera.org/account/accomplishments/specialization/certificate/XYZ123ABC', # Replace
        'is_featured': True,
        'description': 'Comprehensive specialization covering supervised learning, unsupervised learning, and best practices in ML.'
    },
    {
        'id': 2,
        'title': 'Deep Learning Specialization',
        'issuer': 'Coursera / deeplearning.ai',
        'date_issued': '2023-09-20',
        'certificate_url_or_file': 'https://www.coursera.org/account/accomplishments/specialization/certificate/DEF456GHI', # Replace
        'is_featured': True,
        'description': 'In-depth courses on neural networks, CNNs, RNNs, and structuring ML projects.'
    },
    # Add more certificates
]

DEMOS = [
    {
        'id': 1,
        'slug': 'interactive-data-viz',
        'title': 'Interactive Data Visualization',
        'description': 'A web-based interactive dashboard showcasing D3.js for data visualization. (Conceptual for this version)',
        'image_path': 'portfolio/images/demo_dataviz.jpg', # Example path
        'demo_live_url': '#', # Link to a static HTML page or a simple JS app if you build one
        'is_featured': True,
        'related_project_slug': None # Optionally link to a project slug
    },
    # Add more demos
]

RECOMMENDATIONS = [
    {
        'id': 1,
        'name': '"Deep Learning" by Goodfellow, Bengio, Courville',
        'category': 'Book',
        'description': 'The foundational textbook for deep learning. Comprehensive and mathematically rigorous.',
        'product_url': 'https://www.deeplearningbook.org/',
        'image_path': 'portfolio/images/rec_deeplearningbook.jpg', # Example path
        'is_featured': True,
    },
    {
        'id': 2,
        'name': 'fast.ai Courses',
        'category': 'Course',
        'description': 'Practical, code-first approach to learning deep learning with PyTorch.',
        'product_url': 'https://www.fast.ai/',
        'image_path': 'portfolio/images/rec_fastai.jpg', # Example path
        'is_featured': True,
    }
    # Add more recommendations
]

# Helper function to get image path for templates
def get_image_display_path(item, placeholder_text="Image"):
    if item.get('image_path'):
        return item['image_path'] # This will be used with {% static %} tag
    # Fallback placeholder - adjust dimensions as needed
    width = item.get('placeholder_width', 600)
    height = item.get('placeholder_height', 400)
    return f'https://placehold.co/{width}x{height}/E0E0E0/BDBDBD?text={placeholder_text.replace(" ", "+")}&font=inter'

