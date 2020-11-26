from config import *
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask_caching import Cache
import plotly.graph_objects as go

### DATA initialization: all uppercase variables are initialized in config.py
lat, lon, text, color = [], [], [], []
for key, val in DATA.items():
    if key == 'connect': continue
    text.append(key)
    lat.append(val['lat'])
    lon.append(val['lon'])
    color.append(val['color'])

fig = go.Figure(go.Scattermapbox(
    lat=lat,
    lon=lon,
    text=text,
    textposition=TEXT_POS,
    textfont=TEXT_FONT,
    marker=go.scattermapbox.Marker(size=15, color=color),
    mode='text+markers'
))

for connect in DATA['connect']:
    src, dest = connect['src'], connect['dest']
    fig.add_trace(go.Scattermapbox(
        name=connect['label'], # show label on right side legend
        mode="lines",
        hovertemplate='<b>'+DATA[src]['address']+'</b><extra></extra>', # <extra></extra> to hide trace info
        lon=[DATA[src]['lon'], DATA[dest]['lon']],
        lat=[DATA[src]['lat'], DATA[dest]['lat']]
    ))
fig.update_layout(LAYOUT)
#fig.show()

app = dash.Dash()
app.title = APP_TITLE
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
# The dash Interval element allows you to update components on a predefined interval. The n_intervals property is an integer that is automatically incremented every time interval milliseconds pass. You can listen to this variable inside your app's callback to fire the callback on a predefined interval. id has to be 'live-update-graph'
app.layout = html.Div([
    dcc.Graph(id='live-update-graph', figure=fig),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0)
])

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    import json
    with open('assets/backbones.json') as f: DATA = json.load(f)
    import random
    color = []
    for key, val in DATA.items():
        if key == 'connect': continue
        #color.append(val['color'])
        color.append(random.choice(['red', 'green', 'orange']))
    fig['data'][0]['marker']['color'] = color
    return fig

app.run_server(host=HOST, debug=DEBUG, threaded=THREADED)
