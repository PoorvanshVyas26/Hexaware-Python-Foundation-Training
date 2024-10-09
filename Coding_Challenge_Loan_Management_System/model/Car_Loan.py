from model.loan import Loan


class CarLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_status, car_model, car_value):
        
        # Initializing attributes from the parent Loan class
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "CarLoan", loan_status)
        
        # Specific attributes for CarLoan
        self.__car_model = car_model          
        self.__car_value = car_value          

    # Getter methods
    def get_car_model(self):
        return self.__car_model
    
    def get_car_value(self):
        return self.__car_value

    # Setter methods
    def set_car_model(self, car_model):
        self.__car_model = car_model
    
    def set_car_value(self, car_value):
        self.__car_value = car_value


 # Print method
    def print_info(self):
        super().print_info()  # Calls the Loan print method
        print(f"Car Model: {self.__car_model}")
        print(f"Car Value: {self.__car_value}")