from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import password, ip
from flask_optimize import FlaskOptimize

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coralite:' + password + '@' + ip + '/coralite'
db = SQLAlchemy(app)

flask_optimize = FlaskOptimize()


class Descriptions(db.Model):
    __tablename__ = 'descriptions'
    id = db.Column('id', db.Integer, primary_key=True)
    portfolio = db.Column('portfolio', db.String(length=128))
    description = db.Column('description', db.String(length=256))

    def __repr__(self):
        return self.description


class Testimonials(db.Model):
    __tablename__ = 'testimonials'
    id = db.Column('id', db.Integer, primary_key=True)
    content = db.Column('content', db.String(length=10000))
    source = db.Column('source', db.String(length=128))
    link = db.Column('link', db.String(length=256))

    def __init__(self, content, source, link):
        self.content = content
        self.source = source
        self.link = link

    def __repr__(self):
        return '<Testimonial %r>' % self.link

    def get_content(self):
        if self.content is not None:
            return self.content
        else:
            return ""

    def get_source(self):
        return self.source

    def get_link(self):
        return self.link


class Additions(db.Model):
    __tablename__ = 'additions'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Additions %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Bars(db.Model):
    __tablename__ = 'bars'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Bars %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Basements(db.Model):
    __tablename__ = 'basements'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Basements %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Bathrooms(db.Model):
    __tablename__ = 'bathrooms'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Bathrooms %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Builtins(db.Model):
    __tablename__ = 'builtins'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Builtins %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Decks(db.Model):
    __tablename__ = 'decks'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Decks %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Kitchens(db.Model):
    __tablename__ = 'kitchens'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Kitchens %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Mantels(db.Model):
    __tablename__ = 'mantels'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Mantels %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Mudrooms(db.Model):
    __tablename__ = 'mudrooms'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Mudrooms %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Offices(db.Model):
    __tablename__ = 'offices'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Offices %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Paneling(db.Model):
    __tablename__ = 'paneling'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Paneling %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<Stock %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""


class TV(db.Model):
    __tablename__ = 'tv'
    id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column('description', db.String(length=255))
    location = db.Column('location', db.String(length=128))
    gallery_id = db.Column('gallery_id', db.String(length=255), unique=True)
    cpo = db.Column('cpo', db.String(length=255))
    images = db.Column('images', db.Integer, nullable=False, default=0)

    def __init__(self, description, gallery_id, cpo):
        self.description = description
        self.gallery_id = gallery_id
        self.cpo = cpo

    def __repr__(self):
        return '<TV %r>' % self.description

    def get_description(self):
        if self.description is not None:
            return self.description
        else:
            return ""

    def get_location(self):
        if self.location is not None:
            return self.location
        else:
            return ""
