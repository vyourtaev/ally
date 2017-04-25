from django import forms
from api.models import Stack, Service, Port, Variable, Volume


class StackForm(forms.ModelForm):
    """Stack Form customization"""
    VERSION_CHOICES = (
        ('3.0', '3.0'),
        ('3.1', '3.1'),
        ('3.2', '3.2')
    )

    version = forms.ChoiceField(
        choices=VERSION_CHOICES)
    description = forms.CharField(
        widget=forms.TextInput(attrs={'size': 150}),
        required=False)

    class Meta:
        model = Stack
        fields = ['version', 'name', 'description', 'slug']


class ServiceForm(forms.ModelForm):
    """Service form class"""

    script = forms.FileField()
    description = forms.CharField(
        widget=forms.TextInput(attrs={'size': 100}),
        required=False)

    class Meta:
        model = Service
        fields = ['name', 'description', 'image_name', 'script']


class VariableForm(forms.ModelForm):
    """Environment Variable Form customization"""

    value = forms.CharField(widget=forms.TextInput(attrs={'size': 150}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'size': 150}),
        required=False)

    class Meta:
        model = Variable
        fields = ['name', 'value', 'description']


class VolumeForm(forms.ModelForm):
    """Volume s Form"""

    class Meta:
        model = Volume
        fields = ['name', 'volume', 'description']


class ServiceUploadForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
            data = self.cleaned_data["file"]
            # read and parse the file, create a Python dictionary `data_dict` from it
            form = ServiceForm(data_dict)
            if form.is_valid():
                # we don't want to put the object to the database on this step
                self.instance = form.save(commit=False)
            else:
                # You can use more specific error message here
                raise forms.ValidationError(u"The file contains invalid data.")
            return data

    def save(self):
            # We are not overriding the `save` method here because `form.Form` does not have it.
            # We just add it for convenience.
            instance = getattr(self, "instance", None)
            if instance:
                instance.save()
            return instance
