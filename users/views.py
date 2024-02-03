from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from users.serializers import UserSerializer, AuthTokenSerializer



# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user

class CreateTokenView(ObtainAuthToken):
    serializer_class= AuthTokenSerializer

