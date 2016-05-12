#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

import jinja2

def application(environ, start_response):
    grouped_expenses = expense.groupByDate(expense.getAll())

    response_body = 'kebbles'

    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]

    start_response('200 OK', response_headers)
    return [response_body]
