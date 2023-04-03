def assessed_value(county, market_value):
    assessed_percent = 0
    if county == "Cook":
        assessed_percent = 0.90
    elif county == "DuPage":
        assessed_percent = 0.80
    elif county == "McHenry":
        assessed_percent = 0.75
    elif county == "Kane":
        assessed_percent = 0.60
    else:
        assessed_percent = 0.70
    return market_value * assessed_percent
sum_market_values = 0
sum_assessed_values = 0
while True:
    decision = input("Do you want to continue? (Yes or No): ")
    if decision.lower() == 'no':
        break
    county = input("Enter county: ")
    market_value = float(input("Enter market value of the home: "))
    assessed_val = assessed_value(county, market_value)
    print(f"Assessed value: {assessed_val:.2f}")
    sum_market_values += market_value
    sum_assessed_values += assessed_val
print(f"Sum of all market values: {sum_market_values:.2f}")
print(f"Sum of all assessed values: {sum_assessed_values:.2f}")