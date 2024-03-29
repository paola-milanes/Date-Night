from flask import Flask, session, render_template, request, flash, redirect
import crud 
from PIL import Image
from model import connect_to_db, db
import fandango
import yelp
from datetime import datetime
import json

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
    session['name']= user.fname
    session['email']= email

    # session["name"] = user.name
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

@app.route("/homepage", methods = ["get"])
def homepage1():
    """Show options"""

    name = session["name"]
    location = session.get("location")
    print(location)
    return render_template("homepage.html", name=name, location=location)


@app.route("/homepage", methods = ["post"])
def homepage2():
    name = session["name"]
    session["location"]= request.form.get("location")
    # print(session["location"])
    return render_template("homepage.html", name=name)


@app.route("/picnic", methods =["POST"] )
def picnic():
    """"route to parks to go for a picnic"""
    session['list'] = {}
    session["term"] = request.form.get('term')
    # print(session["term"])
    location = session["location"]
    location_names = []
    locations = []

    parks = yelp.find_business(session["term"], location = location)
    
    if 'businesses' not in parks:
        flash('invalid City, Please try again')
        return redirect('/homepage')

    else:
        for place in parks['businesses']:
            picnic_by_id = yelp.search_by_id(place["id"])
           
            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            session['list'][place['id']]['img'] =picnic_by_id["photos"]
            session['list'][place['id']]['rvw count'] =[place][0]['review_count']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['categories'] =[place][0]['categories']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['phone'] =[place][0]['display_phone']
            session['list'][place['id']]['cordinates'] =[place][0]['coordinates']
            session['list'][place['id']]['closed'] =[place][0]['is_closed']
            session['list'][place['id']]['price'] =[place][0].get('price','Not available')
            # print(session['list'])
            locations.append([place][0]['coordinates'])
            location_names.append([place][0]['name'])
            # print(locations)

            
            lon =  -121.901284
            lat = 37.308203
    return render_template("picnic.html", parks = parks,  places = session['list'],location = session['location'],cordinates = locations, lon = lon, lat = lat, location_names = location_names)

@app.route("/bowling", methods =["POST"] )
def bowling():
    """"route to parks to go for a picnic"""
    session['list'] = {}
    session["term"] = request.form.get('term')
    # print(session["term"])
    location = session["location"]
    location_names = []
    locations = []

    bowling = yelp.find_business(session["term"], location = location)
    
    if 'businesses' not in bowling:
        flash('invalid City, Please try again')
        return redirect('/homepage')

    else:
        for place in bowling['businesses']:
            picnic_by_id = yelp.search_by_id(place["id"])
           
            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            session['list'][place['id']]['img'] =picnic_by_id["photos"]
            session['list'][place['id']]['rvw count'] =[place][0]['review_count']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['categories'] =[place][0]['categories']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['phone'] =[place][0]['display_phone']
            session['list'][place['id']]['cordinates'] =[place][0]['coordinates']
            session['list'][place['id']]['closed'] =[place][0]['is_closed']
            session['list'][place['id']]['price'] =[place][0].get('price','Not available')
            # print(session['list'])
            locations.append([place][0]['coordinates'])
            location_names.append([place][0]['name'])
            lon =  -121.901284
            lat = 37.308203
            
    return render_template("bowling.html", bowling = bowling,  places = session['list'],location = session['location'],cordinates = locations, lon = lon, lat = lat, location_names = location_names)


