class GovApiClient(object):
    def __init__(self) -> None:
        self.url = "https://api.data.gov.sg/v1/environment/rainfall"

    def get(self, location, timestamp=None):
        pass
