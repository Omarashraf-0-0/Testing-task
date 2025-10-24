import re
from typing import Optional


class UserValidation:
    """Validation class for user input data"""
    
    # Validation patterns
    EMAIL_PATTERN = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    USERNAME_PATTERN = r'^[a-zA-Z0-9_]{3,20}$'
    LOCAL_PHONE_PATTERN = r'^(010|011|012|015)\d{8}$'
    INTERNATIONAL_PHONE_PATTERN = r'^20(10|11|12|15)\d{8}$'
    NATIONAL_ID_PATTERN = r'^\d{14}$'
    
    @staticmethod
    def _isNullOrEmpty(value: Optional[str]) -> bool:
        """Check if value is None or empty string"""
        return value is None or value == ""
    
    @staticmethod
    def _checkIdDate(nationalId: str) -> bool:
        """Validate date components of national ID"""
        month = int(nationalId[3:5])
        day = int(nationalId[5:7])
        
        if month < 1 or month > 12:
            return False
        
        if day < 1 or day > 31:
            return False
        
        return True
    
    @staticmethod
    def _checkIdCentury(nationalId: str) -> bool:
        """Validate century code in national ID"""
        century = nationalId[0]
        return century in ['2', '3']
    
    @staticmethod
    def _checkIdGovernorate(nationalId: str) -> bool:
        """Validate governorate code in national ID"""
        governorate = int(nationalId[7:9])
        return 1 <= governorate <= 88
    
    @staticmethod
    def checkUsername(username: Optional[str]) -> bool:
        """Validate username format"""
        if UserValidation._isNullOrEmpty(username):
            return False
        
        return re.match(UserValidation.USERNAME_PATTERN, username) is not None
    
    @staticmethod
    def checkEmail(email: Optional[str]) -> bool:
        """Validate email address format"""
        if UserValidation._isNullOrEmpty(email):
            return False
        
        return re.match(UserValidation.EMAIL_PATTERN, email) is not None
    
    @staticmethod
    def checkPhone(phone: Optional[str]) -> bool:
        """Validate Egyptian phone number (local or international format)"""
        if UserValidation._isNullOrEmpty(phone):
            return False
        
        return (re.match(UserValidation.LOCAL_PHONE_PATTERN, phone) is not None or 
                re.match(UserValidation.INTERNATIONAL_PHONE_PATTERN, phone) is not None)
    
    @staticmethod
    def checkNationalId(nationalId: Optional[str]) -> bool:
        """Validate Egyptian national ID number"""
        if UserValidation._isNullOrEmpty(nationalId):
            return False
        
        if not re.match(UserValidation.NATIONAL_ID_PATTERN, nationalId):
            return False
        
        if not UserValidation._checkIdCentury(nationalId):
            return False
        
        if not UserValidation._checkIdDate(nationalId):
            return False
        
        if not UserValidation._checkIdGovernorate(nationalId):
            return False
        
        return True
