from django.forms import ModelForm
from countries.models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments

