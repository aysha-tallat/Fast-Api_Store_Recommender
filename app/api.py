from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from main import recommend_products, get_all_products



app = FastAPI(title="Store Recommender API",
              description="Please select a product from the following list ",
              version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Store Recommender API"}


product_list = [
    'Bookcases', 'Chairs', 'Labels', 'Tables', 'Storage', 'Furnishings', 'Art',
    'Phones', 'Binders', 'Appliances', 'Paper', 'Accessories', 'Envelopes',
    'Fasteners', 'Supplies', 'Machines', 'Copiers'
]

@app.get("/recommend")
def get_recommendations(
    item: str = Query(
        ..., 
        description=f"Select a product from: {', '.join(product_list)}"
    )
):
    recommendations = recommend_products(item)
    return JSONResponse(content={"selected": item, "recommendations": recommendations})


