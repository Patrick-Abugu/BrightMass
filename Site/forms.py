from django import forms
from .import models
class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'title',
            'body',
            'slug',
            'image',]

#class Feedback(forms.ModelForm):
    #class Meta:
        #model = models.Feedback
class FeedbackForm(forms.Form):
    email = forms.EmailField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Enter subject'}) )
    subject = forms.CharField(max_length=100, required = True, widget=forms.TextInput(attrs={'placeholder': 'Enter subject'}))
    message = forms.CharField(required =True, widget= forms.Textarea(attrs ={'placeholder':'Send us your Feedback'}))
