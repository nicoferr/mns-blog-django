from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(
        label='Votre commentaire',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': "Ecrivez votre commentaire ici..."
        })
    )
