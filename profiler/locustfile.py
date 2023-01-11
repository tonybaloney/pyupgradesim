from locust import HttpUser, task

class BasicUser(HttpUser):
    host = "http://localhost:8000"

    @task
    def index(self):
        with self.client.get("/", catch_response=True) as response:
            self.environment.request_meta_data.append(response.request_meta)
    
    @task(6)
    def locations(self):
        with self.client.get("/destinations", catch_response=True) as response:
            self.environment.request_meta_data.append(response.request_meta)
    
    @task(2)
    def view_locations(self):
        for destination_id in range(1, 11):
            with self.client.get(f"/destination/{destination_id}", catch_response=True) as response:
                self.environment.request_meta_data.append(response.request_meta)

    @task(2)
    def view_cruises(self):
        for cruise_id in range(1, 6):
            with self.client.get(f"/cruise/{cruise_id}", catch_response=True) as response:
                self.environment.request_meta_data.append(response.request_meta)

    @task
    def submit_enquiry(self):
        response = self.client.get("/info_request")
        csrftoken = response.cookies['csrftoken']

        with self.client.post("/info_request", {
            "name": "John Smith",
            "email": "john@smith.com" ,
            "cruise": "1", 
            "notes": "I would like to know more about this cruise"},
            headers={"X-CSRFToken": csrftoken}, catch_response=True) as response:
            self.environment.request_meta_data.append(response.request_meta)
