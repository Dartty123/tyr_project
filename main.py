from flask import Flask ,render_template ,request ,redirect ,url_for
from app.routers.tyrs import tyr_route 
from app.model.models import db
from app.model.models import Tour, Booking



app = Flask(__name__,static_folder="app/static",template_folder="app/templates")
app. config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tours.db"
app. register_blueprint(tyr_route)
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db. create_all()
    app. run (debug=True)