class ModelForm(object):
    def __init__(self, model):
        self.data = {}
        self.model = model
        no_params = ["metadata", "query", "query_class"]
        self.attributes = [
            i for i in dir(self.model) if not i.startswith("_") and i not in no_params
        ]
        self.ignore = []

    def is_valid(self):
        for key, value in self.data.items():
            if key in self.attributes:
                if (value == "" or not value) and key not in self.ignore:
                    return False

        return True

    def get(self, attr):
        return self.data.get(attr)
