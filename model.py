import pandas as pd
from sklearn.neighbors import NearestNeighbors
from data import orders

# Get all unique items
all_items = list(set(item for order in orders for item in order))

# Convert orders to binary matrix
def create_matrix(orders, items):
    matrix = []
    for order in orders:
        row = [1 if item in order else 0 for item in items]
        matrix.append(row)
    return pd.DataFrame(matrix, columns=items)

df = create_matrix(orders, all_items)

# Train model
model = NearestNeighbors(metric='cosine')
model.fit(df)

# Recommendation function
def predict_order(selected_items):
    if not selected_items:
        return []

    input_vec = [1 if item in selected_items else 0 for item in all_items]

    distances, indices = model.kneighbors([input_vec], n_neighbors=2)

    nearest_order = df.iloc[indices[0][1]]

    recommendations = [
        item for item in all_items
        if nearest_order[item] == 1 and item not in selected_items
    ]

    return recommendationsst.markdown("""
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