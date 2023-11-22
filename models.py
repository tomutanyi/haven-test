from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property



db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model, SerializerMixin):
    __tablename__="users"

    serialize_rules = ("-game_reviews.user",)

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String())

    # game_entries = db.relationship('GameEntry', backref="user" )
    game_reviews = db.relationship('GameReview', backref="user" )

    def _repr_(self):
        return f'<User: {self.username}>'
    

    @hybrid_property
    def password_hash(self):
        raise AttributeError ("Not allowed")
    

    @password_hash.setter

    def password_hash (self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    # def check_password(self, password):
    #     return bcrypt.check_password_hash(self._password_hash, password)
        
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash,password.encode("utf-8"))



class GameEntry(db.Model, SerializerMixin):
    __tablename__="game_entries"

    serialize_rules = ("-game_genres.game_entry", "-game_reviews.game_entry", )

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    platform = db.Column(db.String(), nullable=False)
    image_url = db.Column(db.String(255))
    description = db.Column(db.String(100))

    # user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    

    game_genres = db.relationship('GameGenre', backref='game_entry')
    game_reviews = db.relationship('GameReview', backref='game_entry')

    def _repr_(self):
        return f'Game: {self.title}, Platform: {self.platform}'


class GameReview(db.Model, SerializerMixin):
    __tablename__='game_reviews'

    serialize_rules = ("-user.game_reviews", "-game_entry.game_reviews",)

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer())
    comment = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    game_entry_id = db.Column(db.Integer(), db.ForeignKey('game_entries.id'))

    def _repr_(self):
        return f'<Review: \n Score: {self.rating}, Comment: {self.comment}>'




class Genre(db.Model, SerializerMixin):
    __tablename__="genres"

    serialize_rules = ("-game_genres.genre",)

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String, nullable=False)

    game_genres = db.relationship('GameGenre', backref='genre')

    def _repr_(self):
        return f'<Genre: {self.name}>'



class GameGenre(db.Model, SerializerMixin):
    __tablename__ = "game_genres"

    serialize_rules = ("-game_entry.game_genres", "-genre.game_genres",)

    id=db.Column(db.Integer, primary_key=True)
    game_entry_id = db.Column(db.Integer(), db.ForeignKey('game_entries.id'))
    genre_id = db.Column(db.Integer(), db.ForeignKey('genres.id'))