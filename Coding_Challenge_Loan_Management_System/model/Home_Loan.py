from model.loan import Loan




class HomeLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_status, property_address, property_value):
        # Initialize attributes from the parent Loan class
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "HomeLoan", loan_status)
        # Specific attributes for HomeLoan
        self.__property_address = property_address  
        self.__property_value = property_value      

    # Getter methods
    def get_property_address(self):
        return self.__property_address
    
    def get_property_value(self):
        return self.__property_value

    # Setter methods
    def set_property_address(self, property_address):
        self.__property_address = property_address
    
    def set_property_value(self, property_value):
        self.__property_value = property_value


 # Print method
    def print_info(self):
        super().print_info()  # Calls the Loan print method
        print(f"Property Address: {self.__property_address}")
        print(f"Property Value: {self.__property_value}")