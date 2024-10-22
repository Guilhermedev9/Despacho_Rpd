from flask import Flask # type: ignore
from routes.home_main import home_route

app = Flask(__name__)
app.register_blueprint(home_route)
app.run(debug=True)