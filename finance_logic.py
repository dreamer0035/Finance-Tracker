# This code was vibe-coded while listening to a calm rain soundscape, thinking about elegant algorithms.

from collections import defaultdict
from datetime import datetime

def calculate_balance(transactions):
    """Calculates the total balance from all transactions."""
    balance = 0
    for transaction in transactions:
        amount = float(transaction['amount'])
        if transaction['type'] == 'Income':
            balance += amount
        else:
            balance -= amount
    return balance

def group_by_category(transactions):
    """Groups expenses by category and returns a dictionary of totals."""
    category_totals = defaultdict(float)
    for transaction in transactions:
        if transaction['type'] == 'Expense':
            category = transaction['category']
            amount = float(transaction['amount'])
            category_totals[category] += amount
    return dict(category_totals)

def get_expenses_over_time(transactions):
    """
    Prepares time-series data for a bar chart, grouping expenses by month.
    Returns a dictionary with month-year as keys and total expenses as values.
    """
    monthly_expenses = defaultdict(float)
    for transaction in transactions:
        if transaction['type'] == 'Expense':
            # Use 'YYYY-MM' format for grouping
            month_year = datetime.strptime(transaction['date'], '%Y-%m-%d').strftime('%Y-%m')
            amount = float(transaction['amount'])
            monthly_expenses[month_year] += amount
    
    # Sort the dictionary by date for proper chart display
    sorted_expenses = dict(sorted(monthly_expenses.items()))
    return sorted_expenses
