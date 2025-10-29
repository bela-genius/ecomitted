"""
Main entry point for Flask application serving React build
"""
import os
from flask_app.app import create_app

# Creamos la app afuera del if para que Gunicorn la pueda encontrar
app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('NODE_ENV', 'production') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode, use_reloader=False)
