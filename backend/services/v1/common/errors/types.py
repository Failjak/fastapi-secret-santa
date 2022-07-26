from enum import Enum


class ErrorType(Enum):
    TECHNICAL = "TECHNICAL"
    VALIDATION = "VALIDATION"
    BUSINESS = "BUSINESS"
