import pytest
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.status import ( HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, )
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make("core.Course", **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make("core.Student", **kwargs)
    return factory
@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse("course-detail", args=[course.id])
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert response.data["id"] == course.id

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse("course-list")
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 3

@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    course1 = course_factory(id=1)
    course2 = course_factory(id=2)
    url = reverse("course-list") + "?id=1"
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["id"] == course1.id

@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course1 = course_factory(name="Math")
    course2 = course_factory(name="Science")
    url = reverse("course-list") + "?name=Math"
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == course1.name

@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse("course-list")
    data = {"name": "Math"}
    response = api_client.post(url, data=data)
    assert response.status_code == HTTP_201_CREATED
    assert response.data["name"] == "Math"

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(name="Math")
    url = reverse("course-detail", args=[course.id])
    data = {"name": "Science"}
    response = api_client.patch(url, data=data)
    assert response.status_code == HTTP_200_OK
    assert response.data["name"] == "Science"

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse("course-detail", args=[course.id])
    response = api_client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
    assert not response.data