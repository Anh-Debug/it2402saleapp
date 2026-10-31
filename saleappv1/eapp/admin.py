from eapp import app
from flask_admin import Admin
from eapp.models import Category,Product

admin = Admin(app=app, name="E-commerce'Admin")

