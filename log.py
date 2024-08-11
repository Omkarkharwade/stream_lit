import streamlit as st
import random
from datetime import datetime, timedelta
from streamlit_option_menu import option_menu

# Mock Lottie animation with a placeholder function
def st_lottie(*args, **kwargs):
    st.write("[Animation Placeholder]")

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

# Sidebar menu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    selected = option_menu(
        menu_title="Logistics App",  # Title for the menu
        options=["Sign In", "Log In"],  # Menu options
        icons=["person", "key"],  # Optional icons for each menu option
        orientation="horizontal",  # Horizontal layout
    )

    if selected == "Sign In":
        st.title("Sign In")
        username = st.text_input("Create Username")
        password = st.text_input("Create Password", type='password')
        if st.button("Sign In"):
            st.session_state['username'] = username
            st.session_state['password'] = password
            st.success("Account created successfully! Please log in.")
            st_lottie()  # Placeholder for animation

    elif selected == "Log In":
        st.title("Log In")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button("Log In"):
            if username == st.session_state.get('username') and password == st.session_state.get('password'):
                st.success("Logged in successfully!")
                st.session_state['logged_in'] = True
                st_lottie()  # Placeholder for animation
            else:
                st.error("Invalid username or password")
else:
    selected = option_menu(
        menu_title="Logistics App",  # Title for the menu
        options=["Enter Product Details", "Track Order", "Thank You"],  # Menu options
        icons=["cart", "map", "smiley"],  # Optional icons for each menu option
        orientation="horizontal",  # Horizontal layout
    )

    if selected == "Enter Product Details":
        st.title("Enter Product Details")

        # Step 1: Enter Product Name
        product_name = st.text_input("Enter the product name")

        # Step 2: Enter Quantity
        quantity = st.number_input("Enter the quantity of product", min_value=1, step=1)

        # Step 3: Calculate Total Price
        if quantity:
            total_price = calculate_total_price(quantity)
            st.write(f"Total Price: ₹{total_price}")

        # Step 4: Enter Delivery Address
        address = st.text_area("Enter the delivery address")

        if product_name and quantity and address:
            st.success("Product details entered successfully!")
            st_lottie()  # Placeholder for animation

    elif selected == "Track Order":
        st.title("Track Your Order")

        if st.button("Track My Order"):
            # Track My Order (Random Metro City)
            city = random.choice(metro_cities)
            delivery_date = expected_delivery_date().strftime('%Y-%m-%d')
            st.write(f"Your order is being shipped to {city}.")
            st.write(f"Expected Delivery Date: {delivery_date}")
            st_lottie()  # Placeholder for animation

    elif selected == "Thank You":
        st.title("Thank You!")
        st.write("Thank you for ordering from our logistics service!")
        st_lottie()  # Placeholder for animation

