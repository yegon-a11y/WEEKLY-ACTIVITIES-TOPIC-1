def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill


units_consumed = float(input("Enter units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))


electricity_bill = calculate_bill(units_consumed, cost_per_unit)

print("The calculated electricity bill is:", electricity_bill)
