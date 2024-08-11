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

# CSS Styling
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

# Function to handle the sign-up page
def sign_up_page():
    st.title("Sign Up", anchor=None)
    st.markdown('<div class="main-title">Sign Up</div>', unsafe_allow_html=True)

    username = st.text_input("Choose a username", key="signup_username", help="Enter a unique username")
    password = st.text_input("Choose a password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm password", type="password", key="confirm_password")

    if st.button("Sign Up", key="signup_button"):
        if username and password and confirm_password:
            if password == confirm_password:
                if username not in st.session_state.USER_CREDENTIALS:
                    st.session_state.USER_CREDENTIALS[username] = password
                    st.markdown('<div class="success-message">Account created successfully! You can now log in.</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="error-message">Username already exists.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-message">Passwords do not match.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-message">Please fill in all fields.</div>', unsafe_allow_html=True)

# Function to handle the log-in page
def log_in_page():
    st.title("Log In", anchor=None)
    st.markdown('<div class="main-title">Log In</div>', unsafe_allow_html=True)

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In", key="login_button"):
        if username and password:
            if st.session_state.USER_CREDENTIALS.get(username) == password:
                st.session_state.authenticated = True
                st.markdown('<div class="success-message">Logged in successfully!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-message">Invalid username or password</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-message">Please enter both username and password</div>', unsafe_allow_html=True)

# Function to display the logistics app
def logistics_app():
    st.title("Logistics Web App", anchor=None)
    st.markdown('<div class="main-title">Logistics Web App</div>', unsafe_allow_html=True)

    # Step 1: Enter Product Name
    product_name = st.text_input("Enter the product name", key="product_name", help="Name of the product")

    # Step 2: Enter Quantity
    quantity = st.number_input("Enter the quantity of product", min_value=1, step=1, key="quantity")

    # Step 3: Calculate Total Price
    if quantity:
        total_price = calculate_total_price(quantity)
        st.write(f"Total Price: ₹{total_price}")

    # Step 4: Enter Delivery Address
    address = st.text_area("Enter the delivery address", key="address")

    # Step 5: Track My Order (Random Metro City)
    if st.button("Track My Order", key="track_button"):
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

    add_custom_css()

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
