class Customer:
    def __init__(self, customer_id, name, email, phone, address, credit_score):
        self.__customer_id = customer_id  
        self.__name = name                
        self.__email = email              
        self.__phone = phone              
        self.__address = address          
        self.__credit_score = credit_score  
    
    # Getter methods 
    def get_customer_id(self):
        return self.__customer_id
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_address(self):
        return self.__address
    
    def get_credit_score(self):
        return self.__credit_score
    
    # Setter methods 
    def set_name(self, name):
        self.__name = name
    
    def set_email(self, email):
        self.__email = email
    
    def set_phone(self, phone):
        self.__phone = phone
    
    def set_address(self, address):
        self.__address = address
    
    def set_credit_score(self, credit_score):
        self.__credit_score = credit_score

 # Print method
    def print_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phone}")
        print(f"Address: {self.__address}")
        print(f"Credit Score: {self.__credit_score}")