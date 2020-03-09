#!/usr/bin/python3
"""
    This script create file with other file template changing parameters
"""

def search_and_add(_file, search_string, new_string):
    """
    this function search for a specific string and after find it
    add a new string
    example: 
    _file = '/to/path'
    search_string='from models import base_model\n'
    new_string = 'from models import {}\n'.format(value)
    """
    with open(_file, encoding='utf-8') as f:
        buf = f.readlines()
        new_array = []
        for line in buf:
            new_array.append(line)
            if line == search_string:
                new_array.append(new_string)

    with open(_file, 'w') as f:
        for item in new_array:
            f.write(item)


def make_file(path, my_list):
    """
    Args: path: path to new file
          my_list: new data for the file

    Return: None
    """
    with open(path, 'w') as f:
        for item in my_list:
            f.write(item)


def read_file(path):
    """
    Args: path: path to read file

    Return: array with the lines of the file
    """
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def replace_line(data, my_array):
    """
    Args: data : data to replace
          my_array : replace data in this array

    Return: new array with new data
    """
    new_list = []

    for line in my_array:
        for idx, value in data.items():
            line = line.replace(idx, value)
        new_list.append(line)
    return new_list


def render_template(template, data):
    """
    Args: template: path the template base
          data: data to replace

    Return: new template in array
    """
    _file = read_file(template)
    return replace_line(data, _file)
