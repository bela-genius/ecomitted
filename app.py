"""
Main entry point for Flask application serving React build
"""
import sys
import os

# Add flask_app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flask_app'))

from flask_app.app import create_app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('NODE_ENV', 'production') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode, use_reloader=False)
