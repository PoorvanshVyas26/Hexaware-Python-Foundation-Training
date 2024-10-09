from abc import ABC, abstractmethod

# Interface for Loan Repository
class ILoanRepository(ABC):

    # @abstractmethod
    # def getCustomerById(self, customer_id):
    #     """Retrieve a loan by loan_id and print its details. Raise InvalidLoanException if not found"""
    #     pass

    @abstractmethod
    def getLoanById(self, loan_id):
        """Retrieve a loan by loan_id and print its details. Raise InvalidLoanException if not found"""
        pass

    @abstractmethod
    def loanStatus(self, loan_id):
        """Check loan status based on credit score, approve or reject, and update in the database"""
        pass

    @abstractmethod
    def applyLoan(self, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status="Pending"):
        """Apply for a loan and store it in the database with status pending"""
        pass

    @abstractmethod
    def calculateInterest(self, loan_id):
        """Calculate interest for the loan by loan_id. Raise InvalidLoanException if loan not found."""
        pass
    
    # @abstractmethod
    # def calculateInterest(self, principal_amount, interest_rate, loan_term):
    #     """Overloaded method to calculate interest when creating a loan"""
    #     pass

    @abstractmethod
    def calculateEMI(self, loan_id):
        """Calculate EMI based on the loan details. Raise InvalidLoanException if loan not found"""
        pass

    # @abstractmethod
    # def calculateEMI(self, principal_amount, interest_rate, loan_term):
    #     """Overloaded method to calculate EMI while creating a loan"""
    #     pass

    @abstractmethod
    def loanRepayment(self, loan_id, amount):
        """Repay the loan and calculate how many EMIs can be paid from the amount"""
        pass

    @abstractmethod
    def getAllLoans(self):
        """Retrieve and print all loans from the database"""
        pass

    

    
