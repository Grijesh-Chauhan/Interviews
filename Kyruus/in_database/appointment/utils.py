import datetime
from json import dumps

from flask import make_response, current_app
from flask_restful.utils import PY3

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    raise TypeError ("Type %s not serializable" % type(o))

def output_json(data, code, headers=None):
    # referces: 
    # https://flask-restful.readthedocs.io/en/latest/extending.
    # python3.6/site-packages/flask_restful/representations/json.py
    # https://stackoverflow.com/questions/11875770/
    
    settings = current_app.config.get('RESTFUL_JSON', {})
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)
    settings['default'] = default
    dumped = dumps(data, **settings) + "\n"
    return make_response(dumped, code)

