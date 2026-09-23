from abc import ABC, abstractmethod

# This is an Template where open and close methods are common for all the parsers and the
#  dataParser method is specific to each parser
class DataParser:
    def _parse(self):
        self._open()
        self._dataParser()
        self._close()

    def _open(self):
        print("Opening file")

    def _close(self):
        print("Closing file")

    @abstractmethod
    def _dataParser(self):
        pass


class CSVParser(DataParser):
    def _dataParser(self):
        print("Parsing CSV File")

# Here the CSVParser and JSONParser classes have their own implementations of the parse method,
# but they share the same structure of opening a file, parsing it, and then closing the file.
# This is an example of the Template Method design pattern, where the common steps are defined in a base class (in this case, the parse method), and the specific steps are implemented in

class JSONParser(DataParser):
    def _dataParser(self):
        print("Parsing JSON File")

csv_parser = CSVParser()
csv_parser._parse()

json_parser = JSONParser()
json_parser._parse()