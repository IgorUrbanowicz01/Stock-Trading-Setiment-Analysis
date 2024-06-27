
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback
def create_plot(hist_dict):
    app = Dash()
    app.layout = [html.H2(children="Stocks and Sentiment"),
                  dcc.Dropdown(
                      list(hist_dict.keys()),
                      list(hist_dict)[0],
                      id='dropdown-selection'
                  ),
                  dcc.Graph(id = 'graph-contnt')
                  ]
    @callback(
        Output('graph-contnt', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph_content(selected_value):
        df = hist_dict[selected_value]
        return go.Figure(data=[go.Candlestick(x=df.index,
                               open=df['Open'],
                               high=df['High'],
                               low=df['Low'],
                               close=df['Close'])])



    return app

