"""
This module handle the different URLs that the application supports using view
functions.
"""

from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, social.co!'
