from locust import HttpUser, task

class BasicUser(HttpUser):
    host = "http://localhost:8900"

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
        with self.client.get(f"/destination/4", catch_response=True) as response:
            self.environment.request_meta_data.append(response.request_meta)

    @task(2)
    def view_cruises(self):
        with self.client.get(f"/cruise/3", catch_response=True) as response:
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
