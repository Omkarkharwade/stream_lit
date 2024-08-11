import streamlit as st

# Apply Custom Theme via config.toml
st.set_page_config(
    page_title="Warehouse Inventory Management System",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App Title
st.title("Warehouse Inventory Management System")

# Sidebar for Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ['Dashboard', 'Transport Vehicles', 'Warehouse Equipment', 'Packaging Materials',
                                      'Tracking & Management Software', 'Logistics Services', 'Cargo Handling Equipment', 
                                      'Supply Chain Solutions'])

# Initialize a variable to store total cost
total_cost = 0

# Dashboard
if options == 'Dashboard':
    st.header("Dashboard")
    st.write("This is the dashboard with key metrics and insights.")
    # Add graphs, metrics, etc.

# Transport Vehicles Management
elif options == 'Transport Vehicles':
    st.header("Manage Transport Vehicles")
    
    with st.form(key='vehicle_form'):
        vehicle_type = st.selectbox("






