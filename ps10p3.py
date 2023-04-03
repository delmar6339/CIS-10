def out_the_door_price(msrp, make, model, ev_code):
    percent_off = 0
    if make == "Honda" and model == "Accord":
        percent_off = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent_off = 0.15
    elif ev_code == "Y":
        percent_off = 0.30
    else:
        percent_off = 0.05
    new_msrp = msrp * (1 - percent_off)
    total = new_msrp * 1.07
    return total
sum_mspr = 0
sum_sales_price = 0
while True:
    decision = input("Do you want to continue? (Yes or No): ")
    if decision.lower() == 'no':
        break
    make = input("Enter automobile make: ")
    model = input("Enter automobile model: ")
    ev_code = input("Enter electric vehicle code (Y or N): ")
    msrp = float(input("Enter MSRP (sticker price): "))
    total = out_the_door_price(msrp, make, model, ev_code)
    print(f"Total out-the-door price: {total:.2f}")
    sum_mspr += msrp
    sum_sales_price += total
print(f"Sum of all MSRP's: {sum_mspr:.2f}")
print(f"Sum of all sales prices: {sum_sales_price:.2f}")