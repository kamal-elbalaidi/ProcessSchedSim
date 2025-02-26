import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List


@dataclass
class Process:
    id: int
    arrival: int
    burst: int
    priority: int
    remaining: int = 0

    def __post_init__(self):
        self.remaining = self.burst
