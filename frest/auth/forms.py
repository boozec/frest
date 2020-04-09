from .models import User
from frest.forms import ModelForm


class UserForm(ModelForm):
    model = User

    def __init__(self, data):
        super().__init__(self.model)
        self.data = data
