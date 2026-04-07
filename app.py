import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="NBA Arena Performance Dashboard",
    layout="wide"
)

st.title("NBA Arena Performance & Fan Experience Optimization")

# Load data
df = pd.read_csv("nba_arena_data.csv")

# Create metrics
df["attendance_rate"] = df["attendance"] / df["arena_capacity"]

df["win_flag"] = (
    df["team_score"] > df["opponent_score"]
).astype(int)

df["revenue_per_fan"] = (
    df["revenue_usd"] / df["attendance"]
)

# Sidebar filters
team = st.sidebar.selectbox(
    "Select Team",
    ["All"] + list(df["team"].unique())
)

if team != "All":
    df = df[df["team"] == team]

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Attendance",
    int(df["attendance"].mean())
)

col2.metric(
    "Attendance Rate",
    round(df["attendance_rate"].mean(), 2)
)

col3.metric(
    "Revenue per Fan",
    round(df["revenue_per_fan"].mean(), 2)
)

# Attendance trend
fig1 = px.line(
    df,
    x="date",
    y="attendance",
    title="Attendance Trend"
)

st.plotly_chart(fig1)

# Fan satisfaction vs attendance
fig2 = px.scatter(
    df,
    x="fan_satisfaction_score",
    y="attendance_rate",
    color="win_flag",
    title="Fan Satisfaction vs Attendance"
)

st.plotly_chart(fig2)

# Revenue analysis
fig3 = px.scatter(
    df,
    x="attendance",
    y="revenue_per_fan",
    title="Revenue per Fan"
)

st.plotly_chart(fig3)
