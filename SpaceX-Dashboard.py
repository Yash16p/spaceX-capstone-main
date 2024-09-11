# This dashboard answers the following questions 
# 1. Which site has the largest successful launches?
# 2. Which site has the highest launch success rate?
# 3. Which payload range(s) has the highest launch success rate?
# 4. Which payload range(s) has the lowest launch success rate?
# 5. Which F9 Booster version (v1.0, v1.1, FT, B4, B5, etc.) has the highest launch success rate?


import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


spacex_df = pd.read_csv("spacex_launch_dash.csv")


min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard', 
            style={'textAlign': 'center', 'color': '#503D36',
                   'font-size': 40}),
    
  
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True
                 ),
    html.Br(),

   
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    

    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                    value=[min_payload, max_payload]),

 
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches by Site')
        return fig
    else:
       
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='class', 
                     title=f"Total Success Launches for site {entered_site}")
        return fig


@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_plot(entered_site, payload_range):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
                            (spacex_df['Payload Mass (kg)'] <= payload_range[1])]

    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                         color="Booster Version Category",
                         title='Correlation between Payload and Success for all Sites')
        return fig
    else:
       
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                         color="Booster Version Category",
                         title=f"Correlation between Payload and Success for site {entered_site}")
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
