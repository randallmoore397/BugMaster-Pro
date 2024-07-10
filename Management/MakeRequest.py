import requests
class MakeRequest():
    def __init__(self,target_url:str,payload:dict,bearer_token:str):
        self.target_url = target_url
        self.payload = payload
        self.bearer_token = bearer_token
        self.headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-,Type': 'application/json'
        }
        


    def sendGET(self):
        """_sendPOST_
        Sends GET request to a target URL

        Returns:
            Status Code : return status code (TRUE OR FALSE) if action was successfully performed
            Respond: Any respond send from BackEnd
        """
        try:
            response = requests.get(self.target_url, json=self.payload, headers=self.headers)

            # Handling Response: Checking for success or errors
            if response.status_code == 200:
                # print('Success:', response.json())
                return response.json()
            else:
                # print('Error:', response.status_code)
                return response.text
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return e
    
    
    def sendPOST(self):
        """_sendPOST_
        Sends POST request to a target URL

        Returns:
            Status Code : return status code (TRUE OR FALSE) if action was successfully performed
            Respond: Any respond send from BackEnd
        """
        try:
            response = requests.post(self.target_url, json=self.payload, headers=self.headers)

            # Handling Response: Checking for success or errors
            if response.status_code == 200:
                # print('Success:', response.json())
                return response.json()
            else:
                # print('Error:', response.status_code)
                return response.text
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return e
    
    
    
    def sendPUT(self):
        """_sendPOST_
        Sends PUT request to a target URL

        Returns:
            Status Code : return status code (TRUE OR FALSE) if action was successfully performed
            Respond: Any respond send from BackEnd
        """
        try:
            response = requests.put(self.target_url, json=self.payload, headers=self.headers)

            # Handling Response: Checking for success or errors
            if response.status_code == 200:
                # print('Success:', response.json())
                return response.json()
            else:
                # print('Error:', response.status_code)
                return response.text
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return e
        
        
    
    def sendDELETE(self):
        """_sendPOST_
        Sends DELETE request to a target URL

        Returns:
            Status Code : return status code (TRUE OR FALSE) if action was successfully performed
            Respond: Any respond send from BackEnd
        """
        try:
            response = requests.delete(self.target_url, json=self.payload, headers=self.headers)

            # Handling Response: Checking for success or errors
            if response.status_code == 200:
                # print('Success:', response.json())
                return response.json()
            else:
                # print('Error:', response.status_code)
                return response.text
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return e