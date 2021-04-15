import graphene
import graphql_jwt
from graphene import ObjectType
from graphql_jwt.decorators import login_required

from graphql_app.models import Task
from graphql_app.mutation import CreateTaskMutation, UpdateTaskMutation
from graphql_app.types import TaskType


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_task = CreateTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()


class Query(ObjectType):
    task_by_user = graphene.List(TaskType)
    task_by_description = graphene.List(TaskType)

    @login_required
    def resolve_task_by_user(self, info, **kwarg):
        user = info.context.user
        return Task.objects.filter(user__id=user.id, is_delete=False)

    @login_required
    def resolve_task_by_description(self, info, description):
        user = info.context.user
        return Task.objects.filter(user__id=user.id, description__search=description)


schema = graphene.Schema(mutation=Mutation, query=Query)
