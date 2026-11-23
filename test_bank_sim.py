import pytest
from bank_sim import deposit, interest, withdraw


def test_deposit_success():
    assert deposit(1000, 250.50) == 1250.50


def test_deposit_invalid_amount():
    with pytest.raises(ValueError, match="greater than zero"):
        deposit(1000, 0)


def test_withdraw_success():
    assert withdraw(1000, 400) == 600.00


def test_withdraw_insufficient_funds():
    with pytest.raises(ValueError, match="Insufficient funds"):
        withdraw(200, 500)


def test_interest_calculation():
    assert interest(1000, 5) == 1050.00
    assert interest(1000, 0) == 1000.00


def test_interest_negative_rate():
    with pytest.raises(ValueError, match="cannot be negative"):
        interest(1000, -2)