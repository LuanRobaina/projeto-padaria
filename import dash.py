import dash
from dash import dcc, html
import plotly.graph_objs as go

# Inicialização do aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Monitoramento de Estoque'),
    dcc.Graph(
        id='grafico-estoque',
        figure={
            'data': [
                go.Scatter(
                    x=dados['timestamp'],
                    y=dados['peso'],
                    mode='lines+markers',
                    name='Peso do Estoque'
                )
            ],
            'layout': go.Layout(
                title='Peso do Estoque ao Longo do Tempo',
                xaxis={'title': 'Tempo'},
                yaxis={'title': 'Peso (kg)'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
