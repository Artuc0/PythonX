def enter_products():
    buying_data = {}
    enter_details = True
    
    while enter_details:
        details = input("Press 1 to add product and 0 to quit\n>")
        if details == "1":
            product = input("Enter product\n>")
            quantity = int(input("Enter quantity\n>"))
            buying_data.update({product:quantity})
        elif details == "0":
            enter_details = False
        else:
            print("Invalid option.")
    return buying_data
            
def get_price(product, quantity):
    price_data = {
        "Biscuit": 5,
        "Chicken": 7,
        "Egg": 3,
        "Fish": 4,
        "Coke": 3,
        "Bread": 3.5,
        }
    subtotal = price_data[product]*quantity
    print(f"{product}: ${price_data[product]} x {quantity} = {subtotal}")
    return subtotal

def get_discount(bill_amount, membership):
    discount = 0
    if bill_amount >= 25:
        if membership == "Gold":
            bill_amount = bill_amount * 0.8
            discount = 20
        elif membership == "Silver":
            bill_amount = bill_amount * 0.9
            discount = 10
        elif membership == "Bronze":
            bill_amount = bill_amount * 0.95
            discount = 5
        print(f"{discount}% off for {membership} membership on total amount: ${bill_amount}")
    else:
        print("No discount on amount less than $25")
    return bill_amount

def make_bill(buying_data, membership):
    bill_amount = 0
    for key, value in buying_data.items():
        bill_amount += get_price(key, value)
    bill_amount = get_discount(bill_amount, membership)
    print(f"The discounted amount is ${bill_amount}")
    
buying_data = enter_products()
membership = input("Enter customer membership\n>")
make_bill(buying_data, membership)