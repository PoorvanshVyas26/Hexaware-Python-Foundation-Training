import sys
import os

# Get the absolute path of the root project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.customer import Customer
from dao.loan_repository import LoanRepository
from exception.invalid_loan_exception import InvalidLoanException


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
           


    # Apply for the loan
            print("calling apply loan")
            self.lr.applyLoan(customer_id, principal_amount, interest_rate, loan_term, loan_type)

            print("Loan application for has been submitted with status 'Pending'.")

            # else:
            #     print("Loan application canceled.")

    def calculateEMI(self):
        try:
            print("Calculating EMI...")
            loan_id = int(input("Please enter the Loan ID to calculate EMI for your loan: "))
            emi = self.lr.calculateEMI(loan_id)
            
            if emi: 
                print(f"Calculated EMI: {emi:.2f}")
        
        except Exception as e:
            print(f"An error occurred while calculating EMI: {e}")
    
    def loanRepayment(self):
        try:
            loan_id = int(input("Enter the loan ID: "))
            amount = float(input("Enter the repayment amount: "))

            # Call the loan repository method to handle the repayment
            self.lr.loanRepayment(loan_id, amount)

        except ValueError:
            print("Invalid input. Please enter numeric values for loan ID and amount.")
        except Exception as e:
            print(f"An error occurred during the repayment process: {e}")

    def calculateInterest(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            interest = self.lr.calculateInterest(loan_id)
            print(f"The calculated interest for loan ID {loan_id} is: {interest:.2f}")
        except InvalidLoanException as e:
            print(e)




def main_menu():
    loan_mgmt = LoanManagement()
    while True:
        print("\n----------Main Menu----------")
        print("Press-1 to Check your Loan details with Id")
        print("Press-2 to Check Loan Status")
        print("Press-3 to see all the Loans in the system")
        print("Press-4 to Apply Loan")
        print("Press-5 to Calculate EMI")
        print("Press-6 to Loan Repayment")
        print("Press-7 to Calculate Interest")
        print("Press-8 to Exit")

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
            loan_mgmt.calculateEMI()
        elif ch== '6':
            loan_mgmt.loanRepayment()
        elif ch== '7':
            loan_mgmt.calculateInterest()
        
        
        elif ch== '8':
            print("You are Exiting the system...")
            break


        else:
            print("You have entered an Invalid choice. Please try again...")
                


if __name__ == "__main__":
    main_menu()