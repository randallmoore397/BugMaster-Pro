from Management.MakeRequest import  MakeRequest
from datetime import datetime
class ProjectManagement:
    """_ProjectManagement_
        o	Project Dashboard: Overview of all bugs, tasks, and progress within a project.
        o	Milestones and Sprints: Track bugs and tasks by milestones or sprints.
        o	Roadmaps and Timelines: Visual representation of project timelines and milestones.
    """
    def __init__(self,title:str,category:str,creator_id:int,token:str):
        """_summary_

        Args:
            title (str): _description_
            category (str): Refers to the category of the project:
                            (1) Web Development
                            (2) Mobile Development
                            (3) Desktop Application
                            (4) Game Development
                            (5) Machine Learning (AI)
                            (6) Embedded System 
                            (7) Cross Platform Application
            creator_id (int): ID of user creating the project
            token (str): Authorization Bearer toekn
        """
        
        self.title = title
        self.category = category
        self.creator_id = creator_id
        self.token = token 
    
    def createProject(self) -> None:
        """_createProject_
            Create a new project and return the project ID
        """
        url = 'http://127.0.0.1:5000/user/create/new/project'
        
        payload = {
            'project_title': self.title,
            'project_category': self.category,
            'project_creator': self.creator_id,
            'date_added': datetime.today().strftime('%Y-%m-%d'),
        }
        
        #? SEND POST REQUEST TO BACKEND TO CREATE NEW PROJECT
        post = MakeRequest(target_url=url,payload=payload,bearer_token=self.token)
        data = post.sendPOST()

        if data["status"] == True:
            print("Project Created....!!!")
            print(f"Response : {data}")
        elif data["status"] == False:
            print("Error, Project Creation Failed..try again")
        else:
            print("Error: Can't Connect to the internet")
            
            
            
    
    def deleteProject(self,project_uuid:str,creator_id:str,message:str)->None:
        """_deleteProject_
            Delete a project and return the project ID
        """
        url = 'http://127.0.0.1:5000/user/create/delete/project'
        
        payload = {
            'project_title': self.title,
            'project_category': self.category,
            'project_creator': self.creator_id,
            'date_added': datetime.today().strftime('%Y-%m-%d'),
        }
        
        #? SEND POST REQUEST TO BACKEND TO CREATE NEW PROJECT
        post = MakeRequest(target_url=url,payload=payload,bearer_token=self.token)
        data = post.sendDELETE()

        if data["status"] == True:
            print("Project Deleted....!!!")
            print(f"Response : {data}")
        elif data["status"] == False:
            print("Error: Project Deletion Failed..try again")
        else:
            print("Error: Can't Connect to the internet")
    
    
    def projectDetails(self,project_uuid:str):
        """_projectDetails_

        Args:
            project_uuid (str): ID of the project
        """
        #? GET PROJECT DETAILS
        get_url = 'http://127.0.0.1:5000/user/get/project/details'
        
        get_payload = {
            'project_uuid': project_uuid
        }
        #? SEND POST REQUEST TO BACKEND TO GET PROJECT DETAILS
        project_details = MakeRequest(target_url=get_url,payload=get_payload,bearer_token=self.token)
        details = project_details.sendGET()
        
        if details["status"] == True:
            print("Project Fetched....!!!")
            print(f"Details : {details}")
        elif details["status"] == False:
            print("Error: Project Deletion Failed..try again")
        else:
            print("Error: Can't Connect to the internet")
    
    
    def editProject(self,project_uuid:str,project_title:str,project_category:str,project_creator:int,project_status:str,project_deadline:str) -> None:
        """_editProject_
            Update a given project details using PROJECT_UUD
        Args:
            project_uuid (str): ID of the project
            project_title (str): Title of the project_
            project_category (str): Project's category, could be:
                            (1) Web Development
                            (2) Mobile Development
                            (3) Desktop Application
                            (4) Game Development
                            (5) Machine Learning (AI)
                            (6) Embedded System 
                            (7) Cross Platform Application
            project_creator (int): ID of user who is updating project details
            project_status (str): Information about project progress:
                                (1) ACTIVE
                                (2) CLOSED
                                (3) SUSPENDED
            project_deadline (str): Associated Deadline for project completion
        """
        #? SEND POST REQUEST TO BACKEND TO UPDATE PROJECT DETAILS
        post_url = 'http://127.0.0.1:5000/user/update/project'
        
        post_payload = {
            'project_uuid': project_uuid,
            'project_title': project_title,
            'project_category': project_category,
            'project_creator': project_category,
            'project_status': project_status,
            'project_deadline': project_deadline,
            'date_edited': datetime.today().strftime('%Y-%m-%d'),
        }
        project_edit = MakeRequest(target_url=post_url,payload=post_payload,bearer_token=self.token)
        respond = project_edit.sendPOST()
        
        if respond["status"] == True:
            print("Project Details Updated....!!!")
            print(f"Response : {respond}")
        elif respond["status"] == False:
            print("Error: Project Deletion Failed..try again")
        else:
            print("Error: Can't Connect to the internet")
        
        
    
    def suspendProject(self):
        #? CHANGE PROJECT STATUS FROM ACTIVE,CLOSED TO SUSPENDED
        pass