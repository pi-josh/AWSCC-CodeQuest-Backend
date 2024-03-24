class User:
    def __init__(self, email, password, website):
        self._email = email
        self._password = password
        self._website = website
    
    
    def get_email(self):
        return self._email
    
    
    def get_password(self):
        return self._password
    
    
    def get_website(self):
        return self._website
    
    
    def set_email(self, email):
        self._email = email
        
    
    def set_password(self, password):
        self._password = password
        
    
    def set_website(self, website):
        self._website = website