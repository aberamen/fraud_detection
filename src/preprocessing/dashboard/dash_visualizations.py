# src/dashboard/dash_visualizations.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Fraud Detection Dashboard"),
    
    # Summary Boxes
    html.Div(id='summary-boxes', className='row'),
    
    # Fraud Over Time
    dcc.Graph(id='fraud-over-time'),
    
    # Fraud By Country
    dcc.Graph(id='fraud-by-country'),
    
    # Fraud By Device
    dcc.Graph(id='fraud-by-device'),
    
    # Fraud By Browser
    dcc.Graph(id='fraud-by-browser')
])

# Callback to update summary boxes
@app.callback(
    Output('summary-boxes', 'children'),
    [Input('summary-boxes', 'id')]
)
def update_summary_boxes(_):
    response = requests.get('http://localhost:5001/api/summary')
    data = response.json()
    
    return [
        html.Div([
            html.H3("Total Transactions"),
            html.P(f"{data['total_transactions']}")
        ], className='three columns'),
        
        html.Div([
            html.H3("Fraud Cases"),
            html.P(f"{data['fraud_cases']}")
        ], className='three columns'),
        
        html.Div([
            html.H3("Fraud Percentage"),
            html.P(f"{data['fraud_percentage']:.2f}%")
        ], className='three columns')
    ]

# Callback to update fraud over time
@app.callback(
    Output('fraud-over-time', 'figure'),
    [Input('fraud-over-time', 'id')]
)
def update_fraud_over_time(_):
    response = requests.get('http://localhost:5001/api/fraud_over_time')
    data = response.json()
    df = pd.DataFrame(data)
    
    fig = px.line(df, x='purchase_time', y='class', title='Fraud Cases Over Time')
    return fig

# Callback to update fraud by country
@app.callback(
    Output('fraud-by-country', 'figure'),
    [Input('fraud-by-country', 'id')]
)
def update_fraud_by_country(_):
    response = requests.get('http://localhost:5001/api/fraud_by_country')
    data = response.json()
    df = pd.DataFrame(data)
    
    fig = px.bar(df, x='country', y='class', title='Fraud Cases By Country')
    return fig

# Callback to update fraud by device
@app.callback(
    Output('fraud-by-device', 'figure'),
    [Input('fraud-by-device', 'id')]
)
def update_fraud_by_device(_):
    response = requests.get('http://localhost:5001/api/fraud_by_device')
    data = response.json()
    df = pd.DataFrame(data)
    
    fig = px.bar(df, x='device_id', y='class', title='Fraud Cases By Device')
    return fig

# Callback to update fraud by browser
@app.callback(
    Output('fraud-by-browser', 'figure'),
    [Input('fraud-by-browser', 'id')]
)
def update_fraud_by_browser(_):
    response = requests.get('http://localhost:5001/api/fraud_by_browser')
    data = response.json()
    df = pd.DataFrame(data)
    
    fig = px.bar(df, x='browser', y='class', title='Fraud Cases By Browser')
    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)