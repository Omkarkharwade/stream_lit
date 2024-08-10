import streamlit as st

# Set the title of the Streamlit app
st.title("Food Budget Planner")

# Input the monthly income
income = st.number_input("Enter your monthly income (INR):", min_value=0)

# Input budget allocation for different food categories
st.subheader("Allocate your budget to different food categories (in %):")

groceries = st.slider("Groceries", 0, 100, 40)
eating_out = st.slider("Eating Out", 0, 100, 20)
snacks = st.slider("Snacks", 0, 100, 10)
beverages = st.slider("Beverages", 0, 100, 10)

# Calculate the total allocation
total_allocation = groceries + eating_out + snacks + beverages

# Display a warning if the total allocation exceeds 100%
if total_allocation > 100:
    st.warning("Your total allocation exceeds 100%. Please adjust the percentages.")
elif total_allocation < 100:
    st.info(f"You have {100 - total_allocation}% of your budget unallocated.")
else:
    # Calculate the budget for each category
    groceries_budget = income * (groceries / 100)
    eating_out_budget = income * (eating_out / 100)
    snacks_budget = income * (snacks / 100)
    beverages_budget = income * (beverages / 100)

    # Display the budget allocation
    st.subheader("Your Food Budget:")
    st.write(f"Groceries: ₹{groceries_budget:.2f}")
    st.write(f"Eating Out: ₹{eating_out_budget:.2f}")
    st.write(f"Snacks: ₹{snacks_budget:.2f}")
    st.write(f"Beverages: ₹{beverages_budget:.2f}")

# Display the total budget
st.subheader("Total Budget Allocation:")
st.write(f"Total: ₹{income:.2f}")
