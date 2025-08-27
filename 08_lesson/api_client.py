import requests


class YougileAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload):
        """POST /api-v2/projects"""
        url = f"{self.base_url}/api-v2/projects"
        return requests.post(url, headers=self.headers, json=payload)

    def update_project(self, project_id, payload):
        """PUT /api-v2/projects/{id}"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.put(url, headers=self.headers, json=payload)

    def get_project(self, project_id):
        """GET /api-v2/projects/{id}"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)