@app.route("/hiking", methods = ["POST"])
def hiking():
    """"route to parks to reastaurants nearby"""
    session['list'] = {}
    session["term"] = request.form.get('term')
    # print(session["term"])
    location = session["location"]
    location_names = []
    locations = []
    hiking = yelp.find_business(session["term"], location = location)
    if 'businesses' not in hiking:
        flash('invalid City, Please try again')
        return redirect('/homepage')

    else:
        for place in hiking['businesses']:
            restaurant_by_id = yelp.search_by_id(place["id"])
            # print(restaurant_by_id["photos"])


            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            # session['list'][place['id']]['img'] =[place][0]['image_url']
            session['list'][place['id']]['img'] =restaurant_by_id["photos"]
            session['list'][place['id']]['rvw count'] =[place][0]['review_count']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['categories'] =[place][0]['categories']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['phone'] =[place][0]['display_phone']
            session['list'][place['id']]['cordinates'] =[place][0]['coordinates']
            session['list'][place['id']]['closed'] =[place][0]['is_closed']
            session['list'][place['id']]['price'] =[place][0].get('price','Not available')
            # print(session['list'])
            # print(session['list'][place['id']]['img'])
            locations.append([place][0]['coordinates'])
            location_names.append([place][0]['name'])
            lon =  -121.901284
            lat = 37.308203
            # print(locations)

    return render_template("hiking.html", places = session['list'],location = session['location'], cordinates = locations,lon = lon, lat= lat, location_names = location_names)

@app.route("/restaurant", methods = ["POST"])
def restaurant():
    """"route to parks to reastaurants nearby"""
    session['list'] = {}
    session["term"] = request.form.get('term')
    # print(session["term"])
    location = session["location"]
    location_names = []
    locations = []
    restaurant = yelp.find_business(session["term"], location = location)
    if 'businesses' not in restaurant:
        flash('invalid City, Please try again')
        return redirect('/homepage')

    else:
        for place in restaurant['businesses']:
            restaurant_by_id = yelp.search_by_id(place["id"])
            # print(restaurant_by_id["photos"])


            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            # session['list'][place['id']]['img'] =[place][0]['image_url']
            session['list'][place['id']]['img'] =restaurant_by_id["photos"]
            session['list'][place['id']]['rvw count'] =[place][0]['review_count']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['categories'] =[place][0]['categories']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['phone'] =[place][0]['display_phone']
            session['list'][place['id']]['cordinates'] =[place][0]['coordinates']
            session['list'][place['id']]['closed'] =[place][0]['is_closed']
            session['list'][place['id']]['price'] =[place][0].get('price','Not available')
            # print(session['list'])
            # print(session['list'][place['id']]['img'])
            locations.append([place][0]['coordinates'])
            location_names.append([place][0]['name'])
            lon =  -121.901284
            lat = 37.308203
 
    return render_template("restaurant.html", places = session['list'],location = session['location'], cordinates = locations,lon = lon, lat= lat, location_names = location_names)

@app.route("/Movies", methods = ["POST"])
def movies():
    """"movies palying in the area"""
    session['list'] = {}
    movies = fandango.get_movies()

    for movie in movies["results"]:
        # print(movie['original_title'])
        
        session["list"][movie['id']]= {}
        session["list"][movie['id']]["title"]= movie["original_title"]
        session["list"][movie['id']]["img"]= movie["poster_path"]
        session["list"][movie['id']]["vote"]= movie["vote_average"]
        session["list"][movie['id']]["release_date"]= movie["release_date"]
        datetime_object = datetime.strptime(session["list"][movie['id']]["release_date"], '%Y-%m-%d').date()
        session["list"][movie['id']]["release_date"]= datetime_object.strftime("%B, %d %Y")
    return render_template("movie.html", movies = session['list'])


