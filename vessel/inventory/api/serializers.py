from rest_framework.serializers import ModelSerializer

from vessel.inventory.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "pk",
            "name",
            "qtd",
        )
        extra_kwargs = {
            "pk": {"read_only": True},
        }
