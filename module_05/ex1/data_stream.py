from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    """
    DataStream - an abstract base class with core streaming functionality
    """
    def __init__(self, arg: str = None) -> None:
        """
        init w/ an arg to show the behavior"""
        super().__init__()

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data
        """
        pass

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        """
         - Filter data based on criteria
        """
        if criteria is None:
            return data_batch
        return [ell for ell in data_batch
                if ell is not None and criteria in ell]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        - Return stream statistics
        """
        return {0: "Place Holder"}


class SensorStream(DataStream):
    """
    SensorStream class that take the stream and process it
    """
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        process basic data w/ stuct
        List[temp: float, humidity: int, pressure: 1013]
        """
        self.process = 3
        if data_batch is not None and len(data_batch) == 3:
            temp, humidity, pressure = data_batch
            self.avg_temp = temp
            self.process = 3
            return f"[temp:{temp}, humidity:{humidity}, pressure:{pressure}]"
        self.process = 0
        return "No data process"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        - Return stream statistics
        """
        print(
            f"Sensor analysis: {self.process} readings processed, "
            f"avg temp: {self.avg_temp}°C"
        )
        return {0: self.avg_temp}


class TransactionStream(DataStream):
    """
    TransactionStream class that take the stream and process it
    """
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        process basic data w/ stuct
        List[buy: int, sell: int, buy: 1013]]
        """
        if data_batch is not None and len(data_batch) == 3:
            buy, sell, buy_second = data_batch
            self.net_flow = buy + buy_second - sell
            self.process = 3
            return f"[buy:{buy}, humidity:{sell}, pressure:{buy_second}]"
        self.process = 0
        return "No data process"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        - Return stream statistics
        """
        print(
            f"Transaction analysis: {self.process} operations, "
            f"net flow: +{self.net_flow} units"
        )
        return {0: self.net_flow}


class EventStream(DataStream):
    """
    EventStream class that take a Event and process it
    """
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        process basic data w/ stuct
        List[state_first: str, state_second: str, state_third: str]]
        """
        error_count = 0
        if data_batch is not None and len(data_batch) == 3:
            state_first, state_second, state_third = data_batch
            if state_first == "error":
                error_count += 1
            if state_second == "error":
                error_count += 1
            if state_third == "error":
                error_count += 1
            self.state_error = error_count
            self.process = 3
            return f"[{state_first}, {state_second}, {state_third}]"
        self.process = 0
        return "No data process"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        print stat and return a dict
        """
        print(
            f"Event analysis: {self.process} events, "
            f"{self.state_error} error detected"
        )
        return {0: self.state_error}


class StreamProcessor:
    """
    StreamProcessor: can handle any stream type through polymorphism
    """

    sensor = SensorStream()
    transaction = TransactionStream()
    event = EventStream()

    sensor_count = 0
    tr_count = 0
    event_count = 0

    def __init__(self) -> None:
        """
        init the class
        """
        self.critical = 2
        self.large_transaction = 1

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        process the good batch
        """
        if isinstance(data_batch[0], float):
            StreamProcessor.sensor.process_batch(data_batch)
            StreamProcessor.sensor_count += 1
        elif isinstance(data_batch[0], int):
            StreamProcessor.transaction.process_batch(data_batch)
            StreamProcessor.tr_count += 1
        elif isinstance(data_batch[0], str):
            StreamProcessor.event.process_batch(data_batch)
            StreamProcessor.event_count += 1
        else:
            raise Exception("class not found")

    def get_info(self) -> None:
        """
        print info
        """
        print(f"- Sensor data: {self.sensor_count} readings processed")
        print(f"- Transaction data: {self.tr_count} operations processed")
        print(f"- Event data: {self.event_count} events processed")

    def filter(self) -> None:
        """
        filter the list
        """
        return f"{self.critical} critical sensor alerts, \
{self.large_transaction} large transaction"


def tester():
    """
    A tester function
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:
        print("Initializing Sensor Stream...")
        sensor = SensorStream()
        print("Stream ID: SENSOR_001, Type: Environmental Data")
        batch = [22.5, 65, 1013]
        print(f"Processing sensor batch: {sensor.process_batch(batch)}")
        sensor.get_stats()
    except Exception as e:
        print("Error grap:", e)
    print()

    try:
        print("Initializing Transaction Stream...")
        transaction = TransactionStream()
        print("Stream ID: TRANS_001, Type: Financial Data")
        batch = [100, 150, 75]
        print(f"Processing transaction batch: \
{transaction.process_batch(batch)}")
        transaction.get_stats()
    except Exception as e:
        print("Error grap:", e)
    print()

    try:
        print("Initializing Event Stream...")
        event = EventStream()
        print("Stream ID: EVENT_001, Type: System Events")
        batch = ["login", "error", "logout"]
        print(f"Processing transaction batch: {event.process_batch(batch)}")
        event.get_stats()
    except Exception as e:
        print("Error grap:", e)
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    batchs = [
        [10.0, 5, 113],
        [23.5, 40, 113],
        [10, 15, 7],
        [10, 10, 5],
        [0, 50, 75],
        [1000, 1500, 750],
        ["login", "error", "login"],
        ["login", "error", "error"],
        ["error", "error", "error"],

    ]

    Processor = StreamProcessor()
    print("Batch 1 Results:")
    try:
        for batch in batchs:
            Processor.process_batch(batch)
    except Exception as e:
        print("Error:", e)
    Processor.get_info()

    print("Stream filtering active: High-priority data only")
    print("Filtered results: ", {Processor.filter()})


if __name__ == "__main__":
    tester()