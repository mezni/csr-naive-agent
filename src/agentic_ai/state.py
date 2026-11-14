from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    user_message: str

    input_items: list[Any] = field(default_factory=list)

    iteration: int = 0

    status: str = "running"

    observations: list[dict[str, Any]] = field(default_factory=list)

    final_response: str | None = None
