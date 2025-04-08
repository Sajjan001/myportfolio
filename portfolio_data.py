"""
Portfolio data module for Sajjan Yadav's portfolio website.
This module contains all the data used in the portfolio website.
"""

def get_portfolio_data():
    """
    Returns the portfolio data.
    """
    return {
        "profile": {
            "name": "Sajjan Yadav",
            "title": "Data Science Trainer & Machine Learning Engineer",
            "email": "sajjanyadav.ml@gmail.com",
            "phone": "6263613169",
            "location": "Village pasaudh masira jaysinghna, Shahdol, MP, India",
            "objective": "I seek challenging opportunities where I can fully use my skills for the success of the organization.",
            "bio": "Data Science Trainer at JSMIES DDUGKY Bhopal since October 2024 with expertise in Python, R, and SQL. Specializing in teaching technical skills including machine learning, deep learning, and data analysis. Passionate about empowering students with data science knowledge and helping them build practical skills for real-world applications.",
            "image": "images/sajjan-profile.jpg"
        },
        "skills": [
            {"name": "Python (Pandas, NumPy, Scikit-learn)", "level": 95},
            {"name": "Machine Learning & Deep Learning", "level": 90},
            {"name": "Data Preprocessing & Visualization", "level": 92},
            {"name": "R Programming", "level": 85},
            {"name": "MySQL & SQL Server", "level": 88},
            {"name": "Advanced Excel & Power BI", "level": 85},
            {"name": "Natural Language Processing", "level": 82},
            {"name": "Django & Flask", "level": 80},
            {"name": "PyTorch & OpenCV", "level": 78},
            {"name": "PySpark & JAX", "level": 75},
            {"name": "Rust", "level": 70}
        ],
        "languages": [
            {"name": "Hindi", "level": "Native"},
            {"name": "English", "level": "Professional"}
        ],
        "experience": [
            {
                "role": "Data Science Trainer",
                "company": "JSMIES DDUGKY Bhopal",
                "period": "October 28, 2024 - Present",
                "description": "Technical training, SQL databases, Python, Machine Learning, Deep Learning, Statistical Modeling, Natural Language Processing, Data Science, Teaching"
            },
            {
                "role": "Data Analyst",
                "company": "RR Finance Consultant Pvt",
                "period": "October 28, 2023 - August 30, 2024",
                "description": "Data processing and visualization and SQL server, Power BI and creating daily basis MIS reports"
            },
            {
                "role": "Data Science Trainer (Freelance)",
                "company": "Infinity Career",
                "period": "January 1, 2023 - November 30, 2023",
                "description": "Providing training on data science concepts and tools"
            },
            {
                "role": "Machine Learning Engineer Trainee",
                "company": "Jsmies under DDUGKY project",
                "period": "October 1, 2022 - January 10, 2022",
                "description": "Training in machine learning engineering concepts and applications"
            }
        ],
        "education": [
            {
                "degree": "Bachelor of technology",
                "institution": "Rajiv Gandhi prodyogiki Viswavidyalay bhopal",
                "year": "2022",
                "score": "83%"
            },
            {
                "degree": "12th Standard",
                "institution": "Navjyoti Academy Higher Secondary School, Manpur",
                "year": "2018",
                "score": "80%"
            },
            {
                "degree": "10th Standard",
                "institution": "Navjyoti Academy Higher Secondary School, Manpur",
                "year": "2016",
                "score": "85%"
            }
        ],
        "contact": {
            "email": "sajjanyadav.ml@gmail.com",
            "phone": "6263613169",
            "location": "Village pasaudh masira jaysinghna, Shahdol, MP, India",
            "social": {
                "linkedin": "https://linkedin.com/in/sajjan-yadav",
                "github": "https://github.com/sajjan-yadav",
                "twitter": "https://twitter.com/sajjan_yadav"
            }
        },
        "projects": [
            {
                "title": "Health AI",
                "description": "Predictive analysis for healthcare diagnosis using a large amount of patient data. The system helps in early diagnosis and treatment recommendations.",
                "technologies": ["Python", "Machine Learning", "Healthcare Data"],
                "image": "images/project-ml.svg",
                "tags": ["AI", "Healthcare", "Predictive Analysis", "Big Data"],
                "link": "#"
            },
            {
                "title": "Doctor Appointment Website",
                "description": "A Django-based website for booking doctor appointments with integrated disease prediction using machine learning algorithms. Built with Python, HTML, JavaScript, and machine learning.",
                "technologies": ["Django", "Python", "HTML", "JavaScript", "Machine Learning"],
                "image": "images/project-web.svg",
                "tags": ["Django", "Machine Learning", "HTML", "JavaScript"],
                "link": "#"
            },
            {
                "title": "Time Series Analysis",
                "description": "Analysis of time series data using ARIMA and SARIMA models and applying machine learning algorithms. Also analyzed the Titanic dataset for passenger survival prediction.",
                "technologies": ["Python", "ARIMA", "SARIMA", "Machine Learning"],
                "image": "images/project-data.svg",
                "tags": ["Time Series", "ARIMA", "SARIMA", "Prediction Models"],
                "link": "#"
            },
            {
                "title": "NLP Projects",
                "description": "Text preprocessing and analysis for IMDB movie review dataset and email spam detection. Deployed the system using Flask framework.",
                "technologies": ["Python", "NLP", "Flask", "Text Preprocessing"],
                "image": "images/project-ml.svg",
                "tags": ["NLP", "Flask", "Text Processing", "Machine Learning"],
                "link": "#"
            },
            {
                "title": "Stock Market & Sales Data Analysis",
                "description": "Analyzed growth rates and KPIs from stock market and sales datasets. Performed data preprocessing and visualization to extract insights.",
                "technologies": ["Python", "Data Analysis", "Visualization"],
                "image": "images/project-data.svg",
                "tags": ["Data Analysis", "Visualization", "Preprocessing", "KPI Tracking"],
                "link": "#"
            },
            {
                "title": "Object & Currency Detection",
                "description": "Computer vision project for object detection and currency recognition using OpenCV and Django framework for deployment.",
                "technologies": ["Python", "OpenCV", "Django", "Computer Vision"],
                "image": "images/project-ml.svg",
                "tags": ["Python", "OpenCV", "Django", "Computer Vision"],
                "link": "#"
            }
        ]
    }