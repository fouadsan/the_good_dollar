
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Submit

from .models import ProductReview


# Review Add Form
class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('review_text', id="id_updateReview_text"),
            Field('review_rating', id="id_updateReview_rating"),
        )
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        super(ReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ProductReview
        fields=('review_text', 'review_rating')