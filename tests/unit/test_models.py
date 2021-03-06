"""
This file (test_models.py) containes the unit tests for the models.py file.
"""
from project.models import Stock


def test_new_stock(new_stock):
    """
    GIVEN a Stock models
    WHEN a new stock object is created
    THEN check the symbol, number of shares, and purchase price fields are defined correctly
    """
    assert new_stock.stock_symbol == "AAPL"
    assert new_stock.number_of_shares == 16
    assert new_stock.purchase_price == 40678


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User object is created
    THEN check the email is valid and hashed password does not equal the password provided
    """
    assert new_user.email == "abesadze.george@gmail.com"
    assert new_user.password_hashed != "FlaskIsAwesome123"


def test_set_password(new_user):
    """
    GIVEN a User model
    WHEN the user's password is changed
    THEN check the password has been changed
    """
    new_user.set_password("FlaskIsStillAwesome456")
    assert new_user.email == "abesadze.george@gmail.com"
    assert new_user.password_hashed != "FlaskIsStillAwesome456"
    assert new_user.is_password_correct("FlaskIsStillAwesome456")
