import graphene
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType

from graphql_app.models import Task


class UserType(DjangoObjectType):
    class Meta:
        model = User


class TaskType(DjangoObjectType):
    status = graphene.String()

    def resolve_status(self, info):
        return self.state

    class Meta:
        model = Task


class TaskPaginatorType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(TaskType)
