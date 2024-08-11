import streamlit as st
import random

# Initialize session state variables
if 'users' not in st.session_state:
    st.session_state['users'] = {'user': 'pass'}  # Pre-defined user
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = 'Sign In'
if 'order_placed' not in st.session_state:
    st.session_state['order_placed'] = False

# List of metro cities in India
metro_cities = [
    'Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 
    'Ahmedabad', 'Pune', 'Jaipur', 'Surat', 'Lucknow', 'Kanpur'
]

# Sign in page
def sign_in():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Sign In"):
        if username in st.session_state['users'] and st.session_state['users'][username] == password:
            st.success("Signed in successfully!")
            st.session_state['logged_in'] = True
            st.session_state['page'] = 'Order'
        else:
            st.error("Invalid username or password")

# Sign up page
def sign_up():
    st.title("Sign Up")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type='password')
    
    if st.button("Sign Up"):
        if username in st.session_state['users']:
            st.error("Username already exists! Please choose a different username.")
        else:
            st.session_state['users'][username] = password
            st.success("Sign up successful! Please sign in.")
            st.session_state['page'] = 'Sign In'

# Order page with colorful background animation
def order_page():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(90deg, rgba(255,0,150,0.1), rgba(0,229,255,0.1));
            animation: gradient 5s infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("Product Order")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        product_name = st.text_input("Enter Product Name")
    
    with col2:
        quantity = st.number_input("Enter Quantity", min_value=1)
    
    with col3:
        if quantity > 0:
            price = random.randint(1000, 30000) * quantity
            st.write(f"Total Price: ₹{price}")
    
    address = st.text_area("Enter Delivery Address")
    
    if st.button("Place Order"):
        st.success("Order placed successfully!")
        st.session_state['order_placed'] = True
        st.session_state['product_name'] = product_name
        st.session_state['quantity'] = quantity
        st.session_state['price'] = price
        st.session_state['address'] = address
        st.session_state['city'] = random.choice(metro_cities)

# Track order and thank you message
def track_order():
    if st.session_state['order_placed']:
        st.write(f"Product Name: {st.session_state['product_name']}")
        st.write(f"Quantity: {st.session_state['quantity']}")
        st.write(f"Total Price: ₹{st.session_state['price']}")
        st.write(f"Shipping to: {st.session_state['city']}")
        st.write(f"Delivery Address: {st.session_state['address']}")
        
        st.markdown(
            "<h1 style='text-align: center; color: green;'>Thank You for Ordering from Our Logistics!</h1>",
            unsafe_allow_html=True
        )
    else:
        st.error("No order placed yet.")

# Main function
def main():
    st.sidebar.title("Navigation")
    
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
        if st.session_state['order_placed']:
            track_order()
        else:
            st.error("No order to track.")

if __name__ == "__main__":
    main()


