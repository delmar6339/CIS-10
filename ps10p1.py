def next_month_forecast(month, sales):
    forecast_percent = 0
    if month in ['Jan', 'Feb', 'Mar']:
        forecast_percent = 0.10
    elif month in ['Apr', 'May', 'Jun']:
        forecast_percent = 0.15
    elif month in ['Jul', 'Aug', 'Sep']:
        forecast_percent = 0.20
    elif month in ['Oct', 'Nov', 'Dec']:
        forecast_percent = 0.25
    return sales * (1 + forecast_percent)
while True:
    decision = input("Do you want to continue? (Yes or No): ")
    if decision.lower() == 'no':
        break
    last_name = input("Enter last name: ")
    month = input("Enter month: ")
    sales = float(input("Enter sales: "))
    next_month_sales = next_month_forecast(month, sales)
    print(f"Next month's sales for {last_name}: {next_month_sales:.2f}")