from app import app
from db import DB

DB.init_app(app)

@app.before_first_request
def create_db():
    DB.create_all()