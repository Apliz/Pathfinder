# from flask import current_app as app
from flask import Flask, current_app as app, render_template, request
from databases import db

app = Flask(__name__)

# Initialises database
# This should be revised. I think it lives in a different place. Possible usecase to create __init__.py now
db.init_app(app)

# Not sure how these decorators work. Could do with some more research! RESEARCH NEEDED
@app.route("/", methods=["POST","GET"])
def home():

  # Checks if a POST request has been received from the view
  if request.method == "POST" :
    # saves the data to a variable 'data'
    data = request.data
    #inserts the data into the db
    db.insert_Data(data)

  return render_template(
    'index.html', 
    title="Aerospace Project",
    description="Project to calculate a series of transfers for space trash deorbit"
  )