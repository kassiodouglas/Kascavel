from flask import Flask
from src.app.core.router import router

app = Flask(__name__)

from src.routes.web import *
from src.routes.api import *
from src.routes.error import *

router(app)




