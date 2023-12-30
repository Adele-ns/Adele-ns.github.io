from flask import Flask, render_template
from flask import request, jsonify
from flask import Flask
from models import db, Language
from flask_sqlalchemy import SQLAlchemy

app = Flask(__