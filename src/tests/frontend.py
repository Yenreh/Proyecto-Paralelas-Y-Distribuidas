from locust import HttpUser, task, between


FRONTEND_URL = "http://127.0.0.1:5000"

class User(HttpUser):
    wait_time = between(1, 2.5)
    host = FRONTEND_URL

    @task
    def load_frontend(self):
        self.client.get("/")

    @task
    def get_projects(self):
        self.client.get("/projects")

    @task
    def get_tasks(self):
        self.client.get("/tasks")

    # test for view that does not exist
    @task
    def get_users(self):
        self.client.get("/users")
