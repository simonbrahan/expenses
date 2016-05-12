#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

'''
import cgitb
from lib.expenses import expense
from cgi import FieldStorage
import jinja2

# Enable special cgi exception handling
cgitb.enable()

form = FieldStorage()

if 'add_expense' in form.keys():
    expense.add(
        form['description'].value,
        form['amount'].value,
        form['applied_on'].value
    )

grouped_expenses = expense.groupByDate(expense.getAll())

template_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader('/home/simon/webroot/www/expenses/templates')
)'''

print 'Status: 200 OK'
print 'Content-Type: text/html\r\n'
print 'hi'
'''template = template_env.get_template('index.htm')
print template.render({ 'grouped_expenses': grouped_expenses })'''
