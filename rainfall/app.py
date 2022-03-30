import logging
from typing import Optional

from flask import Blueprint, Flask

from rainfall.config_loader import ConfigLoader

routes = Blueprint("root", __name__)


@routes.route("/health")
def health():
    return ("", 200)


def get_app(config: Optional[str] = None):
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Rainfall Service started")

    if config is not None:
        app.logger.info("Loading config from %s", config)
        app.config.from_file(config, load=ConfigLoader.load, silent=False)

    app.register_blueprint(routes)

    return app
