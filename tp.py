import streamlit as st
import random
from datetime import datetime, timedelta

# Mock user data
user_data = {'username': 'admin', 'password': 'admin'}

# List of metro cities in India
metro_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 
    'Ahmedabad', 'Pune', 'Jaipur', 'Surat', 'Lucknow', 'Kanpur'
]

# Set background style
st.markdown(
    """
    <style>
    body {
        background-image: url('https://your-logistics-themed-background-image-url');
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True
)

# Add a new product with a random price
def add_product():
    st.title("Add New Product")
    product_name = st.text_input("Product Name")
    if st.button("Add Product"):
        if product_name:
            price = random.randint(1000, 50000)
            st.session_state['product'] = {
                'name': product_name,
                'price': price,
                'quantity': random.randint(10, 100),
                'shipping_date': datetime.now() + timedelta(days=random.randint(1, 10)),
                'delivery_date': datetime.now() + timedelta(days=random.randint(20, 50)),
                'location': random.choice(metro_cities)
            }
            st.success(f"Product '{product_name}' added with price ₹{price} successfully!")
            st.session_state['page'] = 'track_order'
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
    action = st.selectbox("Select Action", ["Place Order", "Track Shipment", "Logout"])
    
    if action == "Place Order":
        add_product()
    elif action == "Track Shipment":
        track_shipment()
    elif action == "Logout":
        st.session_state['logged_in'] = False
        st.session_state['page'] = 'login'
        st.write("Logged out successfully!")

# Track shipment page
def track_shipment():
    st.title("Track My Order")
    product = st.session_state['product']
    
    if product:
        st.write(f"Product Name: {product['name']}")
        st.write(f"Price: ₹{product['price']}")
        st.write(f"Quantity Ordered: {product['quantity']}")
        st.write(f"Current Location: {product['location']}")
        
        days_since_shipping = (datetime.now() - product['shipping_date']).days
        shipping_duration = (product['delivery_date'] - product['shipping_date']).days
        progress = min(max(days_since_shipping / shipping_duration * 100, 0), 100)
        st.progress(progress)
        
        if st.button("Place Another Order"):
            st.session_state['page'] = 'dashboard'
        else:
            st.balloons()
            st.success("Your order has been tracked successfully!")
            st.write("Thank you for using our logistics service!")
    else:
        st.error("No order to track. Please place an order first.")

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
        dashboard()

if __name__ == "__main__":
    main()
