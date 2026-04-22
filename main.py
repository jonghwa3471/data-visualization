from dash import Dash, html, dcc
import plotly.express as px
from data import countries_df, totals_df
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
    projection="natural earth",
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
)
bars_graph.update_layout(xaxis=dict(title="Condition"), yaxis=dict(title="Count"))

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
            children=[
                html.Div(children=[dcc.Graph(figure=bubble_map)]),
                html.Div(children=[make_table(countries_df)]),
            ]
        ),
        html.Div(
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
            ]
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
