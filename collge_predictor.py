import streamlit as st

# Sample data for demonstration. Replace this with actual data.
college_data = {
    "College A": 98.5,
    "College B": 95.0,
    "College C": 90.0,
    "College D": 85.0,
    "College E": 80.0,
}

def predict_college(percentile):
    possible_colleges = []
    for college, cutoff in college_data.items():
        if percentile >= cutoff:
            possible_colleges.append(college)
    return possible_colleges

def main():
    st.title("MHT-CET College Predictor")
    
    percentile = st.slider("Enter your MHT-CET Percentile", 0.0, 100.0, 50.0)
    
    if st.button("Predict Colleges"):
        colleges = predict_college(percentile)
        if colleges:
            st.success("Based on your percentile, you may get into the following colleges:")
            for college in colleges:
                st.write(f"- {college}")
        else:
            st.warning("Your percentile may not meet the cutoff for any listed colleges.")

if __name__ == "__main__":
    main()
