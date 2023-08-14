from gunicorn.app.base import Application
from prod_ready_api import create_app
import os


if __name__ == "__main__":
    app = create_app()

    class GunicornApp(Application):
        def init(self, parser, opts, args):
            pass

        def load(self):
            return app

    bind = "0.0.0.0:8100"
    workers = 2
    threads = 2
    worker_class = "gthread"
    timeout = 30
    keepalive = 2
    os.system(
        f"gunicorn -c prod_ready_api/gunicorn_config.py prod_ready_api:app -b {bind}"
    )
