# The routes module handle the different URLs that the application supports.
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'
