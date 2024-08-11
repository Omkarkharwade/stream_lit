import streamlit as st
import random
from datetime import datetime, timedelta

# Mock Data for Random Generation
metro_cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 'Ahmedabad', 'Pune', 'Jaipur', 'Surat']

# HTML, CSS, and JavaScript for Sign In and Log In
sign_in_log_in_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logistics Web App</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4, #ffecd2, #fcb69f);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
        }

        .container {
            background: rgba(0, 0, 0, 0.5);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }

        h2 {
            margin-bottom: 20px;
            color: #ffecd2;
        }

        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: none;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            background-color: #ff6f61;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }

        button:hover {
            background-color: #ff3b30;
        }
    </style>
</head>
<body>

    <div class="container" id="signIn">
        <h2>Sign In</h2>
        <input type="text" id="signUpUsername" placeholder="Enter Username">
        <input type="password" id="signUpPassword" placeholder="Enter Password">
        <button onclick="signIn()">Sign In</button>
    </div>

    <div class="container" id="logIn" style="display:none;">
        <h2>Log In</h2>
        <input type="text" id="logInUsername" placeholder="Enter Username">
        <input type="password" id="logInPassword" placeholder="Enter Password">
        <button onclick="logIn()">Log In</button>
    </div>

    <script>
        function signIn() {
            const username = document.getElementById('signUpUsername').value;
            const password = document.getElementById('signUpPassword').value;

            if(username && password) {
                alert('Sign In Successful!');
                document.getElementById('signIn').style.display = 'none';
                document.getElementById('logIn').style.display = 'block';
            } else {
                alert('Please enter both username and password.');
            }
        }

        function logIn() {
            const username = document.getElementById('logInUsername').value;
            const password = document.getElementById('logInPassword').value;

            if(username && password) {
                alert('Log In Successful!');
                window.location.href = '#';  // Redirect to the logistics app page
                Streamlit.setComponentValue("logged_in");
            } else {
                alert('Please enter both username and password.');
            }
        }
    </script>
</body>
</html>
"""

# Streamlit Components for Sign In and Log In
def sign_in_log_in_component():
    st.components.v1.html(sign_in_log_in_html, height=600)

# Logistics App Functions
def logistics_app():
    st.title("Logistics Web App")
    st.markdown('<div style="text-align: center; color: #ff6347;"><h1>Place Your Order</h1></div>', unsafe_allow_html=True)

    # Enter Product Name
    product_name = st.text_input("Enter the product name")

    # Enter Quantity
    quantity = st.number_input("Enter the quantity of product", min_value=1, step=1)

    # Generate Random Price
    if quantity:
        total_price = random.randint(1000, 30000) * quantity
        st.write(f"Total Price for {quantity} units of {product_name} is ₹{total_price}")

    # Enter Address
    address = st.text_area("Enter the delivery address")

    # Track Order
    if st.button("Track My Order"):
        city = random.choice(metro_cities)
        delivery_date = datetime.now() + timedelta(days=random.randint(1, 5))
        st.write(f"Your order is being processed and will be delivered to {city} by {delivery_date.strftime('%Y-%m-%d')}")
        st.balloons()

    # Thank You Message
    if st.button("Thank You!"):
        st.markdown('<div style="text-align: center; font-size: 30px; color: #ff6347;">Thank you for ordering with us!</div>', unsafe_allow_html=True)

# Main Function to Control the App Flow
def main():
    if 'signed_in' not in st.session_state:
        st.session_state['signed_in'] = False
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['signed_in'] or not st.session_state['logged_in']:
        sign_in_log_in_component()
    else:
        logistics_app()

# Initialize Session State
if "component_state" not in st.session_state:
    st.session_state.component_state = ""

# Streamlit Communication for Log In
st.session_state.component_state = st.components.v1.html(
    sign_in_log_in_html,
    height=600,
    scrolling=True,
)

# Streamlit Check
if st.session_state.component_state == "logged_in":
    st.session_state['signed_in'] = True
    st.session_state['logged_in'] = True

main()



