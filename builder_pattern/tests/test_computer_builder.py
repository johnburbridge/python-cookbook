"""Tests for the computer builder module."""

from builder_pattern.computer_builder import ComputerBuilder


def test_computer_builder_minimal():
    """Test building a computer with only required components."""
    builder = ComputerBuilder()
    computer = builder.with_case("ATX Mid Tower").build()

    assert computer.case == "ATX Mid Tower"
    assert computer.cpu is None
    assert computer.memory is None
    assert computer.storage is None
    assert computer.gpu is None
    assert computer.power_supply is None


def test_computer_builder_full():
    """Test building a computer with all components."""
    builder = ComputerBuilder()
    computer = (
        builder.with_case("ATX Full Tower")
        .with_cpu("Intel i9")
        .with_memory("32GB DDR4")
        .with_storage("2TB NVMe SSD")
        .with_gpu("RTX 4090")
        .with_power_supply("1000W Gold")
        .build()
    )

    assert computer.case == "ATX Full Tower"
    assert computer.cpu == "Intel i9"
    assert computer.memory == "32GB DDR4"
    assert computer.storage == "2TB NVMe SSD"
    assert computer.gpu == "RTX 4090"
    assert computer.power_supply == "1000W Gold"


def test_computer_builder_no_case():
    """Test that building a computer without a case raises an error."""
    builder = ComputerBuilder()
    try:
        builder.build()
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Computer case is required"


def test_failing_test():
    """Test that should fail to verify pre-push hook."""
    assert False, "This test should fail"
