from datetime import datetime

import requests


class FormatterRawValue(object):
    def format(payload):
        return str(payload["value"])


class FormatterCSV(FormatterRawValue):
    def format(payload):
        amount = payload["value"]
        raining = "Raining" if amount > 0 else "Not Raining"
        time = payload["time"].strftime("%H:%M")
        return f'{payload["name"]}, {time}, {amount}mm, {raining}'


class GovApiClient(object):
    def __init__(self, url=None, formatter=None):
        self.url = url or "https://api.data.gov.sg/v1/environment/rainfall"
        self.formatter = formatter or FormatterRawValue

    def get(self, location, timestamp=None):
        if timestamp:
            params = {"date_time": timestamp.strftime("%Y-%m-%dT%H:%M:%S")}
        else:
            params = None
        response = requests.get(self.url, params)
        response.raise_for_status()
        data = response.json()
        station_id = next(
            (
                station["id"]
                for station in data.get("metadata", {}).get("stations", [])
                if station["name"] == location
            ),
            None,
        )
        if station_id is None:
            return None
        payload = {
            "name": location,
            "time": datetime.strptime(
                data["items"][0]["timestamp"], "%Y-%m-%dT%H:%M:%S%z"
            ),
            "value": next(
                (
                    r["value"]
                    for r in data["items"][0]["readings"]
                    if r["station_id"] == station_id
                ),
                None,
            ),
        }
        return self.formatter.format(payload)

    def set_formatter(self, formatter):
        self.formatter = formatter
