from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
















# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# # from datetime import datetime

# # new instance of the Flask class
# app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite'
# db = SQLAlchemy(app)


# if __name__=="__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True, port=8000)