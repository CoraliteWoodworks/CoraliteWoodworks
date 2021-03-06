from flask import render_template
from sqlalchemy import func

from Coralite import *


@app.route('/')
@flask_optimize.optimize()
def main():
    page_description = Descriptions.query.filter_by(portfolio="default").first()
    testimonials = Testimonials.query.order_by(func.rand()).limit(3).all()
    return render_template('index.html', page_description=page_description, testimonials=testimonials)


def show(n, Class, portfolio, portfolio_full):
    page_description = Descriptions.query.filter_by(portfolio=portfolio).first()
    if page_description is None:
        page_description = Descriptions.query.filter_by(portfolio="default").first()
    row = Class.query.count()
    if int(n) is 0:
        description = []
        location = []
        for num in range(1, row + 1):
            data = Class.query.filter_by(id=num).first()
            description.append(Class.get_description(data))
            location.append(Class.get_location(data))
        return render_template('Gallery Directory.html', portfolio=portfolio, portfolioFull=portfolio_full, row=row,
                               description=description, location=location, page_description=page_description, )
    elif int(n) >= 1:
        data = Class.query.filter_by(id=n).first()
        return render_template('Gallery Basic.html', portfolio=portfolio, portfolioFull=portfolio_full,
                               id=int(n), page_description=page_description, row=row, data=data)


@app.errorhandler(404)
@flask_optimize.optimize()
def page_not_found(e):
    page_description = Descriptions.query.filter_by(portfolio="default").first()
    return render_template('404.html', page_description=page_description), 404


@app.route('/testimonials')
@flask_optimize.optimize()
def testimonials():
    page_description = Descriptions.query.filter_by(portfolio="default").first()
    testimonials = Testimonials.query.all()
    return render_template('testimonials.html', page_description=page_description, testimonials=testimonials)


@app.route('/additions', methods=['GET'], defaults={'n': 0})
@app.route('/additions/<n>', methods=['GET'])
@flask_optimize.optimize()
def additions(n):
    return show(int(n), Additions, 'additions', 'Additions & Renovations')


@app.route('/bars', methods=['GET'], defaults={'n': 0})
@app.route('/bars/<n>', methods=['GET'])
@flask_optimize.optimize()
def bars(n):
    return show(int(n), Bars, 'bars', 'Bars & Wine Storage')


@app.route('/basements', methods=['GET'], defaults={'n': 0})
@app.route('/basements/<n>', methods=['GET'])
@flask_optimize.optimize()
def basements(n):
    return show(int(n), Basements, 'basements', 'Basements')


@app.route('/bathrooms', methods=['GET'], defaults={'n': 0})
@app.route('/bathrooms/<n>', methods=['GET'])
@flask_optimize.optimize()
def bathrooms(n):
    return show(int(n), Bathrooms, 'bathrooms', 'Bathrooms & Vanities')


@app.route('/builtins', methods=['GET'], defaults={'n': 0})
@app.route('/builtins/<n>', methods=['GET'])
@flask_optimize.optimize()
def builtins(n):
    return show(int(n), Builtins, 'builtins', 'Built-ins & Bookcases')


@app.route('/decks', methods=['GET'], defaults={'n': 0})
@app.route('/decks/<n>', methods=['GET'])
@flask_optimize.optimize()
def decks(n):
    return show(int(n), Decks, 'decks', 'Decks & Porches')


@app.route('/kitchens', methods=['GET'], defaults={'n': 0})
@app.route('/kitchens/<n>', methods=['GET'])
@flask_optimize.optimize()
def kitchens(n):
    return show(int(n), Kitchens, 'kitchens', 'Kitchens')


@app.route('/mantels', methods=['GET'], defaults={'n': 0})
@app.route('/mantels/<n>', methods=['GET'])
@flask_optimize.optimize()
def mantels(n):
    return show(int(n), Mantels, 'mantels', 'Mantels')


@app.route('/mudrooms', methods=['GET'], defaults={'n': 0})
@app.route('/mudrooms/<n>', methods=['GET'])
@flask_optimize.optimize()
def mudrooms(n):
    return show(int(n), Mudrooms, 'mudrooms', 'Mudrooms & Closets')


@app.route('/offices', methods=['GET'], defaults={'n': 0})
@app.route('/offices/<n>', methods=['GET'])
@flask_optimize.optimize()
def offices(n):
    return show(int(n), Offices, 'offices', 'Desks & Offices')


@app.route('/paneling', methods=['GET'], defaults={'n': 0})
@app.route('/paneling/<n>', methods=['GET'])
@flask_optimize.optimize()
def paneling(n):
    return show(int(n), Paneling, 'paneling', 'Paneling & Wainscoting')


@app.route('/stock', methods=['GET'], defaults={'n': 0})
@app.route('/stock/<n>', methods=['GET'])
@flask_optimize.optimize()
def stock(n):
    return show(int(n), Stock, 'stock', 'Stock Cabinets')


@app.route('/tv', methods=['GET'], defaults={'n': 0})
@app.route('/tv/<n>', methods=['GET'])
@flask_optimize.optimize()
def tv(n):
    return show(int(n), TV, 'tv', 'TV Entertainment Centers')


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0")
