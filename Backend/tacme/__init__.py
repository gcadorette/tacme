from flask import Flask

def create_app(is_prod: bool):
    app = Flask(__name__)
    from tacme.controller.memes import memes
    app.register_blueprint(memes)
    from tacme.controller.users import users
    app.register_blueprint(users)
    
    if is_prod:
        from tacme.config import ConfigProd
        app.config.from_object(ConfigProd)
    else:
        from tacme.config import ConfigLocale
        app.config.from_object(ConfigLocale)
    return app