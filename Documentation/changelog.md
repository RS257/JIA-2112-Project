## Version 0.4.0

### Features

- Certification Changes
    - When users complete certification there is now an indication that they have completed it
     on their table views

    - Limited vs Not Limited Certifications
        - Limted: There is an Expiration field added to Certifications (measured in days till expiration)
        - Not Limited: There is a field that does not have an expiration for cerifications that need 
                       to be completed one time or unknown completion date.

- Administrative Updates
    - added a table view for admin to see what certifications need to be completed by user in a
      collapsible table. (This view will only show if the user has admin permissions)
      
        - This is based on the Role of the Faculty and Staff assigned so it can change for users.
        - It has statistics for completed  vs uncompleted certifications

- UI Changes
    - Added a Navigation Bar that exists on every screen 
        - There is a logout button that will appear once a user logs in
    - Added a favicon to the website tab

### Bug Fixes
- Login page occasionally does not login after account creation
    - Fixed after we recreated the page backend

- There is a UI Glitch that occasionally the buttons appear Blue instead of the Valliant Orange 
    - Fixed after we realized we pointing to the wrong CSS files

- Back buttons on the Login and Register page are bugged due to it being pure HTML and Not BootStrapped 
    - Fixed and functional
### Known Issues 

- Logout button on dasboard View
    - When a user clicks back on the logout screen it redirects to the dashbaord, it causes the 
      logout button not to be clickable.
      - The temporary solution is to have it fixed  


## Version 0.3.0

### Features

- added a table for Faculty and Staff to see what certifications need to be completed. 
    - This is based on the Role of the Faculty and Staff assigned so it can change for users.

- There is an `Upload` button to upload a certification.
    - Added an ability to allow the user to browse your local files to upload
    - Added a Dropdown selection on menu for the specific certification
    - Added a Date completed selection on to the certifications
    - Certificates are organized by date uploaded in the backend 

- Administrative Updates
    - Ability to login into the System


- UI Overhaul
    - Coloring is aligned to the Valliant School System Colors
    - Added Bootstrap5 to the project
    - Forms have shadows around them to better visually seperate them from the space they are in.
    - Created `Back` buttons on the Login and Registration Pages

### Bug Fixes
- N/A

### Known Issues 
- Login page occasionally does not login after account creation

- Back buttons on the Login and Register page are bugged due to it being pure HTML and Not BootStrapped 
    - This will be fixed next sprint. 

- There is a UI Glitch that occasionally the buttons appear Blue instead of the Valliant Orange 


## Version 0.2.0

### Features
* Roles added
* User profile added
* Roles assignment to users added
* New users are able to write their first and last names during registration 

### Bug Fixes
N/A

### Known Issues 
N/A


## Version 0.1.0

### Features
* User registration of F/SM
* User login of F/SM
* User logout of F/SM

### Bug Fixes
N/A

### Known Issues 
N/A
