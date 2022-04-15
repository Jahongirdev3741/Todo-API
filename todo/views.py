from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(ModelViewSet):
  serializer_class=TodoSerializer
  permission_classes=(IsAuthenticated,)
  authentication_classes=(TokenAuthentication,)

  def perform_create(self, serializer):
    serializer.validated_data["user"]=self.request.user
    serializer.save()

  def get_queryset(self):
    return Todo.objects.filter(user=self.request.user)
  
  @action(detail=True,methods=['GET'])
  def finished_object(self, request,*args,**kwargs):
    todo=self.get_object()
    todo.mark_as_finished() 
    return Response(status=status.HTTP_200_OK)
  
  @action(detail=True,methods=['GET'])
  def unfinished_object(self, request,*args,**kwargs):
    todo=self.get_object()
    todo.mark_as_unfinished() 
    return Response(status=status.HTTP_200_OK)