import streamlit as st

# Internal CSS for styling
st.markdown("""
    <style>
        .header {
            font-size: 40px;
            color: #4CAF50;
            text-align: center;
            margin-top: 50px;
        }
        .subheader {
            font-size: 20px;
            text-align: center;
            margin-top: 20px;
        }
        .button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            margin-top: 30px;
        }
        .dropdown {
            width: 50%;
            margin: auto;
        }
    </style>
    """, unsafe_allow_html=True)

# Crop data (sample data)
crops_data = {
    "Short-Term Crops": {
        "Tomato": {
            "How to farm": "Tomatoes require well-drained soil and plenty of sunlight.",
            "Pesticides": "Common pesticide for tomatoes includes Neem oil.",
            "Cultivation techniques": "Space plants 2 feet apart and water regularly.",
            "Insecticide": "Use organic insecticides like diatomaceous earth."
        },
        "Lettuce": {
            "How to farm": "Lettuce prefers cool weather and moist soil.",
            "Pesticides": "Insecticidal soap works well for lettuce.",
            "Cultivation techniques": "Plant lettuce in rows with sufficient spacing.",
            "Insecticide": "Use natural pest control like ladybugs."
        }
    },
    "Long-Term Crops": {
        "Wheat": {
            "How to farm": "Wheat needs fertile soil and moderate climate.",
            "Pesticides": "Use wheat-safe fungicides to prevent rust.",
            "Cultivation techniques": "Space rows 6 inches apart, irrigate moderately.",
            "Insecticide": "Pyrethrum-based insecticides can be used."
        },
        "Corn": {
            "How to farm": "Corn grows well in warm climates with rich soil.",
            "Pesticides": "Corn borer pesticides can protect against pests.",
            "Cultivation techniques": "Plant corn in rows with proper spacing.",
            "Insecticide": "Use Bacillus thuringiensis for organic control."
        }
    }
}


# Function to display the crop details page
def crop_details(crop_type, crop_name):
    crop = crops_data[crop_type][crop_name]
    st.subheader(f"Details for {crop_name} ({crop_type})")
    st.write("### How to Farm:")
    st.write(crop["How to farm"])
    st.write("### Pesticides:")
    st.write(crop["Pesticides"])
    st.write("### Cultivation Techniques:")
    st.write(crop["Cultivation techniques"])
    st.write("### Insecticides:")
    st.write(crop["Insecticide"])
    if st.button("Go Back"):
        st.session_state.page = 2


# Main function to control the flow of the app
def main():
    # Page 1: Welcome Page
    if 'page' not in st.session_state:
        st.session_state.page = 1

    if st.session_state.page == 1:
        st.markdown('<div class="header">Welcome to Farmers Helping App</div>', unsafe_allow_html=True)
        if st.button("Next"):
            st.session_state.page = 2

    # Page 2: Crop Selection Page
    elif st.session_state.page == 2:
        st.markdown('<div class="header">Select Crop Type</div>', unsafe_allow_html=True)
        crop_type = st.selectbox("Choose Crop Type", ["Short-Term Crops", "Long-Term Crops"], key="crop_type", index=0)
        if st.button("Next"):
            st.session_state.page = 3
            st.session_state.selected_crop_type = crop_type

    # Page 3: Crop List Page
    elif st.session_state.page == 3:
        st.markdown('<div class="header">Select a Crop</div>', unsafe_allow_html=True)
        crop_type = st.session_state.selected_crop_type
        crops = list(crops_data[crop_type].keys())
        crop_name = st.selectbox("Select Crop", crops, key="crop_name")

        if st.button("Show Details"):
            st.session_state.page = 4
            st.session_state.selected_crop_name = crop_name

        if st.button("Go Back"):
            st.session_state.page = 2

    # Page 4: Crop Details Page
    elif st.session_state.page == 4:
        crop_type = st.session_state.selected_crop_type
        crop_name = st.session_state.selected_crop_name
        crop_details(crop_type, crop_name)


if __name__ == "__main__":
    main()
