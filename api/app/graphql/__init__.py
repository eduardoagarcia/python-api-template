import strawberry

from .api.auth.schema import APIAuthOperations
from .moodle.auth.schema import MoodleAuthOperations


@strawberry.type
class HealthQuery:
    @strawberry.field()
    def health(self) -> str:
        return "GraphQL is up and running!"


@strawberry.type
class Query(HealthQuery):
    api_auth: APIAuthOperations = strawberry.field(resolver=lambda: APIAuthOperations())
    moodle_auth: MoodleAuthOperations = strawberry.field(resolver=lambda: MoodleAuthOperations())


@strawberry.type
class Mutation:
    api_auth: APIAuthOperations = strawberry.field(resolver=lambda: APIAuthOperations())
    moodle_auth: MoodleAuthOperations = strawberry.field(resolver=lambda: MoodleAuthOperations())


schema = strawberry.Schema(query=Query, mutation=Mutation)
