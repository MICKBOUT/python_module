from abc import ABC, abstractmethod
from typing import Any, Protocol, List
from time import time


class ProcessingStage(Protocol):
    """
    A blueprint of how to create a process Stage in this file
    """
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    """
    class ProcessingPipeline: an abstract base class with configurable stages
    """
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        self.processed_count = 0
        self.total_time = 0.0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        start = time.time()
        try:
            for stage in self.stages:
                data = stage.process(data)
            self.processed_count += 1
            return data
        except Exception as e:
            print("Pipeline error:", e)
            raise
        finally:
            self.total_time += time.time() - start



# init w/ pipline id ?
class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> None:
        """
        Process the data in arg
        """
        data
        ...


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> None:
        """
        Process the data in arg
        """
        data
        ...


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> None:
        """
        Process the data in arg
        """
        data
        ...




class InputStage(ProcessingStage):
    def process(self, data: tuple[int, str]) -> dict:
        """
        Convert the data to a dict
        """
        intput_dict = {}
        try:
            for key, value in data:
                intput_dict[key] = value
        except Exception as e:
            raise e
        return intput_dict


class TransformStage:
    def process(self, data: dict) -> dict:
        """
        Capitalize the value of the dict
        """
        transform_dict = {}
        try:
            for key, value in data.items():
                transform_dict[key] = value.capitalize()
        except Exception as e:
            raise e
        return transform_dict


class OutputStage:
    def process(self, data) -> str:
        output_str = ""
        try:
            for key, value in data.items():
                output_str += f"Number: {key}, word: {value}\n"
        except Exception as e:
            raise e
        return output_str


class NexusManager:
    """
    class NexusManager that orchestrates multiple pipelines polymorphically
    """
    def __init__(self):
        self.stages = []

    def process_data(self, data) -> bool:
        """
        Execute data throug a pipline
        """
        try:
            for pipeline in self.stages:
                buffer = data
                buffer = pipeline.process(data)
                data = buffer
        except Exception as e:
            print("Error in pipline:", e)
        else:
            print("Pipeline completed")
        print("data at exit :")
        print(data)
        return True

    def add_pipline(self, pipeline) -> None:
        """
        Add a pipeline
        """
        self.stages.append(pipeline)


manager = NexusManager()

input_stage = InputStage()
transform_stage = TransformStage()
output_stage = OutputStage()

manager.add_pipline(input_stage)
manager.add_pipline(transform_stage)
manager.add_pipline(output_stage)

data = (
    (0, "zero"),
    (1, "one"),
    (3, "three"),
    (4, "four"),
)

manager.process_data(data)
