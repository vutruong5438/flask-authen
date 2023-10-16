from app.models import UserProfile


class UserProfileService:

    @classmethod
    def update_profile(cls, id, data):
        profile = UserProfile.get_by_user_id(id)
        profile.update(**data)
        return True
