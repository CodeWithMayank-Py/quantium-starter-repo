import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data from final.csv
df = pd.read_csv('final.csv')

# Initialize the Dash application
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    html.H1("Sales Data Visualizer"),
    dcc.Graph(
        id='sales-chart',
        figure=px.line(df, x='date', y='sales', title='Sales Data Visualization')
    )
])

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
