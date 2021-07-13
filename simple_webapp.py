import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    [
            dbc.Row(dbc.Col(html.H1(""))),
            dbc.Row(dbc.Col(html.H1("Schnellrechner"), style={"color" : "blue"})),
            dbc.Row(dbc.Col(html.H1(""))),
            dbc.Row(

                    [
                    dbc.Col(html.Div("Höhe"),
                            #style={"border" : "blue solid", "align-items" : "center"},
                            width = {"size" : 1, "offset" : 1}),
                    dbc.Col(dbc.Input(id="input1", placeholder="...", type="number",
                            style={"width" : "10%"})),
                    ]
                ),
            dbc.Row(dbc.Col(html.H1(""))),
            dbc.Row(
                    [
                    dbc.Col(html.Div("Breite"),
                            width = {"size" : 1, "offset" : 1}),
                    dbc.Col(dbc.Input(id="input2", placeholder="...", type="number",
                            style={"width" : "10%"})),
                    ]
                ),
            dbc.Row(dbc.Col(html.H1(""))),
            dbc.Row(
                [
                    dbc.Col(html.Div("Länge"),
                            width={"size": 1, "offset": 1}),
                    dbc.Col(dbc.Input(id="input3", placeholder="...", type="number",
                                      style={"width": "10%"})),
                ]
                ),
            dbc.Row(dbc.Col(html.H1(""))),
            dbc.Row([
                    dbc.Col(html.Div(""),
                            #style={"border": "blue solid"},
                            width={"size": 1, "offset": 1}),
                    dbc.Button("Berechnen", id = "button1", color="primary", className="mr-1", n_clicks=0,
                                    style={"width" : "10%"}),
                ]
            ),
            dbc.Row(dbc.Col(html.H1(""))),

            dbc.Row(
                [
                    dbc.Col(html.Div("Kostenwert"),
                            width={"size": 1, "offset": 1}),
                    dbc.Col(html.P(id="output",
                                      style={"width": "10%"})),
            ]
        ),
    ]
)

global counter
counter = 0

@app.callback(Output("output", "children"),
              [
                  Input("input1", "value"),
                  Input("input2", "value"),
                  Input("input3", "value"),
                  Input("button1", "n_clicks")
              ])
def output_text(val1, val2, val3, n_click):
    global counter
    if n_click > 0 and n_click > counter:
        erg = (val1/val2) + 2.3*val3
        n_click_new = n_click + 1
        counter+=1
        return erg
    else:
        return ""

if __name__ == "__main__":
    app.run_server()