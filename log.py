import streamlit as st
import random
from datetime import datetime, timedelta

# List of metro cities for random selection
metro_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad',
    'Ahmedabad', 'Pune', 'Jaipur', 'Surat'
]

# Function to generate random total price
def calculate_total_price(quantity):
    return random.randint(1000, 30000) * quantity

# Function to generate random expected delivery date within 5 days
def expected_delivery_date():
    return datetime.now() + timedelta(days=random.randint(1, 5))

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Sign In and Log In logic
def sign_in():
    st.title("Sign In")
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type='password')
    if st.button("Sign In"):
        st.session_state['username'] = username
        st.session_state['password'] = password
        st.success("Account created successfully! Please log in.")

def log_in():
    st.title("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Log In"):
        if username == st.session_state.get('username') and password == st.session_state.get('password'):
            st.success("Logged in successfully!")
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

# Product details entry page
def enter_product_details():
    st.title("Enter Product Details")
    product_name = st.text_input("Enter the product name")
    quantity = st.number_input("Enter the quantity of product", min_value=1, step=1)
    if quantity:
        total_price = calculate_total_price(quantity)
        st.write(f"Total Price: ₹{total_price}")
    address = st.text_area("Enter the delivery address")
    if product_name and quantity and address:
        st.success("Product details entered successfully!")

# Track order page
def track_order():
    st.title("Track Your Order")
    if st.button("Track My Order"):
        city = random.choice(metro_cities)
        delivery_date = expected_delivery_date().strftime('%Y-%m-%d')
        st.write(f"Your order is being shipped to {city}.")
        st.write(f"Expected Delivery Date: {delivery_date}")

# Thank You page
def thank_you():
    st.title("Thank You!")
    st.write("Thank you for ordering from our logistics service!")

# Main app flow
if not st.session_state['logged_in']:
    option = st.sidebar.selectbox("Choose Action", ["Sign In", "Log In"])
    if option == "Sign In":
        sign_in()
    elif option == "Log In":
        log_in()
else:
    page = st.sidebar.selectbox("Choose Action", ["Enter Product Details", "Track Order", "Thank You"])
    if page == "Enter Product Details":
        enter_product_details()
    elif page == "Track Order":
        track_order()
    elif page == "Thank You":
        thank_you()


