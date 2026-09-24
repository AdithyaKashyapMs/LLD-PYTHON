class Logger:
    
    # # method override
    # def __new__(cls):
    #     return "Hello, World!"
    
    # lets make a class variable to hold 
    # This is a class variable that will hold the single instance of the Logger class
    __instance = None


    # This is the constructor of the Logger class. It initializes the file_name and log_count attributes.
    def __new__(cls, file_name: str):
        if cls.__instance is None: # here are checking if the class variable __object is None, which means that no instance
                                 # of the Logger class has been created yet. If it is None, we create a new instance of the Logger class using super().__new__(cls) 
                                 # and assign it to the class variable __object. This ensures that only one instance of the Logger class is created.
            cls.__instance = super().__new__(cls)
            cls.__instance.file_name = file_name
            cls.__instance.log_count = 0
            return cls.__instance
        
        # Here we are returning the existing instance of the Logger class stored in the class variable __object
        # This ensures that all subsequent calls to the Logger class will return the same instance, maintaining the singleton pattern.
        else: 
            return cls.__instance

    def log(self, text:str):
        print(f"Logger is logging the text: {text} to the file: {self.file_name}")
        self.log_count += 1

    def get_log_count(self):
        return self.log_count

log1 = Logger("app.log")
log1.log("User created successfully")

log2 = Logger("app.log")
log2.log("Staff is banging someone")

log3 = Logger("app.log")
log3.log("Bank transaction is successful")

print(log1.get_log_count())
print(log2.get_log_count())
print(log3.get_log_count())