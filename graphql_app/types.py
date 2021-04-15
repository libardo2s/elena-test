import graphene
from django.contrib.auth import get_user_model
from graphene_django.types import DjangoObjectType

from graphql_app.models import Task


class TaskType(DjangoObjectType):
    status = graphene.String()

    def resolve_status(self, info):
        return self.state

    class Meta:
        model = Task
