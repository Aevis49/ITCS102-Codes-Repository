#Scenario: The bank load and interest rate approver

#inputs
age = int(input("What is your age? ---> "))
is_employed = bool(input("Are you employed? (True/Write nothing if False)--> "))
credit_score = int(input("What is your credit score? (1-1000)--->"))
annual_income = float(input("What is your annnual income? ---> "))
has_collateral = bool(input("Do you have any collateral? (True/Write nothing if False)--->"))


#Baseline eligibility
base_interest = 0.0
if age >= 21 and is_employed == True:
    print("User has passed the baseline Criteria")
    if credit_score >= 750: #Tier 1: High Credit
        print("You have a high credit income!")
        if annual_income >= 100000:
            base_interest = 4.5
            print("You have a high credit income with a base interest rate of ",base_interest, "%")
    else:
            base_interest = 5.0
            print("You have a high credit income with a base interest rate of ", base_interest, "%")


            elif credit_score >= 600 and credit_score < 750: #Tier 2
                 print("You have a fair credit income!")
                 if has_collateral == True:
                    base_interest = 7.0
                    print("You have a fair credit income with a base interest rate of ", base_interest, "%")
                 elif annual_income < 40000:
                      base_interest = 9.5
                      print("You have a fair credit income with a base interest rate of ", base_interest, "%")
            else:
                 base_interest = 8.0
                 print("You have a fair credit income with a base interest rate of ", base_interest, "%")
                 if credit_score < 600:
                    print("Rejected: Credit score too low")
else:
    print("Rejected: Fails baseline criteria")