from config.app import app

from routes.login import login_blueprint
from routes.grabber import grabber_blueprint


app.register_blueprint(login_blueprint)
app.register_blueprint(grabber_blueprint)


with app.app_context():
    app.run(debug=True)