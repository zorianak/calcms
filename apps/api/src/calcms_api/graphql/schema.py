"""
Strawberry GraphQL schema.

Add your types, queries, mutations, and subscriptions here.
Wire the schema into your HTTP handler in main.py.

Example integration (using Strawberry's ASGI app — requires an ASGI server):

    import strawberry
    from strawberry.asgi import GraphQL
    from calcms_api.graphql.schema import schema

    graphql_app = GraphQL(schema)
    # Mount graphql_app at /graphql in your ASGI server.
"""

import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        """Health-check resolver — returns 'pong'."""
        return "pong"


# Add mutations here when you're ready:
# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_content(self, title: str) -> str:
#         return f"Created: {title}"


schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,  # uncomment when you have mutations
)
