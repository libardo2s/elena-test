import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from graphql_app.models import Task
from graphql_app.types import TaskType


class CreateTaskMutation(graphene.Mutation):
    class Input(object):
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    task = graphene.Field(TaskType)

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

                task.title = title if title is not None else task.title
                task.description = description if description is not None else task.description
                task.state = state if state is not None else task.state
                task.is_delete = is_delete if is_delete is not None else task.is_delete
                task.save()

                return CreateTaskMutation(task=task)
            else:
                raise GraphQLError("Usuario no autorizado para modificar esta tarea")
        except Exception as e:
            raise GraphQLError(e.message)
