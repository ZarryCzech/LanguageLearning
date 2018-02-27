import config
from flask import g, json
from modules.db import Database


def setg():
    g.collections = Database().collection_names()
    g.rest = config.rest.root
    g.users = config.users
    g.languages = config.languages
    g.words = config.words

    g.username_length = config.username_length
    g.password_length_max = config.password_length_max
    g.course = config.course
    g.language = config.language
