from app import create_app, db
from app.models import Usuario
from flask_migrate import Migrate


app = create_app('developmentConfig')

migrate = Migrate(app, db)
