#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

import cgi
import jinja2
from lib.expenses import expense

def application(environ, start_response):
    form = cgi.FieldStorage()

    response_body = str(type(form)).encode('utf-8')

    grouped_expenses = expense.groupByDate(expense.getAll())

    template_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(environ['DOCUMENT_ROOT'] + 'templates')
    )

    template = template_env.get_template('index.htm')
    ##response_body = template.render({ 'grouped_expenses': grouped_expenses })

    response_body.encode('utf-8')

    response_headers = [('Content-Type', 'text/html; charset=utf-8'), ('Content-Length', str(len(response_body)))]

    start_response('200 OK', response_headers)
    return response_body
