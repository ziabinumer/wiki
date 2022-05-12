from django import forms

class newEntry(forms.Form):
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                 "class": "mb-4"
                 }
        ),
    )
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Markdown for content",
                "id": "content",
            }
        ),
    )

class editEntry(forms.Form):
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Markdown for content",
                "id": "content",
            }
        ),
    )