@app.route("/bars", methods = ["POST"])
def bars():
    """"route to parks to bars """
    session['list'] = {}
    session["term"] = request.form.get('term')
    location = session['location']
    location_names = []
    locations = []
    bars = yelp.find_business(session['term'], location=location)
    # print(bars)

    if 'businesses' not in bars:
        flash('invalid City, Please try again')
        return redirect('/homepage')

    else:
        for place in bars['businesses']:
            place_by_id = yelp.search_by_id(place["id"])
            # print("THIS IS PLACES", restaurant['businesses'])
            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            session['list'][place['id']]['img'] =place_by_id["photos"]
            session['list'][place['id']]['rvw count'] =[place][0]['review_count']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['categories'] =[place][0]['categories']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['phone'] =[place][0]['display_phone']
            session['list'][place['id']]['cordinates'] =[place][0]['coordinates']
            session['list'][place['id']]['closed'] =[place][0]['is_closed']
            session['list'][place['id']]['price'] =[place][0].get('price','Not available')
            # print(session['list'])
            locations.append([place][0]['coordinates'])
            location_names.append([place][0]['name'])
            lon =  -121.901284
            lat = 37.308203
            # print(locations)
        
    return render_template("bars.html", bars = bars, places =session['list'],location = session['location'], cordinates = locations,lon = lon, lat= lat, location_names = location_names )

@app.route("/museums", methods = ["POST"])
def musseums():
    """"route to parks to museums"""
    session['list'] = {}
    session["term"] = request.form.get('term')
    location = session["location"]
    location_names = []
    locations = []
    # print(session['location'],"\n\n\n")
    musseums = yelp.find_business(session["term"], location = location)
    # print(restaurant["businesses"][0].keys(), "\n\n\n\n")

    if 'businesses' not in musseums:
        flash('invalid City, Please try again')
        return redirect('/homepage')

    else:
        for place in musseums['businesses']:
            place_by_id = yelp.search_by_id(place["id"])
            # print("THIS IS PLACES", restaurant['businesses'])
            session['list'][place['id']] = {}
            session['list'][place['id']]['name'] =[place][0]["name"]
            session['list'][place['id']]['id'] =[place][0]["id"]
            session['list'][place['id']]['city'] =[place][0]["location"]['city']
            session['list'][place['id']]['state'] =[place][0]["location"]['state']
            session['list'][place['id']]['img'] =place_by_id["photos"]
            session['list'][place['id']]['rvw count'] =[place][0]['review_count']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['categories'] =[place][0]['categories']
            session['list'][place['id']]['rating'] =[place][0]['rating']
            session['list'][place['id']]['phone'] =[place][0]['display_phone']
            session['list'][place['id']]['cordinates'] =[place][0]['coordinates']
            session['list'][place['id']]['closed'] =[place][0]['is_closed']
            session['list'][place['id']]['price'] =[place][0].get('price','Not available')
            # print(session['list'])
            locations.append([place][0]['coordinates'])
            location_names.append([place][0]['name'])
            lon =  -121.901284
            lat = 37.308203
            
        

     

    return render_template("museums.html", musseums = musseums, places = session['list'],location = session['location'], cordinates = locations,lon = lon, lat= lat,location_names = location_names)


@app.route("/events")
def events():
    """"events happeining that day"""

    return render_template("events.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
# ################################################
@app.route('/manage')
def manage():
    logged_in_email = session.get('email')
    user = crud.find_user(logged_in_email)
    return render_template('manage.html', user = user)


@app.route('/updateinfo', methods = ['POST'])
def updateinfo():
    logged_in_email = session.get('email')
    user = crud.find_user(logged_in_email)
    


    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']
    session['email'] = email
    session["name"] = fname.title()


    
    new_user = crud.update_info(user.user_id,fname = fname, lname=lname, email=email)
    flash('Successfully Updated')

    return redirect('/manage')

@app.route('/updatepassword', methods = ['POST'])
def updatepassword():


    logged_in_email = session.get('email')
    user = crud.find_user(logged_in_email)

    new_password = request.form['password']
    conf_password = request.form['conf-password']
    old_password = request.form['old-password']

    if user.password == old_password:
        if new_password== conf_password:
            crud.update_pass(user.user_id, new_pass=new_password)
            flash('Successfully Updated')
        else:
            flash('Passwords Did Not Match!')
    else:
        flash('Incorrect Password, Please Try Again')
    
       

    return redirect('/manage')


if __name__ == "__main__":
    connect_to_db(app, "date")
    app.run(debug=True, host='0.0.0.0')
    