from Management.BugManagement import BugManagement

def main():
    add_bug = BugManagement(74383,34,59,'7dsf78sfd6dsf8s78df')
    # status = add_bug.trackBug("Report Card Semester Average","Medium","August/08/2024")
    # if status == True:
    #     print("Bug Tracked....!!!")
    # elif status == False:
    #     print("Error, Bug Tracking Failed..try again")
    # else:
    #     print("Error: Can't Connect to the internet")
    
    add_bug.removeBugTrack('90238432329u239',84,"Bug Fixed")




if __name__ == "__main__":
    main()