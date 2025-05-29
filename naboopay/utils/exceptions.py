class NabooPayError(Exception):
    pass


class AuthenticationError(NabooPayError):
    pass


class APIError(NabooPayError):
    pass
