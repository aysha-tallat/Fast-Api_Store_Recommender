import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
df = pd.read_excel("superstore.xlsx", engine="openpyxl")

# Subset relevant columns
df = df[['Customer Name', 'Sub-Category', 'Sales']]

# Pivot: rows = customers, columns = sub-categories, values = sales
pivot_df = df.pivot_table(index='Customer Name', columns='Sub-Category', values='Sales', aggfunc='sum', fill_value=0)

# Transpose: now rows = products, columns = customers
product_matrix = pivot_df.T

# Compute cosine similarity between products
similarity_matrix = pd.DataFrame(cosine_similarity(product_matrix), 
                                 index=product_matrix.index, 
                                 columns=product_matrix.index)

def recommend_products(selected_product, top_n=3):
    if selected_product not in similarity_matrix.columns:
        return f"Product '{selected_product}' not found in dataset."
    
    similar_items = similarity_matrix[selected_product].sort_values(ascending=False)
    recommendations = similar_items.iloc[1:top_n+1].index.tolist()
    return recommendations

# Example usage
if __name__ == "__main__":
    item = "Binders"  # Replace with any Sub-Category from your dataset
    print(f"Recommendations for '{item}': {recommend_products(item)}")


def get_all_products():
    return similarity_matrix.columns.tolist()

