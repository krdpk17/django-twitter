from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('bio', 'location')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')            

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'birth_date', 
            'twitter_consumer_key', 'twitter_consumer_secret', 'twitter_user_key', 'twitter_user_secret')


'''
Section for update data
'''
class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditUserProfileForm(forms.ModelForm):
    """
    This class is a carbon copy of the UserChangeForm class from
    django.contrib.auth.forms, with the password functionality deleted, and
    the form is modified to allow changes to be made to the
    UserProfle, which extends the Django User
    """
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'birth_date', 
            'twitter_consumer_key', 'twitter_consumer_secret', 'twitter_user_key', 'twitter_user_secret')

    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
