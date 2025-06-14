from naboopay.utils.utils import is_valid_uuid

class Auth:
    def __init__(self, token: str):
        self.token = token
        print(self.token.split("naboo-")[1])
        if is_valid_uuid(self.token.split("naboo-")[1]) and "naboo-" in self.token:
            raise ValueError(
                "API token must be provided via parameter or NABOO_API_KEY environment variable"
            )

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
