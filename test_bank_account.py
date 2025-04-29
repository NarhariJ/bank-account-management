# test_bank_account.py

import pytest
from bank_account import BankAccount  # Import the BankAccount class

def test_deposit_positive_amount():
    account = BankAccount("John", 100.0)
    new_balance = account.deposit(50.0)
    assert new_balance == 150.0  # Check if the balance updated correctly

def test_deposit_negative_amount():
    account = BankAccount("John", 100.0)
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account.deposit(-50.0)  # Check if depositing negative amount raises an error

def test_withdraw_valid_amount():
    account = BankAccount("John", 100.0)
    new_balance = account.withdraw(50.0)
    assert new_balance == 50.0  # Check if the balance updated correctly

def test_withdraw_more_than_balance():
    account = BankAccount("John", 100.0)
    with pytest.raises(ValueError, match="Insufficient balance."):
        account.withdraw(150.0)  # Check if withdrawing more than balance raises an error

def test_withdraw_negative_amount():
    account = BankAccount("John", 100.0)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        account.withdraw(-50.0)  # Check if withdrawing a negative amount raises an error

def test_get_balance():
    account = BankAccount("John", 100.0)
    balance = account.get_balance()
    assert balance == 100.0  # Check if the balance is correctly returned
