import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Carrega os dados
df = pd.read_csv("diabetes_dataset.csv")

# Inicializa o app Dash
app = dash.Dash(__name__)
app.title = "Diabetes Dashboard"

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Diabetes", style={"textAlign": "center"}),

    html.Div([
        html.Label("Selecione uma variável para análise:"),
        dcc.Dropdown(
            id='variavel_dropdown',
            options=[{"label": col, "value": col} for col in df.columns if col != 'Outcome'],
            value='Glucose'
        )
    ], style={'width': '40%', 'margin': 'auto'}),

    dcc.Graph(id='grafico_histograma'),

    dcc.Graph(
        figure=px.pie(df, names="Outcome", title="Distribuição de Diabetes (0 = Não, 1 = Sim)")
    ),

    dcc.Graph(
        figure=px.scatter(df, x="Age", y="Glucose", color="Outcome",
                          title="Idade vs Glicose por Diagnóstico")
    )
])

# Callback para atualizar histograma
@app.callback(
    Output('grafico_histograma', 'figure'),
    Input('variavel_dropdown', 'value')
)
def atualizar_histograma(variavel):
    fig = px.histogram(df, x=variavel, color="Outcome", barmode='overlay',
                       title=f"Distribuição de {variavel}")
    return fig

# Executa o app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=7860)
