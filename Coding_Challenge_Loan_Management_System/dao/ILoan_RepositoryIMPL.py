# dao/ILoanRepositoryImpl.py

from dao.iloan_repository import ILoanRepository
from exception.invalid_loan_exception import InvalidLoanException


class LoanRepositoryImpl(ILoanRepository):
    
    def __init__(self):
        # Simulated database to hold loan records
        self.db = {}

    def applyLoan(self, loan):
        confirmation = input(f"Do you want to apply for the {loan.loanType} loan? (Yes/No): ")
        if confirmation.lower() == 'yes':
            loan.loanStatus = 'Pending'
            self.db[loan.loanId] = loan
            print(f"Loan applied successfully. Loan ID: {loan.loanId}")
        else:
            print("Loan application cancelled.")

    def calculateInterest(self, loanId):
        loan = self.db.get(loanId)
        if not loan:
            raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        interest = (loan.principalAmount * loan.interestRate * loan.loanTerm) / 12
        return interest

    def loanStatus(self, loanId):
        loan = self.db.get(loanId)
        if not loan:
            raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        # Assuming customer has a `creditScore` attribute
        if loan.customer.creditScore > 650:
            loan.loanStatus = 'Approved'
            print(f"Loan {loanId} has been approved.")
        else:
            loan.loanStatus = 'Rejected'
            print(f"Loan {loanId} has been rejected.")

    def calculateEMI(self, loanId):
        loan = self.db.get(loanId)
        if not loan:
            raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        
        monthly_rate = loan.interestRate / 12 / 100
        N = loan.loanTerm
        P = loan.principalAmount
        emi = (P * monthly_rate * ((1 + monthly_rate) ** N)) / (((1 + monthly_rate) ** N) - 1)
        return emi

    def loanRepayment(self, loanId, amount):
        loan = self.db.get(loanId)
        if not loan:
            raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        
        emi = self.calculateEMI(loanId)
        if amount < emi:
            print("Payment rejected: The amount is less than the EMI.")
        else:
            number_of_emis_paid = amount // emi
            remaining_loan_term = loan.loanTerm - number_of_emis_paid
            loan.loanTerm = remaining_loan_term
            print(f"{number_of_emis_paid} EMI(s) paid. Remaining loan tenure: {loan.loanTerm} months.")
    
    def getAllLoan(self):
        if not self.db:
            print("No loans available.")
        else:
            for loan in self.db.values():
                print(vars(loan))

    def getLoanById(self, loanId):
        loan = self.db.get(loanId)
        if not loan:
            raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        print(vars(loan))
