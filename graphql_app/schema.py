from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType

from graphql_app.resolvers import task_resolver

type_defs = [
    load_schema_from_path("graphql_app/schema.graphql"),
    load_schema_from_path("graphql_app/schemas/user_schema.graphql"),
    load_schema_from_path("graphql_app/schemas/task_schema.graphql"),
]

query = QueryType()
query.set_field("tasks", task_resolver.list_tasks)


schema = make_executable_schema(type_defs, query)
