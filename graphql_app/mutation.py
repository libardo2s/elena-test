import graphene
from django.contrib.auth.models import User
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from graphql_app.models import Task
from graphql_app.types import TaskType, UserType


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Input(object):
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        name = graphene.String(required=True)

    @staticmethod
    def mutate(root, info, **kwargs):
        try:
            username = kwargs.get('username', None)
            password = kwargs.get('password', None)
            name = kwargs.get('name', None)
            user = User.objects.create_user(first_name=name, username=username, password=password)
            return CreateUserMutation(user=user)
        except Exception as e:
            raise GraphQLError(e.message)


class CreateTaskMutation(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Input(object):
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    @staticmethod
    @login_required
    def mutate(root, info, **kwargs):
        try:
            user = info.context.user
            title = kwargs.get('title', None)
            description = kwargs.get('description', None)
            obj = Task.objects.create(title=title, description=description, user_id=user.id)
            return CreateTaskMutation(task=obj)
        except Exception as e:
            raise GraphQLError(e.message)


class UpdateTaskMutation(graphene.Mutation):
    class Input(object):
        id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        state = graphene.Int()
        is_delete = graphene.Boolean()
        end_date = graphene.Date()

    task = graphene.Field(TaskType)

    @staticmethod
    @login_required
    def mutate(root, info, **kwargs):
        try:
            id = kwargs.get('id', None)
            user = info.context.user
            task = Task.objects.get(id=id)

            if task.user.id == user.id:
                title = kwargs.get('title', None)
                description = kwargs.get('description', None)
                state = kwargs.get('state', None)
                is_delete = kwargs.get('is_delete', None)
                end_date = kwargs.get('end_date', None)

                task.title = title if title is not None else task.title
                task.description = description if description is not None else task.description
                task.state = state if state is not None else task.state
                task.is_delete = is_delete if is_delete is not None else task.is_delete
                task.end_date = end_date if end_date is not None else task.end_date
                task.save()

                return CreateTaskMutation(task=task)
            else:
                raise GraphQLError("Usuario no autorizado para modificar esta tarea")
        except Exception as e:
            raise GraphQLError(e.message)
