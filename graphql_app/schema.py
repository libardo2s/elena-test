from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType

from graphql_app.resolvers import task_resolver, user_resolver

type_defs = [
    load_schema_from_path("graphql_app/schema.graphql"),
    load_schema_from_path("graphql_app/schemas/user_schema.graphql"),
    load_schema_from_path("graphql_app/schemas/task_schema.graphql"),
]

query = QueryType()
mutation = MutationType()

query.set_field("tasks", task_resolver.list_tasks)

mutation.set_field("createUser", user_resolver.create_user)

schema = make_executable_schema(type_defs, query, mutation)
