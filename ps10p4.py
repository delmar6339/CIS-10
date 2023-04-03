def train_ticket_price(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5
sum_ticket_prices = 0
while True:
    decision = input("Do you want to continue? (Yes or No): ")
    if decision.lower() == 'no':
        break
    last_name = input("Enter last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))
    ticket_price = train_ticket_price(miles)
    print(f"Ticket price: ${ticket_price}")
    sum_ticket_prices += ticket_price
print(f"Sum of all ticket prices: ${sum_ticket_prices}")