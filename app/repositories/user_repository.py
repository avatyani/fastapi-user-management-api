users_db = {}
user_id_counter = 1


def create_user(user_data):
    global user_id_counter

    user = {
        "id": user_id_counter,
        "name": user_data.name,
        "email": user_data.email,
        "password": user_data.password
    }

    users_db[user_id_counter] = user
    user_id_counter += 1

    return user