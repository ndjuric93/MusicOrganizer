from micro_users import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
