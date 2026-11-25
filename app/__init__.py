from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import root_bp
    app.register_blueprint(root_bp)
    app.config.from_object("config.Config")
    return app