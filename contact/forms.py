from django import forms

BANNED_WORDS = ['spam', 'virus', 'casino','nigga','nigger','faggot','shit']


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Adınızı daxil edin'}),
        required=True)
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'E-poçt ünvanınız'}),
        required=True)
    message = forms.CharField(
        label='Message',
        min_length=10,
        widget=forms.Textarea(attrs={'placeholder': 'Mesajınız', 'rows': '6'}),
        required=True)

    def clean_message(self):
        message = self.cleaned_data['message']
        lowered = message.lower()
        for word in BANNED_WORDS:
            if word in lowered:
                raise forms.ValidationError('Mesajda qadağan olunmuş söz aşkarlandı.')
        return message
