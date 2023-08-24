# Dictionary for categories
categories = {
    1: {
        "id": 1,
        "name": "Gamer"
    },
    2: {
        "id": 2,
        "name": "Personal Care"
    },
    3: {
        "id": 3,
        "name": "Jewelry"
    }

}

# Dictionary of products
products = {
    1: {
        "id": 1,
        "name": "Mouse RGB 3600DPI",
        "price": 50,
        "catgory_id": 1
    },
    2: {
        "id": 2,
        "name": "Keyboard RGB",
        "price": 100,
        "catgory_id": 1
    },
    3: {
        "id": 3,
        "name": "Deodorant",
        "price": 20,
        "catgory_id": 2
    },
    4: {
        "id": 4,
        "name": "Coctail ring",
        "price": 280,
        "catgory_id": 3
    }
}

# Create a dictionary to store product names and their corresponding category names
product_category_mapping = {}

# Iterate through the products dictionary
for product_id, product_info in products.items():
    product_name = product_info["name"]
    category_id = product_info["catgory_id"]
    price = product_info["price"]
    id = product_info["id"]
    
    if category_id in categories:
        #add the product name and category name to the product_category_mapping dictionary
        product_category_mapping[id] = {
            "product": product_name,
            "category": categories[category_id]["name"],
            "price": price
        }


# Print the product_category_mapping dictionary
print(product_category_mapping)