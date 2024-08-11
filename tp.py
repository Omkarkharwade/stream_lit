import streamlit as st
import random
from datetime import datetime, timedelta

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

# Run the app
if __name__ == "__main__":
    logistics_app()




