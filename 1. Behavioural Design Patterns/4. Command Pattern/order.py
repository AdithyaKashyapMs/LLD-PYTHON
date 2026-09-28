from abc import ABC, abstractmethod

# this is the command interface which will be implemented by all the concrete commands
# and it is used to execute the command
class Order(ABC):
    @abstractmethod
    def execute(self):
        pass
