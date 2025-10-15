from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Jaradafa"
owner_name = "John Gabriel S. Sta Maria"


# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["California Maki", "Spicy Ramen", "Tonkatsu Curry", "Gyoza", "Curry Rice", "Takoyaki"]
beverages = ["Red Iced Tea", "Matcha Shake"]

# Tuple data type
business_hours = ("12:00 PM", "11:00 PM")

# Dictionary data type
menu = {
    "California Maki": 79.99,
    "Spicy Ramen": 129.99,
    "Tonkatsu Curry": 140.00,
    "Gyoza": 89.99,
    "Curry Rice": 129.99,
    "Takoyaki": 119.99,
    "Red Iced Tea": 45.00,
    "Matcha Shake": 74.99
}

# Set data type
common_allergens = {"gluten", "dairy", "poultry"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['California Maki']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Spicy Ramen']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Tonkatsu Curry']:.2f}", target="price3")
display(product_names[3], target="prod4")
display(f"₱{menu['Gyoza']:.2f}", target="price4")
display(product_names[4], target="prod5")
display(f"₱{menu['Curry Rice']:.2f}", target="price5")
display(product_names[5], target="prod6")
display(f"₱{menu['Takoyaki']:.2f}", target="price6")
display(beverages[0], target="prod7")
display(f"₱{menu['Red Iced Tea']:.2f}", target="price7")
display(beverages[1], target="prod8")
display(f"₱{menu['Matcha Shake']:.2f}", target="price8")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

