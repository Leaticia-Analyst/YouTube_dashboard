import streamlit as st
import pandas as pd

# ===== LOGIN SYSTEM =====
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state["logged_in"] = True
        else:
            st.error("❌ Wrong username or password")

# Initialize session
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# If NOT logged in → show login page
if not st.session_state["logged_in"]:
    login()
    st.stop()

# ===== DASHBOARD STARTS HERE =====

# Page config
st.set_page_config(page_title="YouTube Dashboard", layout="wide")

# Logout button
if st.sidebar.button("Logout"):
    st.session_state["logged_in"] = False
    st.rerun()

# Load data
df = pd.read_csv("data2.csv")

# Sidebar
st.sidebar.title("📊 Dashboard Settings")

category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

filtered_df = df[df["Category"] == category]

# Title
st.title("🚀 YouTube Analytics Dashboard")

# KPIs
st.subheader("📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Videos", len(filtered_df))
col2.metric("Total Views", filtered_df["Views"].sum())
col3.metric("Total Likes", filtered_df["Likes"].sum())

# Charts
st.subheader("📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    st.write("Views per Video")
    st.bar_chart(filtered_df.set_index("Name")["Views"])

with col2:
    st.write("Likes per Video")
    st.line_chart(filtered_df.set_index("Name")["Likes"])

# Table
st.subheader("📋 Data Table")
st.dataframe(filtered_df)