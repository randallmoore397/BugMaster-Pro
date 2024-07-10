from datetime import datetime
import requests
from Management.MakeRequest import  MakeRequest

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
        
        post = MakeRequest(target_url=url,payload=payload,bearer_token=self.token)
        data = post.sendPOST()
        if data["status"] == True:
            print("Bug Tracked....!!!")
            print(f"Response : {data}")
        elif data["status"] == False:
            print("Error, Bug Tracking Failed..try again")
        else:
            print("Error: Can't Connect to the internet")

            
            
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
        
        post = MakeRequest(target_url=url,payload=payload,bearer_token=self.token)
        data = post.sendDELETE()
        if data["status"] == True:
            print("Bug Deleted....!!!")
            print(f"Response : {data}")
        elif data["status"] == False:
            print("Error, Bug Deletion Failed..try again")
        else:
            print("Error: Can't Connect to the internet")
    

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
