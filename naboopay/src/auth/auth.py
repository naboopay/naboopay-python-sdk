class Auth:
    def __init__(self, token: str):
        self.token = token

        if not token:
            raise ValueError(
                "API token must be provided via parameter or NABOOPAY_API_KEY environment variable"
            )

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
