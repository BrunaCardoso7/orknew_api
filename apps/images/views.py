# apps/images/views.py
from rest_framework import viewsets, status
from .models import Images
from .serializers import ImageSerializer, ImageCreateSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer  # Para leitura

    def get_serializer_class(self):
        """Usar serializer diferente para CREATE"""
        if self.action == 'create':
            return ImageCreateSerializer  # Para criar - aceita arquivos
        return ImageSerializer  # Para ler - formata URLs

    def create(self, request, *args, **kwargs):
        print(f"🔍 DEBUG request.data: {request.data}")
        print(f"🔍 DEBUG request.FILES: {request.FILES}")

        # Usar o serializer de criação
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        print(f"🔍 DEBUG instance criada: ID={instance.id}, image='{instance.image}'")

        # Retornar usando o serializer de leitura para formatar URL
        read_serializer = ImageSerializer(instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def images_profile(self, request, *args, **kwargs):
        print(f"🔍 DEBUG request.data: {request.data}")
        print(f"🔍 DEBUG request.FILES: {request.FILES}")

        # Usar o serializer de criação
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        print(f"🔍 DEBUG instance criada: ID={instance.id}, image='{instance.image}'")

        # Retornar usando o serializer de leitura para formatar URL
        read_serializer = ImageSerializer(instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        instances = Images.objects.all()
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ImageCreateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Retornar com URL formatada
        read_serializer = ImageSerializer(instance)
        return Response(read_serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)