from flask import Flask ,render_template ,request ,redirect ,url_for
from app.routers.tyrs import tyr_route 
from app.models.base import create_db


app = Flask(__name__,static_folder="app/static",template_folder="app/templates")
app.register_blueprint(tyr_route)

if __name__ == "__main__":
    create_db()
    app.run(debug=True)