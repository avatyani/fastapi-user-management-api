from app.repositories import user_repository


def create_user(user_data):
    return user_repository.create_user(user_data)