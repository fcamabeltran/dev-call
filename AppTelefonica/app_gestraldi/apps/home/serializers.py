from django.contrib.auth.models import User
from rest_framework import serializers


# from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = Post
        fields = ('pais_codigo', 'pais_descripcion', 'pais_discado', 'pais_grupo', 'pais_idioma', 'pais_multicarrier',
                  'pais_zona', 'pais_usrcreacion', 'pais_feccreacion', 'pais_usrmodifica', 'pais_fecmodifica',
                  'pais_icono')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username","first_name","last_name")




		