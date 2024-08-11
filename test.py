
import streamlit as st

# Function to handle the sign-up page
def sign_up_page():
    st.title("Sign Up Page")
    
    # Input fields for sign-up
    new_username = st.text_input("Create Username")
    new_password = st.text_input("Create Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    
    # Validation and submission
    if st.button("Sign Up"):
        if new_password == confirm_password:
            if new_username and new_password:
                # Save the new user data (For demo purposes, just showing a success message)
                st.session_state.user_data[new_username] = new_password
                st.success("Account created successfully! You can now log in.")
                st.session_state.current_page = "Login"
            else:
                st.error("Please enter both username and password.")
        else:
            st.error("Passwords do not match.")

# Function to handle the login page
def login_page():
    st.title("Login Page")
    
    # Input fields for login
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    # Validation and submission
    if st.button("Login"):
        if username in st.session_state.user_data:
            if st.session_state.user_data[username] == password:
                st.session_state.logged_in = True
                st.session_state.current_page = "Dashboard"
                st.success("Logged in successfully!")
            else:
                st.error("Incorrect password.")
        else:
            st.error("Username not found.")

# Dashboard or home page after logging in
def dashboard_page():
    st.title("Dashboard")
    st.write("Welcome to the dashboard! You are now logged in.")

# Main function to handle page navigation
def main():
    # Initialize session state variables
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Login"

    # Navigation logic
    if st.session_state.current_page == "Login":
        login_page()
        if st.session_state.logged_in:
            st.session_state.current_page = "Dashboard"
    elif st.session_state.current_page == "Sign Up":
        sign_up_page()
    elif st.session_state.current_page == "Dashboard":
        dashboard_page()
    else:
        st.write("Page not found.")

    # Navigation between pages
    if not st.session_state.logged_in:
        if st.session_state.current_page == "Login":
            if st.button("Go to Sign Up"):
                st.session_state.current_page = "Sign Up"
        elif st.session_state.current_page == "Sign Up":
            if st.button("Back to Login"):
                st.session_state.current_page = "Login"

if __name__ == "__main__":
    main()
