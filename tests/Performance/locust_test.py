from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    access_token = None

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        response = self.client.post("url", {"username": "admin", "password": "admin"})
        # response_body = response.json()
        # self.access_token = response_body.get('access_token')

    @task
    def get_index(self):
        self.client.get("/")

    @task
    def get_news(self):
        self.client.get("/news")

    @task
    def get_tasks(self):
        self.client.get("/tasks")

    @task
    def get_planning(self):
        self.client.get("/planning")

    @task
    def get_documents(self):
        self.client.get("/documents")

    @task
    def get_stores(self):
        self.client.get("/stores")

    @task
    def get_supplies(self):
        self.client.get("/supplies")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    host = 'url'
