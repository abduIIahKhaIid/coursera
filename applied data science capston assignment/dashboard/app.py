import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
df = pd.read_csv('falcon9_launches.csv')

# Create Plotly figure
fig = px.bar(df, x='Launch Site', color='Success', title='Launch Success by Site')

app.layout = html.Div([
    html.H1('SpaceX Falcon 9 Dashboard'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)