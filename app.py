import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from portfolio_data import get_portfolio_data

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Get portfolio data
portfolio_data = get_portfolio_data()

@app.route('/')
def home():
    """Render the homepage with all portfolio sections."""
    return render_template('index.html', portfolio=portfolio_data)

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject', 'No Subject')
        message = request.form.get('message')
        
        # Import the email service
        from email_service import send_contact_notification
        
        # Try to send the notification email
        try:
            send_contact_notification(name, email, subject, message)
            flash('Thank you for your message! I will get back to you soon.')
            app.logger.info(f"Contact form submission from {name} ({email})")
        except Exception as e:
            app.logger.error(f"Failed to process contact form: {str(e)}")
            flash('Sorry, there was an issue processing your request. Please try again later.')
        
        return redirect(url_for('home', _anchor='contact'))
    
    return redirect(url_for('home'))

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('index.html', portfolio=portfolio_data, error=404), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    app.logger.error(f"Server error: {e}")
    return render_template('index.html', portfolio=portfolio_data, error=500), 500
