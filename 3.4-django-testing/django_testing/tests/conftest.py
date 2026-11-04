import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def api_client():
    """Фикстура для API клиента."""
    return APIClient()


@pytest.fixture
def course_factory():
    """Фабрика для создания курсов."""
    def _create_course(**kwargs):
        return baker.make(Course, **kwargs)
    return _create_course


@pytest.fixture
def student_factory():
    """Фабрика для создания студентов."""
    def _create_student(**kwargs):
        return baker.make(Student, **kwargs)
    return _create_student