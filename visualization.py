# This code was vibe-coded with a focus on visual aesthetics and a late-night cup of tea.

import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_pie_chart(category_data):
    """
    Generates a pie chart from category data and returns it as a base64 encoded image.
    
    Args:
        category_data (dict): A dictionary with category names as keys and total expenses as values.
    
    Returns:
        str: A base64-encoded string of the PNG image.
    """
    if not category_data:
        return "" # Return empty string if no data

    labels = category_data.keys()
    sizes = category_data.values()
    
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(6, 6), facecolor="#f9f4f4")
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Expense Distribution by Category')
    
    # Save the chart to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig) # Close the figure to free memory
    buffer.seek(0)
    
    # Encode to base64
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return img_base64

def generate_bar_chart(time_series_data):
    """
    Generates a bar chart from time-series data and returns it as a base64 encoded image.
    
    Args:
        time_series_data (dict): A dictionary with dates/months as keys and total expenses as values.
    
    Returns:
        str: A base64-encoded string of the PNG image.
    """
    if not time_series_data:
        return "" # Return empty string if no data

    months = list(time_series_data.keys())
    expenses = list(time_series_data.values())
    
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(10, 6), facecolor="#f9f5f4")
    ax.bar(months, expenses, color='skyblue' 'red')
    ax.set_title('Total Expenses Over Time')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Expenses ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the chart to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    
    # Encode to base64
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return img_base64
