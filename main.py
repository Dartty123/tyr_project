from flask import Flask ,render_template ,request ,redirect ,url_for

from app.models.base import create_db


app = Flask(__name__,static_folder="app/static",template_folder="app/templates")


if __name__ == "__main__":
    create_db()
    app.run(debug=True)