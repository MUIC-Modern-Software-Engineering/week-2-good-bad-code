# Your task is to implement this and write test.
# This is much more nuance than it looks.
from decimal import Decimal
from enum import Enum
from datetime import date


# Depreciation is a method to calculate the value of an asset over time.
# For example, if you buy a car for 100,000 THB, after 1 year, the value of the car
# is not 100,000 THB anymore. It's probably 80,000 THB. Meaning, the car is depreciated by 20,000 THB.
# This is useful for amortizing the cost of an asset over time thus lowering total tax.

# This is an excerpt from Thailand Tax Code.
# Clause 4.xxx
# Depreciation for computer and computer peripherals.
# The company may choose one of the following schemes to calculate
# depreciation for computer and computer peripherals.
# 1. Straight line depreciation Equally for 3 years.
# 2. Front load Depreciation. Depreciate 40% of the value right after purchase.
#   Then, depreciate the remaining value using 1).
# ref: https://www.rd.go.th/2369.html

class TaxMode(Enum):
    STRAIGHT_LINE = 1
    FRONT_LOAD = 2


def remaining_value(value: Decimal, purchase_date: date, current_date: date, tax_mode: TaxMode) -> Decimal:
    """Calculate remaining value of an asset.

    Args:
        value (Decimal): Purchase value
        purchase_date (date): Purchase date
        current_date (date): Current date
        tax_mode (TaxMode): Tax mode

    Returns:
        Decimal: Remaining value
    """
    if tax_mode == TaxMode.STRAIGHT_LINE:
        return value * Decimal(1 - (current_date.year - purchase_date.year) / 3)
    elif tax_mode == TaxMode.FRONT_LOAD:
        if current_date.year == purchase_date.year:
            return value * Decimal(0.6)
        else:
            return value * Decimal(0.6) * Decimal(1 - (current_date.year - purchase_date.year - 1) / 3)
