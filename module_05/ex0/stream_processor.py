from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    An abstract base class defining the common processing interface
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """
         - Process the data and return result string
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
         - Validate if data is appropriate for this processor
        """
        pass

    def format_output(self, result: str) -> str:
        """
         - Format the output string
        """
        return f"===|{result}|==="


class NumericProcessor(DataProcessor):
    """
    • Specialized Classes: NumericProcessor Base on DataProcessor
    with method insted of abstractmethod
    """
    def process(self, data: list[int]) -> str:
        """
        Process the arrey of data
        """
        total = sum(data)
        avg = total / len(data)
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"

    def validate(self, data: list[int]) -> bool:
        """
        Validate if data is appropriate for this processor
        """
        if type(data) is not list:
            return False
        for ell in data:
            if type(ell) is not int:
                return False
        return True

    def format_output(self, result: str) -> str:
        """
        Format the string in parameter
        """
        return f"=== {result} ==="


class TextProcessor(DataProcessor):
    """
    • TextProcessor Classes: NumericProcessor Base on DataProcessor
    with method insted of abstractmethod
    """
    def process(self, data: str) -> str:
        """
        Process the string
        """
        return f"Processed text: {len(data)} characters, \
{data.count(' ') + 1} words"

    def validate(self, data: list[int]) -> bool:
        """
        Validate if data is appropriate for this processor
        """
        for letter in data:
            if type(letter) is not str:
                return False
        return True

    def format_output(self, result: str) -> str:
        """
        Format the output string
        """
        return f"/\\/\\{result}/\\/\\"


class LogProcessor:
    """
    • LogProcessor Classes: NumericProcessor Base on DataProcessor
    with method insted of abstractmethod
    """
    def process(self, data: str) -> str:
        """
        Process the data
        """
        pos = data.find(':')
        if pos == -1:
            return "No log message found"
        return f"[{data[:pos]}] {data[:pos]} level detected:{data[pos+1:]}"

    def validate(self, data: list[int]) -> bool:
        """
        Validate if data is appropriate for this processor
        """
        for letter in data:
            if type(letter) is not str:
                return False
        return True

    def format_output(self, result: str) -> str:
        """
        Format the output string
        """
        return f"/\\{result}/\\"


def data_processor_demo():
    """
    A demo to ilustrate the subject
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric_instance = NumericProcessor()
    lst = [1, 2, 3, 4, 5]
    print("Processing data:", lst)
    if numeric_instance.validate(lst):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data not verified")
    print("Output:", numeric_instance.process(lst))
    print()

    print("Initializing Text Processor...")
    text_instance = TextProcessor()
    text = "Hello Nexus World"
    print(f'Processing data: "{text}"')
    if text_instance.validate(text):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data not verified")
    print("Output:", text_instance.process(text))
    print()

    print("Initializing Log Processor...")
    log_instance = LogProcessor()
    log = "ERROR: Connection timeout"
    print(f'Processing data: "{log}"')
    if log_instance.validate(log):
        print("Validation: Log entry verified")
    else:
        print("Validation: Log entry not verified")
    print("Output:", log_instance.process(log))
    print()


def polymorphic_processing_demo():
    """
    A second demo to ilustrate the subject
    """
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples = [
        [1, 2, 3],
        "Hello world!",
        "INFO: System ready"
    ]

    for processor, data, index in zip(processors, data_samples, range(3)):
        try:
            if not processor.validate(data):
                raise ValueError("Invalid data for this processor")
            print(f"Result {index}: {processor.process(data)}")

        except Exception as e:
            print(f"Error: {e}\n")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    data_processor_demo()
    polymorphic_processing_demo()
