
import pyodbc
import sys
import os

# Get the absolute path of the root project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import DBUtil
from dao.iloan_repository import ILoanRepository
from exception.invalid_loan_exception import InvalidLoanException
from model.customer import Customer

class LoanRepository(ILoanRepository):
    def __init__(self):
        try:
        # Simulated database (could be replaced with actual DB interactions)
            self.conn = DBUtil.getDBConn()
            
            if self.conn is None:
                print("Database connection could not be established.")
        
            self.cursor = self.conn.cursor()
        except :
            print(f"Error establishing database connection")

    # def getCustomerById(self, customer_id):
    #     try:
    #         sql = "SELECT * FROM customer WHERE customer_id = ?"
    #         self.cursor.execute(sql, customer_id)
    #         result = self.cursor.fetchone()
    #         print("fetching cust details...")

    #         if result:
    #             print("printing details...")
    #             print(f"customer details: {result}")

    #     except Exception as e:
    #         print(e)

    def getLoanById(self, loan_id : int):
        try:
            #cursor = self.conn.cursor()
            sql = "SELECT * FROM loan WHERE loan_id = ?"
            self.cursor.execute(sql, (loan_id,))
            loan = self.cursor.fetchone()
            print("fetching loan details...")

            if loan is None:
                raise InvalidLoanException(f"Loan with ID {loan_id} not found.")
            
            print("printing details...")
            print(f"your loan details: {loan}")

            # return {
            #     "loanId": loan[0],
            #     "customerId": loan[1],
            #     "principalAmount": loan[2],
            #     "interestRate": loan[3],
            #     "loanTerm": loan[4],
            #     "loanType": loan[5],
            #     "loanStatus": loan[6]
            # }

        except Exception as e:
            print(e)

        finally:
            self.cursor.close()

    def loanStatus(self, loan_id : int):
        try:
            #cursor = self.conn.cursor()
            sql = "SELECT c.credit_score, l.loan_status from Loan l join Customer c on l.customer_id = c.customer_id WHERE l.loan_id = ?"
            self.cursor.execute(sql, (loan_id,))
            status = self.cursor.fetchone()

            print("fetching credit score and loan status...")

            if status:
                credit_score = status[0]
                loan_status = status[1]

                if credit_score > 650:
                    print(f"the loan with ID {loan_id} will be approved")
                    update_query = "UPDATE Loan SET loan_status = 'Approved' WHERE loan_id = ?"
                    self.cursor.execute(update_query, (loan_id,))
                    self.conn.commit()  # Commit the changes

                else:
                    print(f"Loan with ID {loan_id} is rejected.")
                    # Update loan status in the database
                    update_query = "UPDATE Loan SET loan_status = 'Rejected' WHERE loan_id = ?"
                    self.cursor.execute(update_query, (loan_id,))
                    self.conn.commit()  # Commit the changes
   
            else:
                raise InvalidLoanException(f"Loan with ID {loan_id} not found.")
        
        except InvalidLoanException as e:
            print(f"Error: {e}")
        
        except Exception as e:
            print(e)

        finally:
            self.cursor.close()

    def getAllLoans(self):
        try:
            sql = "SELECT * FROM loan"
            self.cursor.execute(sql)
            loan = self.cursor.fetchall()

            if loan is None:
                raise InvalidLoanException(f"Loans not found.")
            
            print(f"loan details: {loan}")

        except Exception as e:
            print(e)

        finally:
            self.cursor.close()     
    
    def applyLoan(self, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status="Pending"):
        try:
            print("entered into apply loan")
        # SQL query to insert a new loan record
            query = """
            INSERT INTO Loan(loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status) 
            VALUES (14,?, ?, ?, ?, ?, ?)
            """
        
            values = (customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status)

        # Getting user confirmation
          
                # Confirm with the user before applying for the loan
            confirmation = input("Do you want to apply for this loan? (Yes/No): ").lower()
            if confirmation == "yes":
                    # Apply for the loan
                self.cursor.execute(query, values)
                self.conn.commit()
                print("Loan has been successfully applied and stored in the database.")
            else:
                print("Loan application canceled.")
        
            

        # Execute the query with parameters
        
        # Commit the transaction
            
        except Exception as e:
            print(f"An error occurred while applying for the loan: {e}")
            self.conn.rollback()  # Rollback the transaction on error
        finally:
            self.cursor.close()  # Ensure cursor is closed after operation

    def calculateEMI(self, loan_id):
        """Calculate EMI based on loan details"""
        try:
            if loan_id:
                query = "SELECT principal_amount, interest_rate, loan_term FROM Loan WHERE loan_id = ?"
            self.cursor.execute(query, (loan_id,))
            loan = self.cursor.fetchone()

            if not loan:
                print(f"Loan with ID {loan_id} not found.")
                return None
            
            principal_amount, interest_rate, loan_term = loan

            principal_amount = float(principal_amount)
            interest_rate = float(interest_rate)

            print(f"Retrieved Loan Detail: Principal: {principal_amount}, Interest Rate: {interest_rate}, Term: {loan_term}")

            # Convert the annual interest rate to a monthly interest rate
            monthly_interest_rate = (interest_rate / 12) / 100

            emi = (principal_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** loan_term)) / \
              (((1 + monthly_interest_rate) ** loan_term) - 1)
            
            print(f"your monthly EMI is: {emi:.2f}")
            return emi
        
        except Exception as e:
            print(f"An error occurred while calculating EMI: {e}")
            return None
        
        
    def loanRepayment(self, loan_id, amount):
        """Repay the loan and calculate how many EMIs can be paid from the amount."""
        try:
            # Fetch loan and calculate EMI
            emi = self.calculateEMI(loan_id)

            if not emi:
                print(f"Cannot calculate EMI for loan {loan_id}.")
                return

            # Check how many full EMIs can be paid from the given amount
            full_emis = amount // emi

            if full_emis < 1:
                print(f"The amount you're trying to pay should be greater than EMI. EMI for loan {loan_id} is {emi:.2f}")
                return

            # # Update the loan repayment in the database
            # query = "UPDATE Loan SET remaining_loan_amount = remaining_loan_amount - ?, last_payment_amount = ? WHERE loan_id = ?"
            # self.cursor.execute(query, (full_emis * emi, amount, loan_id))
            # self.conn.commit()

            print("loan repayment successful...")

            print(f"{int(full_emis)} EMIs have been paid for loan {loan_id}.")

        except Exception as e:
            print(f"An error occurred during loan repayment: {e}")
            self.conn.rollback()
        finally:
            self.cursor.close()


    def calculateInterest(self, loan_id):
        """Calculate interest for the loan by loan_id. Raise InvalidLoanException if loan not found."""
        try:
            # SQL query to fetch loan details
            query = "SELECT principal_amount, interest_rate, loan_term FROM Loan WHERE loan_id = ?"
            self.cursor.execute(query, (loan_id,))
            loan = self.cursor.fetchone()

            if loan is None:
                raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

            # Extract loan details
            principal_amount = loan[0]
            interest_rate = loan[1]  # Annual interest rate
            loan_term = loan[2]  # Loan term in months

            # Calculate the interest
            interest = (principal_amount * interest_rate * loan_term) / 12

            return interest

        except InvalidLoanException as e:
            print(e)  # Handle loan not found
        except Exception as e:
            print(f"An error occurred while calculating interest: {e}")
        finally:
            self.cursor.close()  # Ensure cursor is closed after operation    
        






