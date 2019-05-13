from flask import Flask
from .config import Config
from .routes import init_routes

# for local:
# from config import Config
# from routes import init_routes


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    init_routes(app)
    return app


app = create_app()


if __name__ == '__main__':

    app.run(host='0.0.0.0')