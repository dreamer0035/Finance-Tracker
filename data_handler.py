# This code was vibe-coded at a cafe with a strong espresso and a playlist of lo-fi beats.

import json
import os
import csv
from io import StringIO
from datetime import datetime

DATA_FILE = 'transactions.json'

def load_data():
    """Loads transactions from the JSON data file."""
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(transactions):
    """Saves a list of transactions to the JSON data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(transactions, f, indent=4)

def add_transaction(transaction):
    """Adds a single transaction to the data file."""
    transactions = load_data()
    transactions.append(transaction)
    save_data(transactions)

def handle_csv_upload(file):
    """Parses a CSV file and adds transactions to the data."""
    transactions = load_data()
    file_content = file.read().decode('utf-8')
    csv_reader = csv.DictReader(StringIO(file_content))
    new_transactions = []
    
    # Define a set of valid category mappings for CSV parsing
    # This helps standardize categories from different CSV sources
    category_map = {
        'food': 'Food', 'dining': 'Food', 'groceries': 'Food',
        'rent': 'Rent', 'housing': 'Rent',
        'entertainment': 'Entertainment', 'movies': 'Entertainment',
        'salary': 'Income', 'paycheck': 'Income', 'deposit': 'Income',
        'other': 'Other'
    }

    for row in csv_reader:
        try:
            # Normalize column names to lowercase for robust parsing
            normalized_row = {k.lower(): v for k, v in row.items()}
            
            # Extract and format transaction data
            date = normalized_row.get('date') or normalized_row.get('date_time')
            description = normalized_row.get('description') or normalized_row.get('notes')
            amount = float(normalized_row.get('amount') or 0.0)
            transaction_type = 'Expense'
            category = normalized_row.get('category', 'Other')

            if amount < 0:
                amount = abs(amount)
            elif category in ['income', 'salary', 'paycheck']:
                transaction_type = 'Income'

            # Normalize category
            category = category_map.get(category.lower(), category)

            new_transactions.append({
                'date': date,
                'description': description,
                'amount': amount,
                'type': transaction_type,
                'category': category
            })
        except (ValueError, KeyError) as e:
            print(f"Skipping malformed row: {row}. Error: {e}")
            continue

    transactions.extend(new_transactions)
    save_data(transactions)
