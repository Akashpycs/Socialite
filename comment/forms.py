from django import forms
from comment.models import Comment
from mptt.forms import TreeNodeChoiceField


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('parent', 'content',)

    content = forms.CharField(required=True, label="",  widget=forms.Textarea(
        attrs={'placeholder': 'Comment', 'class': "form-control", }))
    parent = TreeNodeChoiceField(
        required=False, label="", queryset=Comment.objects.all())
