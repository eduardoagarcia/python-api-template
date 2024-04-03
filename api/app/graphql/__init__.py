import strawberry

from .moodle.auth.schema import AuthQuery as MoodleAuthQuery


@strawberry.type
class BaseQuery:
    @strawberry.field
    def health_check(self) -> str:
        return "GraphQL is up and running!"


@strawberry.type
class Query(BaseQuery, MoodleAuthQuery):
    pass


schema = strawberry.Schema(query=Query)
