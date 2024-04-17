print("Wekcome to tip Calculator")
amt=float(input("What was the amount of your bill ? \n"))
tip=int(input("How many Percentage you like to give as Tip?  10,12 or 14 ?\n"))
persons=int(input("How many people split the bill ? \n"))
tip_percent=tip/100
tip_amount=tip_percent*amt
total_amount=amt+tip_amount
bill_per_person=total_amount/persons
amount=round(bill_per_person, 2)
print(f"Each Person Should Pay $ {amount:.2f}")


