from app.services import user_service


def create_user(user_data):
    return user_service.create_user(user_data)