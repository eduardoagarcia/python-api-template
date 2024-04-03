from app.graphql.moodle.api import moodle_api
from app.graphql.moodle.courses.schema import MoodleCourse


def fetch_moodle_courses(token: str) -> list[MoodleCourse]:
    courses_data = moodle_api(function_name="core_course_get_courses", token=token)

    if courses_data is None:
        return []

    courses = [
        MoodleCourse(
            id=str(course['id']),
            name=course['fullname'],
            description=course.get('summary', '')
        )
        for course in courses_data
    ]

    return courses
