import yaml

LEGAL_KEYS = ("Location", "URL")


class ConfigLoader(object):
    @staticmethod
    def load(fhandler):
        """Load expected config data format and sanitize for expected keys"""
        data = yaml.safe_load(fhandler)
        return {
            "RDC_" + k.upper(): v
            for k, v in data.get("rainfall-data-client", {}).items()
            if k in LEGAL_KEYS
        }
