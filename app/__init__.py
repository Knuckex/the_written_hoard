from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import root_bp
    app.register_blueprint(root_bp)
    return app