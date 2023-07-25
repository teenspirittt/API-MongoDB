from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes.task_routes import task_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(task_bp, url_prefix='/api')
    return app





app = create_app()

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API-MongoDB"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

