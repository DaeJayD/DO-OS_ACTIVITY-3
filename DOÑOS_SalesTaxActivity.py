
tax = 0.06

p_amount = eval(input("Enter purchase amount: "))

sales_tax = p_amount * tax

final_tax = (str(round(sales_tax, 2)))

print("Sales tax is: " + final_tax)
