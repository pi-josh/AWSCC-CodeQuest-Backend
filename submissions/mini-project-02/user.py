class User:
    def __init__(self, username, password, website):
        self._username = username
        self._password = password
        self._website = website
    
    
    def get_username(self):
        return self._username
    
    
    def get_password(self):
        return self._password
    
    
    def get_website(self):
        return self._website
    
    
    def set_username(self, username):
        self._username = username
        
    
    def set_password(self, password):
        self._password = password
        
    
    def set_website(self, website):
        self._website = website