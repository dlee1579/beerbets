from rest_framework import viewsets
from users.api.serializers import UserSerializer
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()
        # return super().get_queryset()