from flask import Flask

def create_app():
    app = Flask(__name__)
    from tacme.controller.memes import memes
    app.register_blueprint(memes)
    
    return app