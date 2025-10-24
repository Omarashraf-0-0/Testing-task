"""
Unit Tests for User Validation Module

This test suite covers all validation methods in the UserValidation class
following the AAA (Arrange, Act, Assert) pattern with descriptive test names.
"""

import pytest
from user_validation import UserValidation


def test_valid_email_returns_true():
    """Test that a standard valid email address is accepted."""
    email = "user@example.com"
    result = UserValidation.checkEmail(email)
    assert result is True, "Valid email should return True"


def test_email_without_at_symbol_returns_false():
    """Test that an email without @ symbol is rejected."""
    email = "userexample.com"
    result = UserValidation.checkEmail(email)
    assert result is False, "Email without @ symbol should return False"


def test_email_without_domain_returns_false():
    """Test that an email without domain name is rejected."""
    email = "user@"
    result = UserValidation.checkEmail(email)
    assert result is False, "Email without domain should return False"


def test_email_with_short_tld_returns_false():
    """Test that an email with TLD shorter than 2 characters is rejected."""
    email = "user@mail.c"
    result = UserValidation.checkEmail(email)
    assert result is False, "Email with single-letter TLD should return False"


def test_email_with_subdomain_returns_true():
    """Test that an email with subdomain is accepted."""
    email = "user@mail.company.com"
    result = UserValidation.checkEmail(email)
    assert result is True, "Email with subdomain should return True"


def test_email_with_special_chars_in_local_part_returns_true():
    """Test that an email with dots, underscores, and hyphens is accepted."""
    email = "ramy.gomaa_21@mail.co"
    result = UserValidation.checkEmail(email)
    assert result is True, "Email with valid special characters should return True"


def test_email_with_uppercase_returns_true():
    """Test that email validation is case-insensitive."""
    email = "USER@MAIL.COM"
    result = UserValidation.checkEmail(email)
    assert result is True, "Uppercase email should return True (case-insensitive)"


def test_email_with_space_returns_false():
    """Test that an email containing spaces is rejected."""
    email = "user name@mail.com"
    result = UserValidation.checkEmail(email)
    assert result is False, "Email with spaces should return False"


def test_empty_email_returns_false():
    """Test that an empty string is rejected."""
    email = ""
    result = UserValidation.checkEmail(email)
    assert result is False, "Empty email should return False"


def test_none_email_returns_false():
    """Test that None input is handled gracefully."""
    email = None
    result = UserValidation.checkEmail(email)
    assert result is False, "None email should return False"


def test_valid_username_returns_true():
    """Test that a valid username with letters and digits is accepted."""
    username = "john_doe123"
    result = UserValidation.checkUsername(username)
    assert result is True, "Valid username should return True"


def test_username_too_short_returns_false():
    """Test that a username shorter than 3 characters is rejected."""
    username = "ab"
    result = UserValidation.checkUsername(username)
    assert result is False, "Username with less than 3 characters should return False"


def test_username_too_long_returns_false():
    """Test that a username longer than 20 characters is rejected."""
    username = "this_username_is_way_too_long"
    result = UserValidation.checkUsername(username)
    assert result is False, "Username with more than 20 characters should return False"


def test_username_with_special_chars_returns_false():
    """Test that a username with special characters (other than underscore) is rejected."""
    username = "user@name"
    result = UserValidation.checkUsername(username)
    assert result is False, "Username with special characters should return False"


def test_username_with_space_returns_false():
    """Test that a username containing spaces is rejected."""
    username = "user name"
    result = UserValidation.checkUsername(username)
    assert result is False, "Username with spaces should return False"


def test_username_exactly_3_chars_returns_true():
    """Test that a username with exactly 3 characters (minimum) is accepted."""
    username = "abc"
    result = UserValidation.checkUsername(username)
    assert result is True, "Username with exactly 3 characters should return True"


def test_empty_username_returns_false():
    """Test that an empty string is rejected."""
    username = ""
    result = UserValidation.checkUsername(username)
    assert result is False, "Empty username should return False"


def test_none_username_returns_false():
    """Test that None input is handled gracefully."""
    username = None
    result = UserValidation.checkUsername(username)
    assert result is False, "None username should return False"


def test_valid_phone_starting_with_010_returns_true():
    """Test that a valid 11-digit phone number starting with 010 is accepted."""
    phone = "01012345678"
    result = UserValidation.checkPhone(phone)
    assert result is True, "Valid phone starting with 010 should return True"


