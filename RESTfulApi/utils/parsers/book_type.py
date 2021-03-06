#!/usr/bin/env python
# encoding: utf-8

"""
    File name: book_type.py
    Function Des: ...
    ~~~~~~~~~~
    
    author: Jerry <cuteuy@gmail.com> <http://www.skyduy.com>
    
"""
from flask.ext.restful import reqparse


# ------------ book_type add parser ------------
book_type_post_parser = reqparse.RequestParser()
book_type_post_parser.add_argument(
    'name', dest='name',
    type=unicode, location='form',
    required=True, help='The book_type\'s name',
)
