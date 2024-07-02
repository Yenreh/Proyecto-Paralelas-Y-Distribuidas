from locust import HttpUser, task, between

BACKEND_URL = "http://127.0.0.1:8000/api"


class User(HttpUser):
    wait_time = between(1, 2.5)
    host = BACKEND_URL

    # Tes for view that does not exist
    @task
    def load_backend(self):
        self.client.get("/")

    @task
    def get_projects(self):
        response = self.client.get("/projects")
        response.raise_for_status()

    @task
    def get_project(self):
        response = self.client.get("/projects/1")
        response.raise_for_status()

    @task
    def create_project(self):
        response = self.client.post("/projects/create", json={"name": "New Project"})
        response.raise_for_status()

    @task
    def update_project(self):
        response = self.client.put("/projects/update/1", json={"name": "Updated Project 1"})
        response.raise_for_status()

    # Test for register that does not exist after first run
    @task
    def delete_project(self):
        response = self.client.delete("/projects/delete/2")
        response.raise_for_status()

    @task
    def get_project_tasks(self):
        response = self.client.get("/projects/1/tasks")
        response.raise_for_status()

    @task
    def get_tasks(self):
        response = self.client.get("/tasks")
        response.raise_for_status()

    @task
    def get_task(self):
        response = self.client.get("/tasks/1")
        response.raise_for_status()

    @task
    def create_task(self):
        response = self.client.post("/tasks/create", json={"name": "New Task for Project 1", "project_id": 1})
        response.raise_for_status()

    # Test with missing required field
    @task
    def create_task2(self):
        response = self.client.post("/tasks/create", json={"name": "New Task for Project 1"})
        response.raise_for_status()

    @task
    def update_task(self):
        response = self.client.put("/tasks/update/1", json={"name": "Updated Task 1"})
        response.raise_for_status()

    # Test for register that does not exist after first run
    @task
    def delete_task(self):
        response = self.client.delete("/tasks/delete/2")
        response.raise_for_status()
