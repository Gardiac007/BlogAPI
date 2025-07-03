from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomToken_Serializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        custom_fields = { 

            'username': self.user.username,
            'date': self.user.date_joined

        }

        data.update(custom_fields)

        return data
