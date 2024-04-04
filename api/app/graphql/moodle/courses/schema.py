import strawberry

from app.graphql.moodle.courses.api import fetch_moodle_courses


@strawberry.type
class MoodleCourse:
    id: strawberry.ID
    name: str
    description: str


@strawberry.type
class Query:
    @strawberry.field()
    def moodle_courses(self, token: str) -> list[MoodleCourse]:
        return fetch_moodle_courses(token=token)
