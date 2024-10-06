from flask import Flask
from routes import api  # Import the blueprint
from models import db
from flask_migrate import Migrate

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprint
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
