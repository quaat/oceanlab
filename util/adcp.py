from typing import List

NUMBER_OF_LAYERS = 7

def depth(blinding: float, cell_size: float) -> List[float]:
    """Calculate depth values for each layer based on blinding and cell size."""
    if blinding < 0:
        raise ValueError("Bliding must be zero or a positive number.")
    if cell_size <= 0:
        raise ValueError("cell_size must be a positive number.")

    return [blinding + (n - 0.5) * cell_size for n in range(1, NUMBER_OF_LAYERS)]

