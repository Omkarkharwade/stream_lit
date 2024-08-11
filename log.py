import streamlit as st
import random
from datetime import datetime, timedelta
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animations
success_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
track_animation = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_ni4sqkmd.json")

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
selected = option_menu(
    menu_title=None,  # required
    options=["Sign In", "Log In", "Enter Product Details", "Track Order", "Thank You"],  # required
    icons=["person", "key", "cart", "map", "smiley"],  # optional
    orientation="horizontal",
)

if selected == "Sign In":
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Sign In"):
        st.success("Signed in successfully!")
        st_lottie(success_animation, height=300, key="success1")

elif selected == "Log In":
    st.title("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Log In"):
        st.success("Logged in successfully!")
        st_lottie(success_animation, height=300, key="success2")

elif selected == "Enter Product Details":
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
        st_lottie(success_animation, height=300, key="success3")

elif selected == "Track Order":
    st.title("Track Your Order")

    if st.button("Track My Order"):
        # Track My Order (Random Metro City)
        city = random.choice(metro_cities)
        delivery_date = expected_delivery_date().strftime('%Y-%m-%d')
        st.write(f"Your order is being shipped to {city}.")
        st.write(f"Expected Delivery Date: {delivery_date}")
        st_lottie(track_animation, height=300, key="track1")

elif selected == "Thank You":
    st.title("Thank You!")
    st.write("Thank you for ordering from our logistics service!")
    st_lottie(success_animation, height=300, key="thankyou")
