#!/usr/bin/python3
"""
Flask App that integrates with <[name-app]> static HTML Template
"""
from flask import Flask, render_template, url_for
from uuid import uuid4


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/')
def hbnb_filters(the_id=None):
    """
    handles request to custom template
    """
    return render_template('0-proyect.html', cache_id=uuid4())

'''
add new routes
'''

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
