import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# -----------------------------
# Load and prepare data
# -----------------------------
df = pd.read_csv("output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# -----------------------------
# Create Dash app
# -----------------------------
app = Dash(__name__)

app.layout = html.Div(style={
    "backgroundColor": "#f5f5f5",
    "padding": "20px",
    "fontFamily": "Arial"
}, children=[

    # Header
    html.H1(
        "Soul Foods Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#333"
        }
    ),

    html.P(
        "Analyze Pink Morsel sales by region",
        style={"textAlign": "center"}
    ),

    # Radio Buttons
    html.Div([
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin": "10px"}
        )
    ], style={"textAlign": "center"}),

    # Graph
    dcc.Graph(id="sales-chart")

])

# -----------------------------
# Callback for filtering
# -----------------------------
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Aggregate
    filtered_df = filtered_df.groupby("date")["sales"].sum().reset_index()

    # Create figure
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Trend ({selected_region.capitalize()})"
    )

    # Add vertical line (safe version)
    fig.add_shape(
        type="line",
        x0="2021-01-15",
        x1="2021-01-15",
        y0=0,
        y1=1,
        xref="x",
        yref="paper",
        line=dict(color="red", dash="dash")
    )

    fig.add_annotation(
        x="2021-01-15",
        y=1,
        yref="paper",
        text="Price Increase",
        showarrow=False,
        yshift=10
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        title_x=0.5,
        plot_bgcolor="white"
    )

    return fig


# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)