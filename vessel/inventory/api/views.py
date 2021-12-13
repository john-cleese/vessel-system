# import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from vessel.inventory.api.serializers import InventorySerializer
from vessel.inventory.models import Inventory


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 200


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all().order_by("name")
    serializer_class = InventorySerializer

    def destroy(self, request, pk=None):
        pass

    """
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    )
    filter_fields = (
        "name",
    )
    # search_fields = ('nome_empresarial', 'nome_fantasia',)
    """


"""
class ParadaViewSet(ModelViewSet):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        error_msg = {
            "message": "chamada GET deve conter campanha, promotor e data no formato YYYY-MM-DD"
        }
        campanha_id = request.query_params.get("campanha")
        promotor_id = request.query_params.get("promotor")
        data_str = request.query_params.get("data")
        try:
            data = parse_date(data_str)
        except:  # noqa E722
            return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
        if not campanha_id or not promotor_id or not data:
            return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)

        paradas = retorna_queryset_de_paradas(campanha_id, promotor_id, data)
        serializer = ParadaListSerializer(paradas, many=True)
        data = serializer.data
        return Response(data)


class PontoViewSet(ModelViewSet):
    queryset = Ponto.objects.all()
    allowed_methods = ["POST", "PUT", "GET"]
    serializer_class = PontoSerializer
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    )
    filter_fields = ("parada", "parada__loja", "parada__data")


class TarefaDiaViewSet(ModelViewSet):
    queryset = TarefaDia.objects.all()
    allowed_methods = ["PUT", "GET", "POST", "PATCH"]
    serializer_class = TarefaDiaSerializer
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    )
    filter_fields = ("parada", "parada__loja", "parada__data")
    lookup_field = "id"


class RespostaQuestionarioViewSet(ModelViewSet):
    queryset = RespostaQuestionarioTarefa.objects.all()
    allowed_methods = ["POST"]
    serializer_class = RespostaQuestionarioPostSerializer


class FotoTarefaViewSet(ModelViewSet):
    queryset = FotoTarefa.objects.all()
    allowed_methods = ["POST", "PUT"]
    serializer_class = FotoTarefaSerializer

# class LojasCampanhaViewSet(ModelViewSet):
#     queryset = LojasCampanha.objects.all()
#     serializer_class = LojasCampanhaSerializer
#     filter_backends = (
#         django_filters.rest_framework.DjangoFilterBackend,
#         filters.SearchFilter,
#     )
#     filter_fields = ("campanha", "loja__rede")
#     pagination_class = LargeResultsSetPagination
"""
