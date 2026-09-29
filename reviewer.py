age = int(input("Enter your age: "))
revenue = float(input("Enter your annual revenue: "))
cc = int(input("Enter your credit score: "))
years = int(input("Enter the number of years you have been employed: "))
defaults = bool(input("Defaults: ")) 
collateral = str(input("Enter the name of your collateral: "))
collateral_value = float(input("Enter the value of your collateral: "))
print("===========================================================")
#Baseline
base_fee = 0.0
max_loan = 0.0
if age >= 21 and years >= 2 and defaults == False:
    print("You have passed the baseline criteria")
    #Tier 1
    print("Results of the loan application are as follows: ")
    if cc >= 720:
        max_loan = 3 * revenue
        if revenue >= 50000:
            print("Passed over 50000")
            base_fee = max_loan * 0.015
            print("base fee is ", base_fee)
            print("max loan is ", max_loan)
        else:
            base_fee = max_loan * 0.025
            print("base fee is ", base_fee)
        #Collateral check 
        if collateral_value >= max_loan:
            print("Ok: Value is checked and approved")
        else:
            print("Rejected: Insufficient collateral value for ", collateral)
        #Surcharge
        surcharge_fee_rate = max_loan * base_fee
        if surcharge_fee_rate % 5000 != 0:
            base_fee += 250
            print("New charge is ", base_fee)
    #Tier 2
    elif cc > 620 and cc < 720:
        print("Passed by 620")
        max_loan = 1.5 * revenue
        if years >= 5.0:
            print("Passed by 5 years")
            base_fee = max_loan * 0.02
            print("Base fee is ", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Base fee is ", base_fee)
        #Collateral check 
        if collateral_value >= max_loan:
                    print("Ok: Value is checked and approved")
        else:
            print("Rejected: Insufficient collateral value for ", collateral)
        #Surcharge
        surcharge_fee_rate = max_loan * base_fee
        if surcharge_fee_rate % 5000 != 0:
            base_fee += 250
            print("New charge is ", base_fee)
    #Tier 3
    elif cc < 620:
        print("Rejected: Credit score below requirement")
            
else:
    print("Rejected: High Risk Application or Ineligible Owner")
