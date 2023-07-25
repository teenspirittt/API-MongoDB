from flask import Flask
from flask_cors import CORS
from routes.task_routes import task_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(task_bp, url_prefix='/api')
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

