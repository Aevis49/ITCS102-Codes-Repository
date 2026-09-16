# Scenario: The bank loan and interest rate approver

# Inputs
age = int(input("What is your age? ---> "))
is_employed = bool(input("Are you employed? (True/leave blank if False) ---> "))
credit_score = int(input("What is your credit score? (1-1000) ---> "))
annual_income = float(input("What is your annual income? ---> "))
has_collateral = bool(input("Do you have any collateral? (True/leave blank if False) ---> "))

#Status Separator
print("=============================")
print("===========Status============")
print("=============================")
print("Age: ", age)
print("Employed: ", is_employed)
print("Credit Score: ", credit_score)
print("Annual Income: ", annual_income)
print("Collateral: ", has_collateral)

# Baseline eligiability
base_interest = 0.0

if age >= 21 and is_employed:
    print("User has passed the baseline criteria")

    if credit_score >= 750:  # Tier 1: High credit
        print("You have a high credit score!")
        if annual_income >= 100000:
            base_interest = 4.5
        else:
            base_interest = 5.0
        print("Approved at", base_interest, "℅ interest")

    elif credit_score >= 600:  # Tier 2: Fair credit
        print("You have a fair credit score!")
        if has_collateral:
            base_interest = 7.0
        elif annual_income < 40000:
            base_interest = 9.5
        else:
            base_interest = 8.0
        print("Approved at ", base_interest, "℅ interest")

    else:  # Tier 3: credit_score < 600
        print("Rejected: Credit score too low")

else:
    print("Rejected: Fails baseline criteria")
