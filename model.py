from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_to_db(app, db_name):
    """Connect to database."""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    fname = db.Column(db.String)
    lname = db.Column(db.String)

    user_sug = db.relationship('User_Suggestions', back_populates="users")
    

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
#Place
# class Places(db.Model):
#     __tablename__ = "places"

#     place_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     place_ylp_id = db.Column(db.String(255), unique =True, nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     city = db.Column(db.String(50), nullable=False)
#     zip_code = db.Column(db.Integer, nullable=False)
#     address = db.Column(db.String(50), nullable=True)
#     type = db.Column(db.String(50), nullable=False)
#     img = db.Column(db.String, nullable=False)

#     fav_place = db.relationship("User_fav_places", back_populates="place")
# #name, lovation, cist , img 

# #user-fav-Plce - middle table
# class User_fav_places(db.Model):

#     __tablename__ = "user_fav_places"

#     fav_places_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     favorite_place_id = db.Column(db.Integer, db.ForeignKey("places.place_id"), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
#     likes = db.Column(db.Boolean, default = True, nullable = False) #*make sure this is how you write it


#     place = db.relationship("Places", back_populates="fav_place") #!
#     user = db.relationship("User", back_populates="fav_place") #! 
#usr
class User_Suggestions(db.Model):
    """"middle class between user and siggestion- where users can save their favorite dates"""
    __tablename__ = "user_suggestions"

    use_sug_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    sug_id = db.Column(db.Integer, db.ForeignKey('suggestions.sug_id'), nullable = False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.type_id'), nullable = False)


    users = db.relationship('User', back_populates = 'user_sug')
    sugg = db.relationship('Suggestion', back_populates = 'user_sug')
    type = db.relationship('Type', back_populates ="use_sugg" )



class Suggestion(db.Model):
    """"Date suggestions"""

    __tablename__ = "suggestions"

    sug_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    sug_name = db.Column(db.String, unique=True)
    sug_details = db.Column(db.String)
    sug_type = db.Column(db.Integer, db.ForeignKey('type.type_id'))

    user_sug = db.relationship('User_Suggestions', back_populates="sugg")
    type = db.relationship('Type', back_populates ="sugg" )
    location = db.relationship('Location', back_populates= "sugg" )



    # def __repr__(self):
    #     return f'< >'


class Type(db.Model):
    """List of activities that a user can choose from"""
    
    __tablename__ = "type"

    type_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    type = db.Column(db.String)

    use_sugg = db.relationship('User_Suggestions', back_populates = 'type')
    sugg = db.relationship('Suggestion', back_populates = 'type')


    def __repr__(self): 
        return f'< >'


class Location(db.Model):
    """Locations of restaurants or events """

    __tablename__ = "locations"
    
    location_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    city = db.Column(db.String, nullable = False)
    state = db.Column(db.String, nullable = False)
    zipcode = db.Column(db.Integer, nullable = False)
    sug_id = db.Column(db.Integer, db.ForeignKey('suggestions.sug_id'))
    


    sugg = db.relationship('Suggestion', back_populates = 'location')

    def __repr__(self):     
        return f'< >'


# class Event():
#     """Events areound user"""

#     __tablename__ = "events"

#     event_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     event_name = db.Column(db.String)
#     event_time = db.Column(db.datetime)
#     event_locations = db.Column(db.String)
#     event_details = db.Column(db.Text)

#     def __repr__(self):     
#         return f'< >'


if __name__ == "__main__":
    from server import app

    connect_to_db(app, "date")
    # with app.app_context():
    #     db.create_all() 