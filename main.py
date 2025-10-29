import os
import sys

# Asegúrate de que flask_app esté en el path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flask_app'))

from app import create_app  # Nota: desde flask_app/app.py importamos create_app

# Crear la app **fuera** del if para que Gunicorn la encuentre
app = create_app()

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('NODE_ENV', 'production') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
