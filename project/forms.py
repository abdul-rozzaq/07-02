from django import forms
from .models import Food, Order
from django import forms
from .models import Food


class FoodForm(forms.Form):
    image = forms.ImageField(label="Mahsulot rasmi", required=True)
    title = forms.CharField(max_length=128, label="Nomi")
    price = forms.IntegerField(label="Narxi")

    def __init__(self, *args, **kwargs) -> None:
        instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields["image"].required = False

        for field_name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def create(self):

        return Food.objects.create(**self.cleaned_data)

    def update(self, instance: Food):
        instance.title = self.cleaned_data["title"]
        instance.price = self.cleaned_data["price"]

        if self.cleaned_data.get("image"):
            instance.image = self.cleaned_data["image"]

        instance.save()

        return instance


class OrderForm(forms.Form):
    food = forms.ModelChoiceField(queryset=Food.objects.all(), label="Mahsulot")
    count = forms.IntegerField(label="Soni")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_count(self):
        count = self.cleaned_data.get("count", -1)

        if count <= 0:
            raise ValueError("Mahsulot soni 0 dan katta bo'lishi kerak")

        return count

    def create(self):
        return Order.objects.create(**self.cleaned_data)
