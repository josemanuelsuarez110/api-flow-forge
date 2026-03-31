from datetime import datetime
from app.utils import get_logger

logger = get_logger("transform")

def transform_product(product):
    """Applies transformations to a single product record."""
    try:
        # 1. Basic Cleaning
        pid = product.get("id")
        title = product.get("title", "Unknown").strip()
        brand = product.get("brand", "N/A").strip()
        category = product.get("category", "Uncategorized").lower()
        
        # 2. Numerical Normalization
        price = float(product.get("price", 0.0))
        discount_percentage = float(product.get("discountPercentage", 0.0))
        stock = int(product.get("stock", 0))
        rating = float(product.get("rating", 0.0))
        
        # 3. Feature Engineering
        # Calculate stock value
        stock_value = round(price * stock, 2)
        
        # Calculate discounted price
        discount_amount = (price * (discount_percentage / 100))
        final_price = round(price - discount_amount, 2)
        
        # Categorize by rating
        if rating >= 4.5:
            rating_class = "Premium"
        elif rating >= 4.0:
            rating_class = "High"
        elif rating >= 3.0:
            rating_class = "Average"
        else:
            rating_class = "Low"
            
        # Add metadata
        processed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "product_id": pid,
            "name": title,
            "brand": brand,
            "category": category,
            "original_price": price,
            "discount_pct": discount_percentage,
            "final_price": final_price,
            "stock_quantity": stock,
            "inventory_value": stock_value,
            "rating": rating,
            "rating_class": rating_class,
            "processed_at": processed_at,
            "thumbnail": product.get("thumbnail", "")
        }
    except Exception as e:
        logger.error(f"Error transforming product {product.get('id', 'unknown')}: {e}")
        return None

def transform_all_products(raw_products):
    """Processes the entire list of products."""
    logger.info(f"Starting transformation of {len(raw_products)} records...")
    
    transformed_data = []
    
    for product in raw_products:
        cleaned = transform_product(product)
        if cleaned:
            transformed_data.append(cleaned)
            
    logger.info(f"Transformation complete. Success: {len(transformed_data)}/{len(raw_products)}")
    return transformed_data
