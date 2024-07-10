from Management.BugManagement import BugManagement
from Management.ProjectManagement import ProjectManagement

def main():
    # ***********************************************
    #? CREATING A PROJECT
    pro_title = "StudyLiberia School Management System"
    pro_category = "Web Development" 
    creator = 36
    access_token = "66ds8fds67df8ds8ds8fds9fds6ds5"
    create_proj = ProjectManagement(title=pro_title,category=pro_category,creator_id=creator,token=access_token)
    # create_proj.createProject()
    
    #? DELETING A PROJECT
    project_uuid = "8s78dff87sds5ds87dfs3f"
    creator_id = 36
    message = "Project Completed Successfully"
    # create_proj.deleteProject(project_uuid=project_uuid,creator_id=creator_id,message=message)
    
    #? GETTING PROJECT DETAILS
    # create_proj.projectDetails(project_uuid=project_uuid)
    
    #? UPDATING PROJECT DETAILS
    project_title = "PathogenPulse"
    project_category= "Web Development" 
    project_status = "ACTIVE"
    project_deadline = "August/08/2024"
    
    create_proj.editProject(project_uuid=project_uuid,project_title=project_title,project_category=project_category,project_creator=creator_id,project_status=project_status,project_deadline=project_deadline)
    
    # *********************************************
    #? ADD A BUG FOR TRACKING
    # add_bug = BugManagement(74383,34,59,'7dsf78sfd6dsf8s78df')
    # add_bug.trackBug("Report Card Semester Average","Medium","August/08/2024")
    
    #? Remove bug from tracking
    # add_bug.removeBugTrack('90238432329u239',84,"Bug Fixed")
    # ********************************************



if __name__ == "__main__":
    main()