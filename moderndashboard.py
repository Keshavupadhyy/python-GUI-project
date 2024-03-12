import dash
from dash import dcc, html
import pandas as pd

# Sample data (replace this with your data)
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [20, 14, 25, 30]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Modern Dashboard"),

    dcc.Graph(
        id='bar-chart',
        figure={
            'data': [
                {'x': df['Category'], 'y': df['Values'], 'type': 'bar', 'name': 'Category Values'}
            ],
            'layout': {
                'title': 'Bar Chart'
            }
        }
    ),

    dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': category, 'value': category} for category in df['Category']
        ],
        value='A',  # Default selected value
        multi=False,
        style={'width': '50%'}
    ),

    dcc.Graph(id='line-chart'),

])

# Define callback to update line chart based on dropdown selection
@app.callback(
    dash.dependencies.Output('line-chart', 'figure'),
    [dash.dependencies.Input('category-dropdown', 'value')]
)
def update_line_chart(selected_category):
    filtered_df = df[df['Category'] == selected_category]

    figure = {
        'data': [
            {'x': filtered_df['Category'], 'y': filtered_df['Values'], 'type': 'line', 'name': 'Category Values'}
        ],
        'layout': {
            'title': f'Line Chart for {selected_category}'
        }
    }

    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
