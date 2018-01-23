from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post('http://store.demoqa.com/wp-login.php', {'log': 'test_user123', 'pwd': '123qwe123'})

    @task
    def get_home(self):
        self.client.get('/')

    @task
    def get_products(self):
        self.client.get('/products-page')

    @task
    def get_categories(self):
        self.client.get('/products-page/product-category')

    @task
    def get_specific_product(self):
        self.client.get('/products-page/product-category/n')

    @task
    def get_cart(self):
        self.client.get('/products-page/checkout')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    host = 'http://store.demoqa.com'
