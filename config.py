import json
with open('assets/backbones.json') as f: DATA = json.load(f)

#TOKEN = open(".mapbox_token").read() # get your own token
TOKEN = 'pk.eyJ1IjoiZ3JhbnRtZW5nIiwiYSI6ImNraHZoYXl5MTAwYnAzMHBrb211d3R3YTgifQ.wrJwTnuikIlseH9n-qxWaw'
APP_TITLE = 'Real-time Network Health Dashboard'
LAYOUT = dict(
    #margin ={'l':0,'t':0,'b':0,'r':0},
    title_text='<b>' + APP_TITLE + '</b>',
    title_font_color="blue",
    height=900,
    autosize=True,
    showlegend=True,
    hovermode='closest',
    hoverlabel=dict(bgcolor='lightblue'),
    mapbox=dict(
        accesstoken=TOKEN,
        bearing=0,
        center=dict(lat=40.5954563, lon=-74.1477251),
        pitch=0,
        zoom=9.5))
TEXT_FONT = dict(size=15, color='blue', family='arial')
TEXT_POS = 'top center'
HOST = '0.0.0.0'
DEBUG = False
THREADED = False
