from locust import HttpUser, task, between
import time

class BasicUser(HttpUser):
    wait_time = between(3, 5)

    @task
    def index(self):
        self.client.get("/")
    
    @task(6)
    def locations(self):
        self.client.get("/destinations")
    
    @task(2)
    def view_locations(self):
        for destination_id in range(1, 11):
            self.client.get(f"/destination/{destination_id}")
            time.sleep(1)

    @task(2)
    def view_cruises(self):
        for cruise_id in range(1, 6):
            self.client.get(f"/cruise/{cruise_id}")
            time.sleep(1)

    # TODO : submit enquiry
