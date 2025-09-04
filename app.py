# This code was vibe-coded while feeling inspired to integrate all the pieces together.

from flask import Flask, render_template, request, redirect, url_for
from datetime import date
from data_handler import load_data, add_transaction, handle_csv_upload
from finance_logic import calculate_balance, group_by_category, get_expenses_over_time
from visualization import generate_pie_chart, generate_bar_chart

app = Flask(__name__)

@app.route('/')
def index():
    """Main dashboard route, loads data and renders the charts and info."""
    transactions = load_data()
    balance = calculate_balance(transactions)
    
    # Generate data for charts
    category_data = group_by_category(transactions)
    time_series_data = get_expenses_over_time(transactions)

    # Generate base64 images of the charts
    pie_chart_img = generate_pie_chart(category_data)
    bar_chart_img = generate_bar_chart(time_series_data)
    
    return render_template(
        'index.html',
        transactions=transactions,
        balance=balance,
        pie_chart_img=pie_chart_img,
        bar_chart_img=bar_chart_img,
        today=date.today().isoformat()
    )

@app.route('/add_transaction', methods=['POST'])
def add_new_transaction():
    """Handles manual transaction entry from the form."""
    try:
        transaction = {
            'date': request.form['date'],
            'description': request.form['description'],
            'amount': float(request.form['amount']),
            'type': request.form['type'],
            'category': request.form['category']
        }
        add_transaction(transaction)
    except (ValueError, KeyError) as e:
        print(f"Error adding transaction: {e}")
    return redirect(url_for('index'))

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    """Handles CSV file upload and processes it."""
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        handle_csv_upload(file)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
