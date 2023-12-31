from django.forms import ModelForm
from users.models import CostumeUser


class UserCreateForm(ModelForm):
    class Meta:
        model = CostumeUser
        fields = ('first_name', 'last_name',  'password', 'phone_number', 'avatar')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user


class UserEditForm(ModelForm):
    class Meta:
        model = CostumeUser
        fields = ('first_name', 'last_name', 'email')

