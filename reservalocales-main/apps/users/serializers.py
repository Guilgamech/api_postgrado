from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from apps.users.models import Trabajador


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.refresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.refresh).blacklist()

        except TokenError:
            self.fail('Bad Token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = ('id', 'username', 'password', 'email', 'nombre',
                  'apellido', 'telefono_privado', 'telefono_fijo',
                  'area_trabajo', 'tipo_usuario', 'is_active', 'is_superuser')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }
