#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.<[name-api-lower]> import <[name-api-capitalize]>


@app_views.route('/<[name-api-pluralize]>', methods=['GET'])
def get_<[name-api-pluralize]>():
    """
    List of all <[name-api-capitalize]> objects
    """
    pass


@app_views.route('/<[name-api-pluralize]>/<<[name-api-lower]>_id>', methods=['GET'])
def get_<[name-api-lower]>(<[name-api-lower]>_id):
    """
    The <[name-api-capitalize]> based on the id
    """
    pass


@app_views.route('/<[name-api-pluralize]>/<<[name-api-lower]>_id>', methods=['DELETE'])
def delete_<[name-api-lower]>(<[name-api-lower]>_id):
    """
    Function to deletes a <[name-api-capitalize]> by id
    """
    pass


@app_views.route('/<[name-api-pluralize]>', methods=['POST'])
def create_<[name-api-lower]>(<[name-api-lower]>_id):
    """
    Create new <[name-api-capitalize]>
    """
    pass


@app_views.route('/<[name-api-pluralize]>/<<[name-api-lower]>_id>', methods=['PUT'])
def update_<[name-api-lower]>(<[name-api-lower]>_id):
    """
    Update <[name-api-capitalize]> by id
    """
    pass
