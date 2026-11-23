from decimal import Decimal, ROUND_HALF_UP


def _to_decimal(value: float | int | str | Decimal) -> Decimal:
    return Decimal(str(value))


def _round_currency(amount: Decimal) -> float:
    return float(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def deposit(bal: float | int | str | Decimal, amt: float | int | str | Decimal) -> float:
    """Add `amt` to `bal` and return the updated balance."""
    balance = _to_decimal(bal)
    amount = _to_decimal(amt)

    if balance < 0:
        raise ValueError("Balance cannot be negative.")
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    return _round_currency(balance + amount)


def withdraw(bal: float | int | str | Decimal, amt: float | int | str | Decimal) -> float:
    """Subtract `amt` from `bal` if sufficient funds exist and return the updated balance."""
    balance = _to_decimal(bal)
    amount = _to_decimal(amt)

    if balance < 0:
        raise ValueError("Balance cannot be negative.")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Insufficient funds.")

    return _round_currency(balance - amount)

def interest(bal: float | int | str | Decimal, rate: float | int | str | Decimal) -> float:
    """Apply percentage interest `rate` (e.g., 5 for 5%) to `bal` and return the updated balance."""
    balance = _to_decimal(bal)
    interest_rate = _to_decimal(rate)

    if balance < 0:
        raise ValueError("Balance cannot be negative.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    earned = (balance * interest_rate) / Decimal("100")
    return _round_currency(balance + earned)

if __name__ == "__main__":
    current_balance = 1000.00
    current_balance = deposit(current_balance, 250.00)
    current_balance = withdraw(current_balance, 150.00)
    current_balance = interest(current_balance, 5.0)
    print(f"Balance after Phase 1 transactions: {current_balance:.2f}")