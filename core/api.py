from rest_framework import serializers, viewsets
from core.serializers import AutorSerializer

from core.models import Autor


class AutorViewSet(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()
