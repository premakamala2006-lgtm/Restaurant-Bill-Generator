import streamlit as st
from menu import menu
from model import predict_order

st.set_page_config(page_title="ML Order Prediction", layout="centered")
st.markdown("""
<style>
.stApp {
    background-image: url("https://www.gsghome.com/wp-content/uploads/2020/03/blurry-restaurant-menu.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container {
    background-color: rgba(0,0,0,0.6);
    padding: 20px;
    border-radius: 10px;
}

h1, h2, h3, h4, p, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🍽 ML-Based Order Prediction System")

st.write("Select items to place your order:")

selected_items = []

# UI for selecting items
for item, price in menu.items():
    if st.checkbox(f"{item} (₹{price})"):
        selected_items.append(item)

# Show selected items
if selected_items:
    st.subheader("🛒 Your Order")
    total = 0

    for item in selected_items:
        st.write(f"{item} - ₹{menu[item]}")
        total += menu[item]

    st.success(f"Total Bill: ₹{total}")

    # ML Prediction
    st.subheader("🤖 Recommended Items (ML Prediction)")
    recommendations = predict_order(selected_items)

    if recommendations:
        for item in recommendations:
            st.write(f"👉 {item}")
    else:
        st.write("No recommendations found")

else:
    st.warning("Please select at least one item")