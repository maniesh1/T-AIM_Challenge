from flask import Flask
import os
from flask_restful import Api

from application.config import LocalDevelopmentConfig
app = None
api = None

def create_app():
    app = Flask(__name__)
    if os.getenv('ENV',"development") == "production":
        raise Exception("Currently no production config is set up.")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)

    api = Api(app)
    app.app_context().push()
    return app, api



app, api = create_app()

@app.route("/")
def hello():
    return "Hello!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)