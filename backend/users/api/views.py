from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response
from users.api.serializers import UserSerializer
from users.models import User
from . import serializers
from django.contrib.auth import login, authenticate

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()
        # return super().get_queryset()
    

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)
        
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # serializer = serializers.LoginSerializer(data=request.data, context={'request': self.request})
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # login(request, user)
        # return Response(None, status=status.HTTP_202_ACCEPTED)