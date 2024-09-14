products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))

def display_products(products_list):
    for index, (name, price) in enumerate(products_list, start=1):
        print(f"{index}. {name} - ${price:.2f}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append({'product': product[0], 'quantity': quantity, 'price': product[1]})

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        for item in cart:
            print(f"Product: {item['product']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f} (Total: ${item['price'] * item['quantity']:.2f})")

def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Receipt for {name} ({email}):")
    display_cart(cart)
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")
    print("----------------")

def validate_name(name):
    parts = name.split()
    if len(parts) != 2:
        return False
    first_name, last_name = parts
    return first_name.isalpha() and last_name.isalpha()

def validate_email(email):
    return '@' in email

def main():
    cart = []
    
    while True:
        name = input("Enter your name (First Last): ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid name with first and last names.")

    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email address with '@'.")

    while True:
        display_categories()
        category_choice = int(input("Select a category number: "))
        
        categories = list(products.keys())
        if 1 <= category_choice <= len(categories):
            selected_category = categories[category_choice - 1]
            product_list = products[selected_category]
            sorted_product_list = product_list.copy()  # Initialize with a copy of the unsorted list
            
            while True:
                display_products(sorted_product_list)
                action = int(input("Choose an action: \n1. Select a product to buy\n2. Sort products by price\n3. Go back to categories\n4. Finish shopping\n"))
                
                if action == 1:
                    product_choice = int(input("Enter the number of the product you want to buy: "))
                    if 1 <= product_choice <= len(sorted_product_list):
                        quantity = int(input("Enter the quantity: "))
                        add_to_cart(cart, sorted_product_list[product_choice - 1], quantity)
                    else:
                        print("Invalid product number.")
                
                elif action == 2:
                    sort_order = int(input("Sort by price: \n1. Ascending\n2. Descending\n"))
                    if sort_order in [1, 2]:
                        sorted_product_list = display_sorted_products(product_list, sort_order)
                        display_products(sorted_product_list)
                    else:
                        print("Invalid sort order.")
                
                elif action == 3:
                    break
                
                elif action == 4:
                    if cart:
                        # Display cart and calculate total cost
                        print("Here is your cart:")
                        display_cart(cart)
                        total_cost = sum(item['price'] * item['quantity'] for item in cart)
                        address = input("Enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return
                
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid category number. Please try again.")

if __name__ == "__main__":
    main()
