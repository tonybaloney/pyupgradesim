from locust import HttpUser, task, between

class BasicUser(HttpUser):
    wait_time = between(0,0.1)

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

    @task(2)
    def view_cruises(self):
        for cruise_id in range(1, 6):
            self.client.get(f"/cruise/{cruise_id}")

    @task
    def submit_enquiry(self):
        response = self.client.get("/info_request")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/info_request", {
            "name": "John Smith",
            "email": "john@smith.com" ,
            "cruise": "1", 
            "notes": "I would like to know more about this cruise"},
            headers={"X-CSRFToken": csrftoken})
