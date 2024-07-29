
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback
def create_plot(hist_dict):
    app = Dash()
    app.layout = html.Div([
        html.H2(id='title-stock'),
                  dcc.Dropdown(
                      list(hist_dict.keys()),
                      list(hist_dict)[0],
                      id='dropdown-selection'
                  ),
                  dcc.Graph(id='graph-contnt')
                  ])
    @callback(
        Output('graph-contnt', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph_content(selected_value):
        df = hist_dict[selected_value]
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                               open=df['Open'],
                               high=df['High'],
                               low=df['Low'],
                               close=df['Close'])],
                        layout={'margin':dict(l=40, r=20, t=60, b=20),
                                'height' : 500,
                                'paper_bgcolor': 'LightSteelBlue'})
        fig.update_layout()
        return fig
    @callback(
        Output('title-stock', 'children'),
        Input('dropdown-selection', 'value')
    )
    def update_title(selected_value):
        return str(selected_value) + ' stock and public opinion'

    return app