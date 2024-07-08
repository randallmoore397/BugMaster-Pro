from datetime import datetime
import requests

class BugManagement:
    """_summary_
    o	Status Tracking: Standard bug status workflow (e.g., Open, In Progress, Resolved, Closed).
    o	Assignment: Assign bugs to team members for resolution.
    o	Comments and Discussions: Threads for communication and updates on bugs.
    o	Change History: Log of all changes made to the bug (e.g., status updates, reassignment).
    
        Args:
            project_id (str): Project (Project ID) bug is liked to
            creator_id (str): The person who is assigning this bug to a developer
            assign_developer (str): The developer work to solve the bug

    """
    def __init__(self, project_id: str, creator_id: str, assigned_developer: str, token: str):
        self.project_id = project_id
        self.creator_id = creator_id
        self.assigned_developer = assigned_developer
        self.token = token  # Include token in the class initialization
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
    
    def trackBug(self, bug_title: str, severity: str, deadline: str):
        """Track a new bug in the system.

        Args:
            bug_title (str): The title of the bug being tracked.
            severity (str): The severity level of the bug. 
                Possible values are:
                - 'Critical'
                - 'High'
                - 'Medium'
                - 'Low'
                - 'Trivial'
                - 'Blocker'
                - 'Urgent'
                - 'Enhancement'
            deadline (str): The deadline to fix the bug (format: 'Month/Day/Year').
        """
        url = 'http://127.0.0.1:5000/user/track/bug'
        

        
        payload = {
            'bug_title': bug_title,
            'severity': severity,
            'deadline': datetime.strptime(deadline, '%B/%d/%Y').strftime('%Y-%m-%d'),
            'date_added': datetime.today().strftime('%Y-%m-%d'),
            'project_id': self.project_id,
            'creator_id': self.creator_id,
            'assigned_developer': self.assigned_developer
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)

            # Handling Response: Checking for success or errors
            if response.status_code == 200:
                print('Success:', response.json())
                return True
            else:
                print('Error:', response.status_code, response.text)
                return False
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            
            
    def removeBugTrack(self,bug_uuid:str,creator_id:str,message:str):
        """_Removes Bug from Database_

        Args:
            bug_uuid (str): Unique UUID of the Bug
            creator_id (str): ID of user who is performing the delete action
            message (str): Message explaining why bug was deleted

        Returns:
            _type_: _description_
        """
        url = 'http://127.0.0.1:5000/user/remove/bug'
        
        payload = {
            'bug_uuid': bug_uuid,
            'creator_id': creator_id,
            'message': message,

        }

        try:
            response = requests.delete(url, json=payload, headers=self.headers)

            # Handling Response: Checking for success or errors
            if response.status_code == 200:
                print('Success:', response.json())
                return True
            else:
                print('Error:', response.status_code, response.text)
                return False
        
        except requests.RequestException as e:
            print(f"Request failed: {e}")
    
    

# Example usage
if __name__ == '__main__':
    tracker = BugManagement(
        project_id='12345',
        creator_id='creator_user_id',
        assigned_developer='developer_user_id',
        token='your_actual_token_here'  # Replace with a real token
    )
    tracker.trackBug(
        bug_title='Sample Bug',
        severity='High',
        deadline='July/31/2024'
    )
