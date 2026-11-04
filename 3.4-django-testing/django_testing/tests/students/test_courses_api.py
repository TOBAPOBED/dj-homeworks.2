import pytest
from rest_framework import status


@pytest.mark.django_db
class TestCoursesAPI:
    """Тесты для API курсов."""

    def test_retrieve_course(self, api_client, course_factory):
        """Тест получения одного курса (retrieve)."""
        # Arrange
        course = course_factory(name='Тестовый курс')
        
        # Act
        url = f'/api/v1/courses/{course.pk}/'
        response = api_client.get(url)
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == course.pk
        assert response.data['name'] == course.name

    def test_list_courses(self, api_client, course_factory):
        """Тест получения списка курсов (list)."""
        # Arrange
        course_factory(name='Курс 1')
        course_factory(name='Курс 2')
        course_factory(name='Курс 3')
        
        # Act
        url = '/api/v1/courses/'
        response = api_client.get(url)
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_filter_courses_by_id(self, api_client, course_factory):
        """Тест фильтрации курсов по id."""
        # Arrange
        course1 = course_factory(name='Курс 1')
        course_factory(name='Курс 2')
        
        # Act
        url = f'/api/v1/courses/?id={course1.pk}'
        response = api_client.get(url)
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['id'] == course1.pk

    def test_filter_courses_by_name(self, api_client, course_factory):
        """Тест фильтрации курсов по name."""
        # Arrange
        course_factory(name='Python')
        course_factory(name='Django')
        
        # Act
        url = '/api/v1/courses/?name=Python'
        response = api_client.get(url)
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['name'] == 'Python'

    def test_create_course(self, api_client):
        """Тест создания курса."""
        # Arrange
        url = '/api/v1/courses/'
        data = {
            'name': 'Новый курс',
            'students': []
        }
        
        # Act
        response = api_client.post(url, data, format='json')
        
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'Новый курс'

    def test_update_course(self, api_client, course_factory):
        """Тест обновления курса."""
        # Arrange
        course = course_factory(name='Старое название')
        url = f'/api/v1/courses/{course.pk}/'
        data = {
            'name': 'Новое название',
            'students': []
        }
        
        # Act
        response = api_client.patch(url, data, format='json')
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Новое название'

    def test_delete_course(self, api_client, course_factory):
        """Тест удаления курса."""
        # Arrange
        course = course_factory(name='Курс для удаления')
        url = f'/api/v1/courses/{course.pk}/'
        
        # Act
        response = api_client.delete(url)
        
        # Assert
        assert response.status_code == status.HTTP_204_NO_CONTENT