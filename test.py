import streamlit as st
import random
from datetime import datetime, timedelta
import time

# Initial data for shipments
shipments = {
    'Shipment A': {'quantity': 50, 'shipping_date': datetime.now() + timedelta(days=5), 'delivery_date': datetime.now() + timedelta(days=30)},
    'Shipment B': {'quantity': 20, 'shipping_date': datetime.now() + timedelta(days=3), 'delivery_date': datetime.now() + timedelta(days=15)},
    'Shipment C': {'quantity': 100, 'shipping_date': datetime.now() + timedelta(days=7), 'delivery_date': datetime.now() + timedelta(days=45)},
}

# Mock user data
user_data = {'username': 'admin', 'password': 'admin'}

# List of metro cities in India
metro_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 
    'Ahmedabad', 'Pune', 'Jaipur', 'Surat', 'Lucknow', 'Kanpur'
]

# Add a new product with a random price
def add_product():
    st.title("Add New Product")
    product_name = st.text_input("Product Name")
    if st.button("Add Product"):
        if product_name:
            price = random.randint(1000, 50000)
            shipments[product_name] = {
                'quantity': random.randint(10, 100),
                'price': price,
                'shipping_date': datetime.now() + timedelta(days=random.randint(1, 10)),
                'delivery_date': datetime.now() + timedelta(days=random.randint(20, 50))
            }
            st.success(f"Product '{product_name}' added with price {price} successfully!")
        else:
            st.error("Product name cannot be empty")

# Sign up page
def sign_up():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    if st.button("Sign Up"):
        if password == confirm_password:
            st.session_state['username'] = username
            st.session_state['password'] = password
            st.success("Sign Up successful! Please log in.")
            st.session_state['page'] = 'login'
        else:
            st.error("Passwords do not match")

# Login page
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if username == st.session_state.get('username') and password == st.session_state.get('password'):
            st.success("Logged in successfully!")
            st.session_state['logged_in'] = True
            st.session_state['page'] = 'dashboard'
        else:
            st.error("Invalid username or password")

# Dashboard page
def dashboard():
    st.title("Logistics Dashboard")
    action = st.selectbox("Select Action", ["Track Shipment", "Manage Inventory", "Check Delivery Status", "Add Product"])
    
    if action == "Track Shipment":
        track_shipment()
    elif action == "Manage Inventory":
        manage_inventory()
    elif action == "Check Delivery Status":
        check_delivery_status()
    elif action == "Add Product":
        add_product()

# Track shipment page
def track_shipment():
    shipment_name = st.selectbox("Select Shipment", list(shipments.keys()))
    shipment = shipments[shipment_name]
    
    # Randomly select a metro city
    city = random.choice(metro_cities)
    
    st.write(f"Order Date: {datetime.now().strftime('%Y-%m-%d')}")
    st.write(f"Shipping Status: {'Shipped' if datetime.now() > shipment['shipping_date'] else 'Pending'}")
    st.write(f"Current Location: {city}")
    
    days_since_shipping = (datetime.now() - shipment['shipping_date']).days
    shipping_duration = (shipment['delivery_date'] - shipment['shipping_date']).days
    progress = min(max(days_since_shipping / shipping_duration * 100, 0), 100)
    st.progress(progress)

# Manage inventory page
def manage_inventory():
    shipment_name = st.selectbox("Select Shipment", list(shipments.keys()))
    shipment = shipments[shipment_name]
    st.write(f"Shipment: {shipment_name}")
    st.write(f"Quantity Available: {shipment['quantity']}")
    
    quantity_to_order = st.number_input("Enter Quantity to Order", min_value=1, max_value=shipment['quantity'])
    if st.button("Update Inventory"):
        update_inventory(shipment_name, quantity_to_order)

# Update inventory page
def update_inventory(shipment_name, quantity_to_order):
    shipment = shipments[shipment_name]
    
    if quantity_to_order > shipment['quantity']:
        st.error("Order quantity exceeds available inventory!")
    else:
        shipment['quantity'] -= quantity_to_order
        st.write(f"Inventory updated: {quantity_to_order} units of {shipment_name} processed successfully!")
        
        # Show order placed confirmation with a "Thank you" animation
        st.balloons()
        
        # Display order confirmation message
        st.success("Your order has been placed successfully!")
        st.write("Thank you for your order!")

# Check delivery status page
def check_delivery_status():
    shipment_name = st.selectbox("Select Shipment", list(shipments.keys()))
    shipment = shipments[shipment_name]
    if datetime.now() > shipment['delivery_date']:
        st.error("Shipment has been delivered!")
        if st.button("Record Delivery"):
            st.write("Delivery recorded successfully!")
    else:
        st.write(f"Expected Delivery Date: {shipment['delivery_date'].strftime('%Y-%m-%d')}")

# Main function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'page' not in st.session_state:
        st.session_state['page'] = 'signup'

    if not st.session_state['logged_in']:
        if st.session_state['page'] == 'signup':
            sign_up()
        elif st.session_state['page'] == 'login':
            login()
    else:
        st.sidebar.title("Menu")
        menu = ["Dashboard", "Logout"]
        choice = st.sidebar.selectbox("Choose Option", menu)

        if choice == "Dashboard":
            dashboard()
        elif choice == "Logout":
            st.session_state['logged_in'] = False
            st.session_state['page'] = 'login'
            st.write("Logged out successfully!")

if __name__ == "__main__":
    main()




