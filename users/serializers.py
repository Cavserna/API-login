from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['nombre_usuario', 'contrasena', 'rol','sucursal']
        extra_kwargs = {'contrasena': {'write_only': True}}
        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance,validated_data):
        contrasena = validated_data.pop('contrasena', None)
        user = super().update(instance,validated_data)
        
        if contrasena:
            user.set_contrasena(contrasena)
            user.save()
            
        return user
    
class AuthTokenSerializer(serializers.Serializer):
    nombre_usuario = serializers.CharField()
    contrasena = serializers.CharField(style={'input_type' : 'contrasena'})
    
    def validate(self, data):
        nombre_usuario = data.get ('nombre_usuario')
        contrasena= data.get ('contrasena')
        user = authenticate(
            request=self.context.get('request'),
            username=nombre_usuario,
            contrasena=contrasena
        )
        
        if not user:
            raise serializers.ValidationError("No se pudo autenticar", code= "authorization")
        
        data['user'] = user
        return data
    
    
