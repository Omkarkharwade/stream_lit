import streamlit as st
import random
from datetime import datetime

# Mock user data for authentication
user_data = {'username': 'user', 'password': 'pass'}

# List of metro cities in India
metro_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 
    'Ahmedabad', 'Pune', 'Jaipur', 'Surat', 'Lucknow', 'Kanpur'
]

# Animation for order placement
def show_animation():
    st.markdown(
        """
        <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        .pulse {
            animation: pulse 2s infinite;
            color: #ff4b2b;
            font-size: 30px;
        }
        </style>
        <div class="pulse">🎉 Thank You for Your Order! 🎉</div>
        """, unsafe_allow_html=True
    )

# Sign in page
def sign_in():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Sign In"):
        if username == user_data['username'] and password == user_data['password']:
            st.success("Signed in successfully!")
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password")

# Sign up page
def sign_up():
    st.title("Sign Up")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type='password')
    if st.button("Sign Up"):
        st.success("Sign up successful! Please sign in.")
        st.session_state['page'] = 'Sign In'

# Order page
def order_page():
    st.title("Product Order")
    
    product_name = st.text_input("Enter Product Name")
    quantity = st.number_input("Enter Quantity", min_value=1)
    
    if quantity > 0:
        price = random.randint(1000, 50000) * quantity
        st.write(f"Total Price: ₹{price}")
    
    city = st.selectbox("Where do you want to ship the product?", metro_cities)
    address = st.text_area("Enter Delivery Address")
    
    if st.button("Place Order"):
        st.success("Order placed successfully!")
        st.session_state['order_placed'] = True
        st.session_state['product_name'] = product_name
        st.session_state['quantity'] = quantity
        st.session_state['price'] = price
        st.session_state['city'] = city
        st.session_state['address'] = address

# Track order page
def track_order():
    st.title("Track My Product")
    
    if 'product_name' in st.session_state:
        st.write(f"Product Name: {st.session_state['product_name']}")
        st.write(f"Quantity: {st.session_state['quantity']}")
        st.write(f"Total Price: ₹{st.session_state['price']}")
        st.write(f"Shipping to: {st.session_state['city']}")
        st.write(f"Delivery Address: {st.session_state['address']}")
        
        current_city = random.choice(metro_cities)
        st.write(f"Current Location: {current_city}")
        
        show_animation()
    else:
        st.write("No order placed yet.")

# Main function
def main():
    st.sidebar.title("Navigation")
    
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Sign In'
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    page = st.sidebar.radio("Go to", ["Sign In", "Sign Up", "Order", "Track Order"])
    
    if page == "Sign In":
        sign_in()
    elif page == "Sign Up":
        sign_up()
    elif page == "Order":
        if st.session_state['logged_in']:
            order_page()
        else:
            st.error("Please sign in first.")
    elif page == "Track Order":
        if st.session_state.get('order_placed', False):
            track_order()
        else:
            st.error("No order to track.")

if __name__ == "__main__":
    main()
