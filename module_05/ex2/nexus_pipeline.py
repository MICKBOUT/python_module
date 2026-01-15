from abc import ABC
from typing import Any, Protocol, List


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

    def add_stage(self, stage: ProcessingStage) -> None:
        """
        Add a stage in the pipeline
        """
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        """
        Execute the current process
        """
        try:
            for stage in self.stages:
                data = stage.process(data)
            self.processed_count += 1
            return data
        except Exception as e:
            print("Pipeline error:", e)
            raise


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        """
        Header Json
        """
        print(f"[JSONAdapter {self.pipeline_id}] Processing JSON data")
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        """
        Header CVS
        """
        print(f"[CSVAdapter {self.pipeline_id}] Processing CSV data")
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: int) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        """
        Header StreamAdapter
        """
        print(f"[StreamAdapter {self.pipeline_id}] Processing Stream data")
        return super().process(data)


class InputStage:
    def process(self, data: tuple[tuple[int, str], ...]) -> dict:
        """
        Transform the data into a dict
        """
        return {key: value for key, value in data}


class TransformStage:
    def process(self, data: dict) -> dict:
        """
        Capitalize the value of the dict
        """
        return {k: v.capitalize() for k, v in data.items()}


class OutputStage:
    def process(self, data: dict) -> str:
        """
        Transthe imput into a readable one
        """
        output_str = ""
        for key, value in data.items():
            output_str += f"Number: {key}, word: {value}\n"
        return output_str


class StringToRecordsStage:
    def process(self, data: str) -> tuple[tuple[int, str], ...]:
        """
        Transform the string from the previous pipeline to be usable
        """
        records = []
        for line in data.strip().splitlines():
            left, right = line.split(",")
            num = int(left.replace("Number:", "").strip())
            word = right.replace("word:", "").strip().lower()
            records.append((num, word))
        return tuple(records)


class NexusManager:
    """
    class NexusManager that orchestrates multiple pipelines polymorphically
    """
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def process_data(self, data: Any) -> Any:
        """
        Execute data throug a pipline
        """
        try:
            for pipeline in self.pipelines:
                data = pipeline.process(data)
        except Exception as e:
            print("Error in pipline:", e)
        else:
            print("Pipeline completed")
        return data

    def add_pipeline(self, pipeline: Any) -> None:
        """
        Add a pipeline
        """
        self.pipelines.append(pipeline)


if __name__ == "__main__":
    data = (
        (0, "zero"),
        (1, "one"),
        (2, "two"),
        (3, "three"),
    )

    json_pipeline = JSONAdapter(1)
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())

    csv_pipeline = CSVAdapter(2)
    csv_pipeline.add_stage(StringToRecordsStage())
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())

    Stream_pipeline = StreamAdapter(3)
    Stream_pipeline.add_stage(StringToRecordsStage())
    Stream_pipeline.add_stage(InputStage())
    Stream_pipeline.add_stage(TransformStage())
    Stream_pipeline.add_stage(OutputStage())

    manager = NexusManager()
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(Stream_pipeline)

    result = manager.process_data(data)
    print()

    print("=== FINAL RESULT ===")
    print(result)
