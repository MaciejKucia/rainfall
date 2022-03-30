from os import environ

from rainfall.app import get_app

app = get_app(environ.get("CONFIG_FILE"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
