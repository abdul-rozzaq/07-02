from django import forms
from .models import Food, Order
from django import forms
from .models import Food


class FoodForm(forms.ModelForm):

    image = forms.ImageField(widget=forms.FileInput(attrs={"accept": "image/*"}), required=False)

    class Meta:
        model = Food
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}
