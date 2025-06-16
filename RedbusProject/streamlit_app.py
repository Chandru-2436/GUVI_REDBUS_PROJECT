
import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Redbus Data Viewer", layout="wide")
st.title("🚌 Redbus Bus Route Explorer")

# Load data
conn = sqlite3.connect("bus_routes.db")
df = pd.read_sql_query("SELECT * FROM bus_routes", conn)

if df.empty:
    st.warning("No data found in the database. Run the scraper first.")
else:
    # Filters
    st.sidebar.header("🔍 Filter Buses")
    route = st.sidebar.selectbox("Select Route", options=sorted(df["route_name"].unique()))
    min_price, max_price = st.sidebar.slider("Price Range", 0, int(df["price"].max()), (0, int(df["price"].max())))
    min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 0.0, 0.5)
    min_seats = st.sidebar.slider("Minimum Seats Available", 0, int(df["seats_available"].max()), 0)

    # Apply filters
    filtered = df[
        (df["route_name"] == route) &
        (df["price"] >= min_price) &
        (df["price"] <= max_price) &
        (df["star_rating"] >= min_rating) &
        (df["seats_available"] >= min_seats)
    ]

    st.write(f"Showing results for **{route}**")
    st.dataframe(filtered)

conn.close()
