from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Actor
from .serializers import (
    ActorListSerializer,
    ActorDetailSerializer,
)


class ActorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Actor.objects.all()
        serializer = ActorListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Actor.objects.all()
        actor = get_object_or_404(queryset, pk=pk)
        serializer = ActorDetailSerializer(actor)
        # print(self.retrieve.u)
        return Response(serializer.data)



class ActorReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorModelViewSet(viewsets.ModelViewSet):
    serializer_class = ActorListSerializer
    queryset = Actor.objects.all()

    # @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    # def my_list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'put']) #, renderer_classes=[renderers.AdminRenderer])
    def example(self, request, *args, **kwargs):
        actor = self.get_object()
        serializer = ActorDetailSerializer(actor)
        print(self.reverse_action('highlight'))
        self.reverse_action("actor", args=['1']),
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == "example":
    #         permission_classes = [permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]
