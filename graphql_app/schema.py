import graphene
import graphql_jwt
from django.contrib.postgres.search import SearchVector
from graphene import ObjectType
from graphql_jwt.decorators import login_required

from graphql_app.models import Task
from graphql_app.mutation import CreateTaskMutation, UpdateTaskMutation, CreateUserMutation
from graphql_app.types import TaskType, TaskPaginatorType
from graphql_app.utils import get_paginator


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_task = CreateTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()


class Query(ObjectType):
    task_by_user = graphene.Field(TaskPaginatorType, page=graphene.Int())
    task_by_description = graphene.List(TaskType, text=graphene.String())

    @login_required
    def resolve_task_by_user(self, info, page):
        page_size = 10
        user = info.context.user
        tasks = Task.objects.filter(user__id=user.id, is_delete=False)
        return get_paginator(tasks, page_size, page, TaskPaginatorType)

    @login_required
    def resolve_task_by_description(self, info, text):
        user = info.context.user
        return Task.objects.annotate(search=SearchVector('description')).filter(search=text, user__id=user.id, is_delete=False)


schema = graphene.Schema(mutation=Mutation, query=Query)
