from flask import Flask, session, render_template, request, flash, redirect
import crud 
from model import connect_to_db, db
import yelp
app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"




@app.route("/")
def homepage():
    """Show signup-signin."""

    return render_template("signup-in.html")

@app.route("/singin", methods = ['POST'])
def singin():
    email = request.form.get("email")
   
    user = crud.find_user(email)
    if user != None:
        password = request.form.get("password")
        if password == user.password:
            return redirect("/homepage")

    flash("incorrect User or Password")
    return redirect("/")
    


@app.route("/signup", methods = ['POST'])
def singup():
    session["name"]= request.form.get("name")
    session["lname"] = request.form.get("lname")
    session["email"] = request.form.get("email")
    session["password"] = request.form.get("password")
    
    user = crud.find_user(session["email"])
    if user:
        flash("Email aready exist, please sign in")
        return redirect("/")
    user = crud.create_user(session["name"], session["lname"], session["email"], session["password"])
    db.session.add(user) 
    db.session.commit() 
    return redirect("/homepage")

@app.route("/homepage")
def homepage1():
    """Show options"""
    name = session["name"]

    return render_template("homepage.html", name=name)

@app.route("/picnic")
def picnic():
    """"route to parks to go for a picnic"""

    return render_template("picnic.html")

@app.route("/restaurant")
def restaurant():
    """"route to parks to reastaurants nearby"""

    restaurant = yelp.find_buisness("restaurant", "San Jose")
    return render_template("restaurant.html", restaurant = restaurant)


@app.route("/movies")
def movies():
    """"movies palying in the area"""

    return render_template("movie.html")


@app.route("/bars")
def bars():
    """"route to parks to bars """

    return render_template("bars.html")

@app.route("/museums")
def musseums():
    """"route to parks to museums"""

    return render_template("museums.html")

@app.route("/events")
def events():
    """"events happeining that day"""

    return render_template("events.html")

if __name__ == "__main__":
    connect_to_db(app, "date")
    app.run(debug=True, host='0.0.0.0')
    