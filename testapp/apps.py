from django.apps import AppConfig


class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'


# extra_kwargs = {
#             "password":{"write_only":True}
#         }
    # def validate(self,attrs):
    #     password = attrs.get('password')
    #     password2 = attrs.get('password2')
    #     if password != password2:
    #         raise serializers.ValidationError("password and confirm_password doesn't match")
    #     return attrs

    # def create(self, validate_data):
    #     return User.objects.create_user(**validate_data)
    

# change_password

# password = serializers.CharField(max_length=255,
#                                      style={"input_type":"password"},write_only=True)
#     password2 = serializers.CharField(max_length=255,
#                                       style={"input_type":"password"},write_only=True)
    

#  def validate(self,attrs):
#         password = attrs.get('password')
#         password2 = attrs.get('password2')
#         user = self.context.get('user')
#         if password != password2:
#             raise serializers.ValidationError("password and confirm password doesn`t match")
#         user.set_password(password)
#         user.save()
#         return attrs
            