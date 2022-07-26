from typing import Dict

from services.v1.common.errors.types import ErrorType


class PredefinedErrorMetaClass(type):
    def __new__(mcs, class_name, bases, attrs, **kwargs):
        error_base_class = super().__new__(mcs, class_name, bases, attrs, **kwargs)
        for error_name, error_args in attrs.items():
            if not error_name.isupper():
                continue
            error_class_name = class_name + '.' + error_name
            error_cls = type(error_class_name, (error_base_class, ), {
                'error_code': error_args[0],
                'error_type': error_args[1],
                'http_status_code': error_args[2],
                'message': error_args[3],
            })
            setattr(error_base_class, error_name, error_cls)

        return error_base_class


class PredefinedError(Exception, metaclass=PredefinedErrorMetaClass):
    error_code: str = None
    error_type: ErrorType = None
    http_status_code: int = None
    message: str = None
    details: Dict = {}
    cause: Exception = None
