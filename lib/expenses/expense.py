import dbconn


def getAll():
    conn = dbconn.get()

    cursor = conn.cursor()
    cursor.execute(
        """select amount, description, applied_on from expense
           order by applied_on desc limit 10"""
    )

    column_names = ['amount', 'description', 'applied_on']

    expenses = []
    for row in cursor.fetchall():
        # Convert row list to dictionary with column names as keys
        expense = dict(zip(column_names, row))
        expense['description'] = expense['description'].decode('utf-8')
        expenses.append(expense)

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


def getCategories():
    conn = dbconn.get()

    cursor = conn.cursor()
    cursor.execute(
        """
            select
                lower(split_part(description, ' ', 1)) category,
                sum(amount) as total
        from expense
        group by lower(split_part(description, ' ', 1))
        order by total desc
        """
    )

    column_names = ['category', 'total']

    categories = []
    for row in cursor.fetchall():
        # Convert row list to dictionary with column names as keys
        categories.append(dict(zip(column_names, row)))

    return categories
