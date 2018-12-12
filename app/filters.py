from django_filters import FilterSet
from django_filters import filters

from .models import Item

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順)'

class ItemFilter(FilterSet):

    name = filters.CharFilter(label="Name", loolup_expr="contains")
    memo = filters.CharFilter(label="Other", lookup_expr ="contains")

    order_by = MyOrderingFilter(

        fields=(
            ("name", "name"),
            ("age", "age"),
        ),
        field_labels = {
            "name": "Name",
            "age": "Age",
        },
        label = "order_by"
    )    


    class Meta:
        model = Item
        fields = ("name", "sex", "memo",)