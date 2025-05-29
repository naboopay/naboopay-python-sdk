from naboopay.models import CodeStatusExceptions, ExceptionMessage

from .exceptions import APIError


def api_exception(code: int, error: Exception) -> Exception:
    return CodeStatusExceptions.exceptions.get(code, APIError)(
        ExceptionMessage.messages.get(code, ExceptionMessage.default.format(str(error)))
    )


def general_exception(error: Exception) -> Exception:
    return CodeStatusExceptions.default(ExceptionMessage.default.format(str(error)))
