from dataclasses import dataclass

@dataclass(slots = True)
class SamplingParams:
    temperature: float = 1.0
    max_tokens: int = 64
    ignore_eos = False

    def __post__init__(self):
        assert self.temperature > 1e-10, "greedy sampling is not permitted"