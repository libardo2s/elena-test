from django.contrib.auth.models import User
from django.db import IntegrityError


def create_user(*_, first_name, last_name, username, password):
    try:
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        password=password)
        return {
            "error_message": "",
            "is_error": False,
            "user": {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
        }
    except IntegrityError:
        return {
            "error_message": "El usuario ya se encuentra registrado",
            "is_error": True,
            "user": {}
        }
    except Exception as e:
        return {
            "error_message": "Ha ocurrido un error.",
            "is_error": True,
            "user": {}
        }
