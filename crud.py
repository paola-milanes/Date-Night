
from model import db, User, Suggestion,Type, Location, connect_to_db, User_Suggestions
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()


def create_user(fname,lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname,lname=lname, email=email, password=password)
    print(user.email,"\n\n\n")

    # db.session.add(user) 
    # db.session.commit() 

    return user
    
def find_user(email):
    user = User.query.filter(User.email == email).first()
    print(user)
    return user

def create_suggestions(name, details, types):
    """retun suggestions"""

    suggestions = Suggestion(name = name, details = details,types = types)
    
    return suggestions

def create_User_seggestion(user_id, sug_id):

    user_sug = User_Suggestions(user_id = user_id, sug_id = sug_id)
    

    return user_sug

def create_types(type):

    types = Type(type=type)

  
    return types


def create_location(city, state, zipcode):

    location = Location(city=city, state= state, zipcode = zipcode)

   
    return location

if __name__ == "__main__":
    from server import app

    connect_to_db(app, "date")
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all() 
    #     user = create_user("a","b","c","d")
    #     db.session.add(user)  
    #     db.session.commit()
    #     print(User.query.first())

