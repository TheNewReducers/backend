import json


class Product:

    def __init__(self, name: str, co2_emission=None, agriculture=None, consumption=None, distribution=None,
                 packaging=None,
                 processing=None, total=None, transportation=None):
        self.name = name
        self.co2_emission = co2_emission
        self.agriculture = agriculture
        self.consumption = consumption
        self.distribution = distribution
        self.packaging = packaging
        self.processing = processing
        self.total = total
        self.transportation = transportation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
