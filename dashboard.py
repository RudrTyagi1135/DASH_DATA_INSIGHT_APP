import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc

# 1. Load Data
df = pd.read_csv('gapminder.csv')
# Filtering for a single year to make the scatter plot cleaner
df_2007 = df[df['year'] == 2007]

# 2. Create the Scatter Plot (Left)
fig_scatter = go.Figure(data=[
    go.Scatter(
        x=df_2007['gdpPercap'], 
        y=df_2007['lifeExp'], 
        mode='markers',
        marker=dict(color='#3176B1') # Matching the blue in your image
    )
])
fig_scatter.update_layout(title='Scatter Plot', template='ggplot2')

# 3. Create the Boxplot (Right)
fig_box = go.Figure(data=[
    go.Box(
        x=df_2007['lifeExp'], 
        name='Life Expectancy',
        marker_color='#3176B1'
    )
])
fig_box.update_layout(title='Boxplot', template='ggplot2')

# 4. App Layout
app = Dash(__name__)

app.layout = html.Div([
    # Red Title at the top
    html.H1(
        "My First Dashboard", 
        style={'textAlign': 'center', 'color': 'red', 'fontSize': '32px', 'marginBottom': '20px'}
    ),
    
    # Flex container for side-by-side charts
    html.Div([
        # Left Graph
        html.Div([
            dcc.Graph(figure=fig_scatter)
        ], style={'width': '49%', 'display': 'inline-block', 'border': '1px solid #ddd'}),
        
        # Right Graph
        html.Div([
            dcc.Graph(figure=fig_box)
        ], style={'width': '49%', 'display': 'inline-block', 'border': '1px solid #ddd', 'marginLeft': '1%'})
        
    ], style={'display': 'flex', 'padding': '10px'})
])

if __name__ == '__main__':
    app.run(debug=True)
