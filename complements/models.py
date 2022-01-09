from flask import Flask, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from complements import db


class User(UserMixin):
    username = ""
    password_hash = ""

    def __init__(self, username):
        self.username = username

    @staticmethod
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def set_pwhash(self, password):
        self.password_hash = password

    @staticmethod
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

