from app.models import User, UserProfile


class UserService:

    @classmethod
    def create_user(cls, **data):
        email = data.get("email")
        password = data.get("password")
        user = User(email=email, password=password).save()
        profile = UserProfile()
        profile.user_id = user.id
        profile.save()
        return user


