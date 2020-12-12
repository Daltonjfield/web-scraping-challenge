from flask import Flask, render_template, redirect
import mission_to_mars
from pymongo import MongoClient


mongo = MongoClient("mongodb://localhost:27017/mars")

app = Flask(__name__)

@app.route("/")
def home():
    mars_collection = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars=mars_collection)

@app.route("/scrape")
def scrape():
    mars_scrape = mission_to_mars.scrape()
    mongo.db.mars_collection.update({}, mars_scrape, upsert=True)
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)