def test_valid_phone_starting_with_011_returns_true():
    """Test that a valid 11-digit phone number starting with 011 is accepted."""
    phone = "01112345678"
    result = UserValidation.checkPhone(phone)
    assert result is True, "Valid phone starting with 011 should return True"


def test_valid_phone_starting_with_012_returns_true():
    """Test that a valid 11-digit phone number starting with 012 is accepted."""
    phone = "01212345678"
    result = UserValidation.checkPhone(phone)
    assert result is True, "Valid phone starting with 012 should return True"


def test_valid_phone_starting_with_015_returns_true():
    """Test that a valid 11-digit phone number starting with 015 is accepted."""
    phone = "01512345678"
    result = UserValidation.checkPhone(phone)
    assert result is True, "Valid phone starting with 015 should return True"


def test_valid_phone_with_country_code_20_returns_true():
    """Test that a valid 12-digit phone with country code 20 is accepted."""
    phone = "201012345678"
    result = UserValidation.checkPhone(phone)
    assert result is True, "Valid phone with country code 20 should return True"


def test_phone_starting_with_013_returns_false():
    """Test that a phone number starting with 013 (invalid prefix) is rejected."""
    phone = "01312345678"
    result = UserValidation.checkPhone(phone)
    assert result is False, "Phone starting with 013 should return False"


def test_phone_with_10_digits_returns_false():
    """Test that a phone number with only 10 digits is rejected."""
    phone = "0101234567"
    result = UserValidation.checkPhone(phone)
    assert result is False, "Phone with 10 digits should return False"


def test_phone_with_12_digits_returns_false():
    """Test that a phone number with 12 digits but wrong prefix is rejected."""
    phone = "011234567890"
    result = UserValidation.checkPhone(phone)
    assert result is False, "Phone with 12 digits and wrong prefix should return False"


def test_phone_with_letters_returns_false():
    """Test that a phone number containing letters is rejected."""
    phone = "0101234567a"
    result = UserValidation.checkPhone(phone)
    assert result is False, "Phone with letters should return False"


def test_phone_with_spaces_returns_false():
    """Test that a phone number containing spaces is rejected."""
    phone = "010 1234 5678"
    result = UserValidation.checkPhone(phone)
    assert result is False, "Phone with spaces should return False"


def test_empty_phone_returns_false():
    """Test that an empty string is rejected."""
    phone = ""
    result = UserValidation.checkPhone(phone)
    assert result is False, "Empty phone should return False"


def test_none_phone_returns_false():
    """Test that None input is handled gracefully."""
    phone = None
    result = UserValidation.checkPhone(phone)
    assert result is False, "None phone should return False"


def test_valid_national_id_century_2_returns_true():
    """Test that a valid national ID with century code 2 is accepted."""
    national_id = "29001011234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is True, "Valid national ID with century 2 should return True"


def test_valid_national_id_century_3_returns_true():
    """Test that a valid national ID with century code 3 is accepted."""
    national_id = "30112011234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is True, "Valid national ID with century 3 should return True"


def test_national_id_with_invalid_century_returns_false():
    """Test that a national ID with invalid century code (not 2 or 3) is rejected."""
    national_id = "19001011234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with century 1 should return False"


def test_national_id_with_invalid_month_returns_false():
    """Test that a national ID with invalid month (13) is rejected."""
    national_id = "29013011234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with month 13 should return False"


def test_national_id_with_month_00_returns_false():
    """Test that a national ID with month 00 is rejected."""
    national_id = "29000011234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with month 00 should return False"


def test_national_id_with_invalid_day_returns_false():
    """Test that a national ID with invalid day (32) is rejected."""
    national_id = "29001321234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with day 32 should return False"


def test_national_id_with_day_00_returns_false():
    """Test that a national ID with day 00 is rejected."""
    national_id = "29001001234567"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with day 00 should return False"


def test_national_id_with_invalid_governorate_returns_false():
    """Test that a national ID with invalid governorate code (89) is rejected."""
    national_id = "29001018912345"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with governorate 89 should return False"


def test_national_id_with_13_digits_returns_false():
    """Test that a national ID with only 13 digits is rejected."""
    national_id = "2900101123456"
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "National ID with 13 digits should return False"


def test_none_national_id_returns_false():
    """Test that None input is handled gracefully."""
    national_id = None
    result = UserValidation.checkNationalId(national_id)
    assert result is False, "None national ID should return False"
