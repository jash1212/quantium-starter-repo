import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df = df.groupby("date")["sales"].sum().reset_index()

fig = px.line(df, x="date", y="sales", title="Sales of Pink Morsels Over Time")

# ✅ SAFE vertical line
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
    title_x=0.5
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Dashboard", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)