from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from data import countries_df, totals_df, dropdown_options
from builders import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(
    countries_df,
    size="Confirmed",
    hover_name="Country_Region",
    locations="Country_Region",
    locationmode="country names",
    size_max=40,
    title="Confirmed By Country",
    color="Confirmed",
    template="plotly_dark",
    color_continuous_scale=px.colors.sequential.Oryel,
    # projection="natural earth",
    hover_data={
        "Confirmed": ":,",
        "Recovered": ":,",
        "Deaths": ":,",
        "Country_Region": False,
    },
)

bars_graph = px.bar(
    totals_df,
    x="condition",
    y="count",
    template="plotly_dark",
    title="Total Global Cases",
    hover_data={"count": ":,"},
    labels={"condition": "Condition", "count": "Count", "color": "Condition"},
)

bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={"textAlign": "center", "paddingTop": "50px", "marginBottom": 100},
            children=html.H1("Corona Dashboard", style={"fontSize": 40}),
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[dcc.Graph(figure=bubble_map)],
                ),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
                html.Div(
                    children=[
                        dcc.Dropdown(
                            style={"color": "black"}, id="country", options=[]
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(Output("hello-output", "children"), [Input("country", "value")])
def update_hello(value):
    if value is None:
        return "Hello Anonymous"
    else:
        return f"Hello {value}"


if __name__ == "__main__":
    app.run(debug=True)
