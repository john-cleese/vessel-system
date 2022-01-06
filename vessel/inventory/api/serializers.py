from rest_framework.serializers import ModelSerializer

from vessel.inventory.models import Inventory


class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            "pk",
            "name",
            "qtd",
        )
        extra_kwargs = {
            "pk": {"read_only": True},
        }
