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
        self.client.get("/projects")

    @task
    def get_project(self):
        self.client.get("/projects/1")

    @task
    def create_project(self):
        self.client.post("/projects/create", json={"name": "New Project"})

    @task
    def update_project(self):
        self.client.put("/projects/update/1", json={"name": "Updated Project 1"})

    # Test for register that does not exist after first run
    @task
    def delete_project(self):
        response = self.client.delete("/projects/delete/2")
        response.raise_for_status()

    @task
    def get_project_tasks(self):
        self.client.get("/projects/1/tasks")

    @task
    def get_tasks(self):
        self.client.get("/tasks")

    @task
    def get_task(self):
        self.client.get("/tasks/1")

    @task
    def create_task(self):
        self.client.post("/tasks/create", json={"name": "New Task for Project 1", "project_id": 1})

    # Test with missing required field
    @task
    def create_task2(self):
        self.client.post("/tasks/create", json={"name": "New Task for Project 1"})

    @task
    def update_task(self):
        self.client.put("/tasks/update/1", json={"name": "Updated Task 1"})

    # Test for register that does not exist after first run
    @task
    def delete_task(self):
        self.client.delete("/tasks/delete/2")
