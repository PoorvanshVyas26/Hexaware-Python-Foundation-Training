import sys
import os

# Get the absolute path of the root project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.customer import Customer
from dao.loan_repository import LoanRepository
from model.loan import Loan

class LoanManagement:
    def __init__(self):
        self.lr = LoanRepository()

    def getLoanById(self):
        loan_id = input("Enter Loan ID: ")
        # Fetch loan details by loan ID
        self.lr.getLoanById(loan_id)

    def loanStatus(self):
        loan_id = input("Enter Loan ID: ")
        # Check loan status by loan ID
        self.lr.loanStatus(loan_id)

    def getAllLoans(self):
        # Getting all the loans in the system, no parameter needed
        self.lr.getAllLoans()
    
    def applyLoan(self):

    # Get customer details
            customer_id = int(input("Enter your Customer ID: "))
            principal_amount = float(input("Enter the Principal Amount: "))
            interest_rate = float(input("Enter the Interest Rate: "))
            loan_term = int(input("Enter the Loan Term (in months): "))
            loan_type = input("Enter the Loan Type (CarLoan/HomeLoan): ")
            loan_status = "Pending"
           
            confirmation = input("Do you want to apply for the loan? (Yes/No): ")
            if confirmation.lower() == 'yes':
    # Create loan and customer instances
        #customer = Customer(customer_id=customer_id)  # Assuming a constructor that takes customer ID
                # loan = loan(customer_id=customer_id, 
                #         principal_amount=principal_amount, 
                #         interest_rate=interest_rate, 
                #         loan_term=loan_term, 
                #         loan_type=loan_type,
                #         loan_status='Pending')

    # Apply for the loan
                print("calling apply loan")
                self.lr.applyLoan(customer_id, principal_amount, interest_rate, loan_term, loan_type)

                print("Loan application for has been submitted with status 'Pending'.")

            else:
                print("Loan application canceled.")


def main_menu():
    loan_mgmt = LoanManagement()
    while True:
        print("\n----------Main Menu----------")
        print("Press-1 to Check your Loan details with Id")
        print("Press-2 to Check Loan Status")
        print("Press-3 to see all the Loans in the system")
        # print("Press-3 to Calculate Interest")
        print("Press-4 to Apply Loan")
        # print("Press-5 to Loan Repayment")
        print("Press-5 to Exit")

        ch = input("Select an option (1-8): ")
        
        if ch== '1':
            loan_mgmt.getLoanById()
        elif ch== '2':
            loan_mgmt.loanStatus()
        elif ch== '3':
            loan_mgmt.getAllLoans()
        elif ch== '4':
            loan_mgmt.applyLoan()
        
        
        
        elif ch== '5':
            print("You are Exiting the system...")
            break


        else:
            print("You have entered an Invalid choice. Please try again...")
                # c = int(input('\nEnter Your Customer ID :'))
                # cust = lp.getCustomerByID(c)
                # if not cust:
                #     n = input('Enter Your Name : ')
                #     eml = input('Enter Your Email Address : ')
                #     pno = input("Enter Your Phone Number : ")
                #     add = input('Enter Your Address : ')
                #     cscore = int(input('Enter Your Credit Score : '))
                #     c = Customer(name=n, email_address=eml, phone_number=pno, address=add, credit_score=cscore).insert_new_customer()
    
if __name__ == "__main__":
    main_menu()