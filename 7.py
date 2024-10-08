import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

# In-memory storage for users and orders (simulating a database)
if 'users' not in st.session_state:
    st.session_state['users'] = {}

if 'orders' not in st.session_state:
    st.session_state['orders'] = []

if 'products' not in st.session_state:
    st.session_state['products'] = {}

# Helper function to hash passwords (simplified)
def hash_password(password):
    return password[::-1]

# Generate random price for a product
def get_product_price(product_name):
    # Return price of a custom product if it exists
    product_info = st.session_state['products'].get(product_name)
    return product_info['price'] if product_info else random.randint(1000, 50000)

# Add custom CSS with animations
def add_custom_css():
    st.markdown("""
    <style>
        body {
            background-color: #e0f7fa; /* Light blue background */
            font-family: Arial, sans-serif;
        }
        .main-title {
            color: #00796b; /* Dark teal color */
            text-align: center;
            margin-bottom: 20px;
        }
        .section-title {
            color: #004d40; /* Even darker teal color */
            font-size: 24px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .stButton {
            background-color: #00796b;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton:hover {
            background-color: #004d40;
        }
        .input-text, .input-number, .input-area {
            margin-bottom: 15px;
            width: 100%;
        }
        .success-message {
            color: #004d40;
            font-size: 18px;
            animation: fadeIn 2s ease-in-out;
        }
        .thank-you {
            text-align: center;
            font-size: 24px;
            color: #00796b;
            animation: bounceIn 2s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes bounceIn {
            0% { opacity: 0; transform: scale(0.3); }
            50% { opacity: 1; transform: scale(1.05); }
            100% { opacity: 1; transform: scale(1); }
        }
    </style>
    """, unsafe_allow_html=True)

# Sign up page
def sign_up():
    st.title("Sign Up")
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
    product_name = st.text_input("Enter Product Name")
    quantity = st.number_input("Enter Quantity", min_value=1)
    
    if product_name:
        # Generate or retrieve the product price
        price = get_product_price(product_name)
        total_price = price * quantity

        st.write(f"Price per unit: ₹{price}")
        st.write(f"Total Price: ₹{total_price}")

        if st.button("Place Order"):
            # Generate a random shipping date between 1 and 5 days
            shipping_days = random.randint(1, 5)
            shipping_date = datetime.now() + timedelta(days=shipping_days)
            
            # Randomly select the status
            status = random.choice(['Packaging Started', 'Packaging Not Started'])

            order = {
                'username': st.session_state['username'],
                'product': product_name,
                'quantity': quantity,
                'order_date': datetime.now(),
                'shipping_date': shipping_date,
                'status': status,
                'total_price': total_price
            }
            st.session_state['orders'].append(order)

            # Update the products in session state
            if product_name in st.session_state['products']:
                st.session_state['products'][product_name]['quantity'] += quantity
            else:
                st.session_state['products'][product_name] = {'price': price, 'quantity': quantity}

            st.success("Order placed successfully!")

            # Display thank you message with animation
            st.markdown('<div class="thank-you">Thank You for Your Order!</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a product name.")

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

# Inventory page
def inventory():
    st.title("Inventory")
    # Use session state to reflect current products
    inventory_data = st.session_state['products']
    
    if not inventory_data:
        st.write("No products available in inventory.")
        return

    # Prepare data for DataFrame
    data = []
    for product, details in inventory_data.items():
        total_price = details['price'] * details['quantity']
        data.append([product, details['price'], details['quantity'], total_price])

    df = pd.DataFrame(data, columns=['Product Name', 'Price', 'Quantity', 'Total Price'])

    # Add a numerical index starting from 1
    df.index += 1

    # Calculate total price of all products
    overall_total_amount = df['Total Price'].sum()
    
    # Display the DataFrame and the total price
    st.table(df)
    st.write(f"Total Amount of All Products: ₹{overall_total_amount:.2f}")

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
