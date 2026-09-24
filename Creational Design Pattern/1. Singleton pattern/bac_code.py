class Logger:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.log_count = 0

    def log(self, text:str):
        print(f"Logger is logging the text: {text} to the file: {self.file_name}")
        self.log_count += 1

# Suppose there are different files 
# file1 : userservice
    # log1=Logger()
# file2: txn
    # log2=Logger()
# file3: staff

log1 = Logger("app.log")
log2 = Logger("app.log")
log3 = Logger("app.log")

#User 
log1.log("User created successfully")

# staff
log2.log("Staff is banging someone")

# bank
log3.log("Bank transaction is successful")


print(log1.log_count)
print(log2.log_count)
print(log3.log_count)
# everthing is printing 1 because we are creating multiple instances of the logger class.
# 3 objects are created and each object has its own log_count variable. So, the log_count variable is not shared among the objects.

# But we need to have only one instance of the logger class and that instance should be shared among all the objects. So, we need to implement singleton pattern in the logger class.

# All are different objects
# We need to ensure that only one instance of the logger class is created.
print(id(log1))
print(id(log2))
print(id(log3))