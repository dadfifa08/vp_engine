class Roles:
    ADMINS = {"your_twitter_handle"}
    MODERATORS = set()

    @staticmethod
    def is_admin(user):
        return user in Roles.ADMINS

    @staticmethod
    def is_moderator(user):
        return user in Roles.MODERATORS
