import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# In-memory storage for users and orders (simulating a database)
if 'users' not in st.session_state:
    st.session_state['users'] = {}

if 'orders' not in st.session_state:
    st.session_state['orders'] = []

# Helper function to hash passwords (simplified)
def hash_password(password):
    return password[::-1]

# Generate random price for a product
def get_product_price(product_name):
    price_dict = {
        "Product A": random.randint(1000, 50000),
        "Product B": random.randint(1000, 50000),
        "Product C": random.randint(1000, 50000)
    }
    return price_dict.get(product_name, 0)

# Add custom CSS for styling
def add_custom_css():
    st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .main-title {
            color: #ff6f61;
            text-align: center;
            margin-bottom: 20px;
        }
        .section-title {
            color: #333;
            font-size: 24px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .stButton {
            background-color: #ff6f61;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton:hover {
            background-color: #ff3b30;
        }
        .input-text, .input-number, .input-area {
            margin-bottom: 15px;
            width: 100%;
        }
        .success-message {
            color: #28a745;
        }
        .error-message {
            color: #dc3545;
        }
    </style>
    """, unsafe_allow_html=True)

# Sign up page
def sign_up():
    st.title("Sign Up")
    st.markdown('<div class="main-title">Sign Up</div>', unsafe_allow_html=True)

    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    if st.button("Sign Up"):
        if username in st.session_state['users']:
            st.error("Username already exists. Please choose another one.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.session_state['users'][username] = hash_password(password)
            st.success("Sign-up successful! You can now log in.")
            st.session_state['signed_up'] = True

# Login page
def login():
    st.title("Log In")
    st.markdown('<div class="main-title">Log In</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Log In"):
        if username in st.session_state['users'] and st.session_state['users'][username] == hash_password(password):
            st.success("Logged in successfully!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Invalid username or password")

# Main menu page
def main_menu():
    st.sidebar.title(f"Welcome, {st.session_state['username']}")
    menu = ["Place Order", "Track Order", "Inventory", "Log Out"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    if choice == "Place Order":
        place_order()
    elif choice == "Track Order":
        track_order()
    elif choice == "Inventory":
        inventory()
    elif choice == "Log Out":
        st.session_state['logged_in'] = False
        st.sidebar.empty()

# Place order page
def place_order():
    st.title("Place Order")
    product_name = st.selectbox("Select Product", ["Product A", "Product B", "Product C"])
    quantity = st.number_input("Enter Quantity", min_value=1)
    
    price = get_product_price(product_name)
    total_price = price * quantity

    st.write(f"Price per unit: ₹{price}")
    st.write(f"Total Price: ₹{total_price}")

    if st.button("Place Order"):
        order = {
            'username': st.session_state['username'],
            'product': product_name,
            'quantity': quantity,
            'order_date': datetime.now(),
            'shipping_date': datetime.now() + timedelta(days=5),
            'status': 'Processing',
            'total_price': total_price
        }
        st.session_state['orders'].append(order)
        st.success("Order placed successfully!")
        
        # Display "Thank You" GIF
        st.image("https://media.giphy.com/media/3o6ZsT3tI60sNc4DdG/giphy.gif", caption="Thank You!", use_column_width=True)

# Track order page
def track_order():
    st.title("Track My Order")
    if len(st.session_state['orders']) == 0:
        st.write("No orders to track.")
        return
    
    for order in st.session_state['orders']:
        if order['username'] == st.session_state['username']:
            st.write(f"Order for {order['product']} ({order['quantity']} units)")
            st.write(f"Order Date: {order['order_date'].strftime('%Y-%m-%d')}")
            st.write(f"Shipping Date: {order['shipping_date'].strftime('%Y-%m-%d')}")
            st.write(f"Status: {order['status']}")
            st.write(f"Total Price: ₹{order['total_price']}")
            if datetime.now() > order['shipping_date']:
                order['status'] = 'Shipped'
            st.progress((datetime.now() - order['order_date']).days / 5 * 100)

            # Display tracking animation (optional)
            st.image("https://media.giphy.com/media/3o6ZsTxIj9b71H8PzK/giphy.gif", caption="Tracking Order", use_column_width=True)

# Inventory page
def inventory():
    st.title("Inventory")
    inventory_data = {
        "Product A": {"Quantity": 50, "Location": "Warehouse 1", "Price": get_product_price("Product A")},
        "Product B": {"Quantity": 30, "Location": "Warehouse 2", "Price": get_product_price("Product B")},
        "Product C": {"Quantity": 20, "Location": "Warehouse 3", "Price": get_product_price("Product C")},
    }
    
    df = pd.DataFrame.from_dict(inventory_data, orient='index')
    st.table(df)

# Main function
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if 'signed_up' not in st.session_state:
        st.session_state['signed_up'] = False

    if not st.session_state['logged_in']:
        if not st.session_state['signed_up']:
            sign_up()
        else:
            login()
    else:
        main_menu()

if __name__ == "__main__":
    add_custom_css()
    main()


