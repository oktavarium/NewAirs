from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Имя:")
    user_town = forms.CharField(label="Город:")
    user_text = forms.CharField(label="Отзыв:", widget=forms.Textarea)

    def save_review(self):
        print(self.user_name, self.user_town, self.user_text)

    def is_valid(self):
        valid = super(ReviewForm, self).is_valid()
        print("CHECK VALID", self.cleaned_data, valid)
        return False