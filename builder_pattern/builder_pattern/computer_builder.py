"""Module for building computers using the builder pattern."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Computer:
    """Represents a computer with various components."""

    case: str
    cpu: Optional[str] = None
    memory: Optional[str] = None
    storage: Optional[str] = None
    gpu: Optional[str] = None
    power_supply: Optional[str] = None


class ComputerBuilder:
    """Builder class for creating Computer instances."""

    def __init__(self) -> None:
        """Initialize an empty computer builder."""
        self._case: Optional[str] = None
        self._cpu: Optional[str] = None
        self._memory: Optional[str] = None
        self._storage: Optional[str] = None
        self._gpu: Optional[str] = None
        self._power_supply: Optional[str] = None

    def with_case(self, case: str) -> "ComputerBuilder":
        """Set the computer case."""
        self._case = case
        return self

    def with_cpu(self, cpu: str) -> "ComputerBuilder":
        """Set the CPU."""
        self._cpu = cpu
        return self

    def with_memory(self, memory: str) -> "ComputerBuilder":
        """Set the memory."""
        self._memory = memory
        return self

    def with_storage(self, storage: str) -> "ComputerBuilder":
        """Set the storage."""
        self._storage = storage
        return self

    def with_gpu(self, gpu: str) -> "ComputerBuilder":
        """Set the GPU."""
        self._gpu = gpu
        return self

    def with_power_supply(self, power_supply: str) -> "ComputerBuilder":
        """Set the power supply."""
        self._power_supply = power_supply
        return self

    def build(self) -> Computer:
        """Build and return the computer."""
        if not self._case:
            raise ValueError("Computer case is required")

        return Computer(
            case=self._case,
            cpu=self._cpu,
            memory=self._memory,
            storage=self._storage,
            gpu=self._gpu,
            power_supply=self._power_supply,
        )
