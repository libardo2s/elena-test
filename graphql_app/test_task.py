from django.contrib.auth import get_user_model

from graphql_jwt.testcases import JSONWebTokenTestCase

query_task_by_user = '''
        query TaskByUser($page:Int!){
          taskByUser(page: $page){
            page
            pages
            objects{title, startDate, id}
          }
        }'''

query_task_by_description = '''
        query
        TaskByDescription($text: String!){
            taskByDescription(text: $text){
            title, description
        }
        }'''


class UsersTests(JSONWebTokenTestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='test')
        self.client.authenticate(self.user)

    def test_get_task_by_user(self):
        variables = {'page': 1}

        self.client.execute(query_task_by_user, variables)

    def test_get_task_by_description(self):
        variables = {}

        self.client.execute(query_task_by_description, variables)

