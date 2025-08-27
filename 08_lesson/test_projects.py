import pytest

class TestProjects:

    def test_create_project_positive(self, api):
        payload = {"title": "Test Project"}
        response = api.create_project(payload)
        assert response.status_code == 201  # успешное создание
        data = response.json()
        assert "id" in data

    def test_create_project_negative(self, api):
        # пустой payload → ошибка
        payload = {}
        response = api.create_project(payload)
        assert response.status_code == 400

    def test_get_project_positive(self, api):
        # создаём проект
        payload = {"title": "Project to Get"}
        response = api.create_project(payload)
        project_id = response.json()["id"]

        # получаем проект
        response = api.get_project(project_id)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == project_id
        assert data["title"] == payload["title"]

    def test_get_project_negative(self, api):
        response = api.get_project("non_existing_id")
        assert response.status_code == 404

    def test_update_project_positive(self, api):
        # создаём проект
        payload = {"title": "Old Name"}
        response = api.create_project(payload)
        project_id = response.json()["id"]

        # обновляем проект
        update_payload = {"title": "Updated Name"}
        response = api.update_project(project_id, update_payload)
        assert response.status_code == 200

        # проверяем через GET
        response = api.get_project(project_id)
        data = response.json()
        assert data["title"] == "Updated Name"

    def test_update_project_negative(self, api):
        update_payload = {"title": "Some Name"}
        response = api.update_project("non_existing_id", update_payload)
        assert response.status_code in [400, 404]
