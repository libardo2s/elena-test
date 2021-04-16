import graphene
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType

from graphql_app.models import Task


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


class TaskType(DjangoObjectType):
    status = graphene.String()

    def resolve_status(self, info):
        return self.state

    class Meta:
        model = Task
        fields = '__all__'


class TaskPaginatorType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(TaskType)
