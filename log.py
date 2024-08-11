import streamlit as st

# Define a function for the sign-in page
def sign_in_page():
    st.title("Sign In")
    st.markdown('<style>body{background-color: red;}</style>', unsafe_allow_html=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if username and password:
            st.success("Signed in successfully!")
            # Add logic to check credentials and redirect to the main page
        else:
            st.error("Please enter both username and password")

# Define a function for the log-in page
def log_in_page():
    st.title("Log In")
    st.markdown('<style>body{background-color: red;}</style>', unsafe_allow_html=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if username and password:
            st.success("Logged in successfully!")
            # Add logic to check credentials and redirect to the main page
        else:
            st.error("Please enter both username and password")

# Main page selector
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", ["Sign In", "Log In"])

    if page == "Sign In":
        sign_in_page()
    elif page == "Log In":
        log_in_page()

if __name__ == "__main__":
    main()



