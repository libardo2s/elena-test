from graphql_app.models import Task


def list_tasks(*_):
    return [
        {
            "title": task.title,
            "description": task.description,
            "start_date": task.start_date,
            "end_date": task.end_date,
            "user": {
                "username": task.user.username,
                "first_name": task.user.first_name,
                "last_name": task.user.last_name
            }
        }
        for task in Task.objects.all()
    ]
