from concurrent.futures import Future, ThreadPoolExecutor
from typing import Any, Callable


class LockpickExecutor:

    executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=2)

    @classmethod
    def execute(cls, callable: Callable[..., Any | None]) -> Future:
        return cls.executor.submit(callable)
