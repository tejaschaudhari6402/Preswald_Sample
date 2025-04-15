from preswald import connect, get_df, query, table, text, slider, dropdown, plotly, sidebar
import plotly.express as px


connect()
df = get_df("deliveries")


sidebar("IPL Analysis Dashboard", content="Explore IPL deliveries data with interactive controls!"

text("# IPL Deliveries Analysis App")


sql = "SELECT match_id, inning, batting_team, batsman, total_runs FROM deliveries WHERE total_runs > 4"
filtered_df = query(sql, "deliveries")
table(filtered_df, title="High-Scoring Deliveries (Runs > 4)")


threshold = slider("Runs Threshold", min_val=0, max_val=6, default=4)
dynamic_df = df[df["total_runs"] > threshold]
table(dynamic_df, title=f"Deliveries with Runs > {threshold}"

teams = df["batting_team"].unique().tolist()
selected_team = dropdown("Select Batting Team", options=teams, default=teams[0])
team_df = df[df["batting_team"] == selected_team]
table(team_df, title=f"Deliveries by {selected_team}")


fig = px.scatter(
    df,
    x="over",
    y="total_runs",
    color="batting_team",
    title="Runs Scored per Over by Batting Team",
    labels={"over": "Over Number", "total_runs": "Runs Scored"}
)
plotly(fig)