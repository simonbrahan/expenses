import dbconn


def getAll():
    conn = dbconn.get()

    return 'kebbles'
    cursor = conn.cursor()
    cursor.execute(
        """select amount, description, applied_on from expense
           order by applied_on desc limit 10"""
    )

    column_names = ['amount', 'description', 'applied_on']

    expenses = []
    for row in cursor.fetchall():
        # Convert row list to dictionary with column names as keys
        expenses.append(dict(zip(column_names, row)))

    return expenses


def groupByDate(expenses):
    keyed_grouped_expenses = {}

    for ungrouped_expense in expenses:
        if ungrouped_expense['applied_on'] not in keyed_grouped_expenses:
            keyed_grouped_expenses[ungrouped_expense['applied_on']] = []

        keyed_grouped_expenses[
            ungrouped_expense['applied_on']
        ].append(ungrouped_expense)

    grouped_expenses = keyed_grouped_expenses.items()
    grouped_expenses.sort(reverse=True)

    return grouped_expenses

def add(description, amount, applied_on):
    conn = dbconn.get()
    conn.cursor().execute(
        """insert into expense (amount, description, applied_on)
           values (%s, %s, %s)""",
        (amount, description, applied_on)
    )
    conn.commit()
