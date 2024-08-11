import streamlit as st
import random
from datetime import datetime, timedelta

# In-memory user storage for demonstration purposes
if "USER_CREDENTIALS" not in st.session_state:
    st.session_state.USER_CREDENTIALS = {}

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

# Function to handle the sign-up page
def sign_up_page():
    st.title("Sign Up")
    st.markdown('<style>body{background-color: red;}</style>', unsafe_allow_html=True)

    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    if st.button("Sign Up"):
        if username and password and confirm_password:
            if password == confirm_password:
                if username not in st.session_state.USER_CREDENTIALS:
                    st.session_state.USER_CREDENTIALS[username] = password
                    st.success("Account created successfully! You can now log in.")
                else:
                    st.error("Username already exists.")
            else:
                st.error("Passwords do not match.")
        else:
            st.error("Please fill in all fields.")

# Function to handle the log-in page
def log_in_page():
    st.title("Log In")
    st.markdown('<style>body{background-color: red;}</style>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if username and password:
            if st.session_state.USER_CREDENTIALS.get(username) == password:
                st.session_state.authenticated = True
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")
        else:
            st.error("Please enter both username and password")

# Function to display the logistics app
def logistics_app():
    st.title("Logistics Web App")

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

    # Step 5: Track My Order (Random Metro City)
    if st.button("Track My Order"):
        if product_name and quantity and address:
            city = random.choice(metro_cities)
            delivery_date = expected_delivery_date().strftime('%Y-%m-%d')
            st.write(f"Your order is being shipped to {city}.")
            st.write(f"Expected Delivery Date: {delivery_date}")

            # Step 6: Thank You Message
            st.success("Thank you for ordering from our logistics service!")

        else:
            st.error("Please fill in all the details.")

# Main page selector
def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        logistics_app()
    else:
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Choose a page", ["Sign Up", "Log In"])

        if page == "Sign Up":
            sign_up_page()
        elif page == "Log In":
            log_in_page()

if __name__ == "__main__":
    main()





