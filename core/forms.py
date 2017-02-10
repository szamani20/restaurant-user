from django.contrib.auth.forms import UserCreationForm
from .models import Member


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for f in iter(self.fields):
            print(f)
            f = self.fields[f]
            if f.required:
                f.widget.attrs.update({'class': 'required'})

    class Meta:
        model = Member
        fields = (
            'email',
        )
        help_texts = {

        }
        labels = {

        }
