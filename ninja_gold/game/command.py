from typing import Protocol

class Command(Protocol):
    def execute(self, target) -> None:
        ...

    def describe_string() -> str:
        ...

    def display_name() -> str:
        ...

    def result_string() -> str:
        ...