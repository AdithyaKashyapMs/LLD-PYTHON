class CSVParser:
    def parse(self):
        self.openFile()
        # Specific logic/code for parsing CSV files
        print("Parsing CSV file")

        self.closeFile()

    def openFile(self):
        print("Opening CSV file")

    def closeFile(self):
        print("Closing CSV file")


# Here the CSVParser and JSONParser classes have their own implementations of the parse method,
#  but they share the same structure of opening a file, parsing it, and then closing the file.
#  This is an example of the Template Method design pattern, where the common steps are defined in a base class (in this case, 
# the parse method), and the specific steps are implemented in the subclasses (CSVParser and JSONParser).
class JSONParser:
    def parse(self):
        self.openFile()
        # Specific logic/code for parsing JSON files
        print("Parsing JSON file")
        
        self.closeFile()

    def openFile(self):
        print("Opening JSON file")

    def closeFile(self):
        print("Closing JSON file")

csv_parser = CSVParser()
csv_parser.parse()

json_parser = JSONParser()
json_parser.parse()
