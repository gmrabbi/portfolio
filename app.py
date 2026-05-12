"""
Flask Application Entrypoint for Vercel, Render, and other deployment platforms.
"""
import os
from app import create_app
from app.config import DevelopmentConfig, ProductionConfig

config_name = os.environ.get('FLASK_CONFIG', 'ProductionConfig')
config_class = DevelopmentConfig if config_name == 'DevelopmentConfig' else ProductionConfig

app = create_app(config_class)
application = app  # For gunicorn

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=config_class.DEBUG, host='0.0.0.0', port=port)
