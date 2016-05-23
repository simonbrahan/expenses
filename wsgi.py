#!/usr/bin/python
import os

if 'OPENSHIFT_PYTHON_DIR' in os.environ.keys():
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    try:
        execfile(virtualenv, dict(__file__=virtualenv))
    except IOError:
        pass

import cgi
import os.path
import urlparse
import jinja2

from lib.expenses import dbconn
from lib.expenses import expense

def application(environ, start_response):
    dbconn.init(environ)

    post_body = urlparse.parse_qs(environ['wsgi.input'].read())
    if 'add_expense' in post_body.keys():
        expense.add(
            post_body['description'][0],
            post_body['amount'][0],
            post_body['applied_on'][0]
        )

    grouped_expenses = expense.groupByDate(expense.getAll())


    template_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.join(environ['DOCUMENT_ROOT'], 'templates'))
    )

    template = template_env.get_template('index.htm')
    response_body = template.render({ 'grouped_expenses': grouped_expenses }).encode('utf-8')

    response_headers = [('Content-Type', 'text/html; charset=utf-8'), ('Content-Length', str(len(response_body)))]

    start_response('200 OK', response_headers)

    return response_body
