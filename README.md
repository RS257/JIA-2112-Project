# Valliant Certification Tracker

### This Project was made by team JIA-2112 for the Valliant Public School District. The project is designed as a web application that allows staff to update and keep up with their necessary certification. The application provides simple methods for submission and tracking of the completed certifications. 

# Table of Contents

- [Release Notes](https://github.com/RS257/JIA-2112-Project#version-100)
  
  - [Features](https://github.com/RS257/JIA-2112-Project#features)
  - [Bug Fixes](https://github.com/RS257/JIA-2112-Project#bug-fixes)
  - [Known Issues](https://github.com/RS257/JIA-2112-Project#known-issues)
   
- [Install Guide](https://github.com/RS257/JIA-2112-Project#install-guide)
    - 
- [How To Use the Application]()





# Release Notes

## Version 1.0.0
### Features

- Administration
    - Added the Ability to give other users Admin privileges  

- Dashboard Table
    - Text change from Due Date to Expiration,
    - Added Download Feature for all certifcations

- UI Changes
    - Aligned Text on the Navbar
    - put the Yes and Back buttons on the logout page on the same row.
### Bug Fixes

- Fixed a Bug where uploading files would push to the wrong folder

- Fixed a file getting bug for the download 
### Known Issues 

- Logout button on dasboard View
    - When a user clicks back on the logout screen it redirects to the dashbaord, it causes the 
      logout button not to be clickable.
      - The temporary solution is to have it fixed  


# Install Guide

This project needs a server that can host the Project and the Media Files (the media files in this instance is the certifcations that will be uploaded by each employee). Since ultimeately this project is a website, there are many ways to host the application and run it.

We reccomend following the official [Django Deployment Checklist](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/).
Another good resources for Django Deployment can be found [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment). 

Media Files will also need a host as well. One such service that can host media files is an [Amazon Web Service S3 bucket](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

If there any changes that need to be made for accessing or setting endpoints. Those changes will generally exist in the `settings.py`
found in `tracker/tracker/` folder.


For this install guide, we will show how to run the application on the local host side. 

## Prerequsites 

A computer that has the ltest version of python3 installed. 

[Python3 Installation](https://www.python.org/downloads/) 

## Dependencies 

The application itself is using django for the Backend. It can be installed by following the [install guide on the Django website](https://docs.djangoproject.com/en/4.1/intro/install/)

The frontend of the application is using Bootstrap5 and HTML. 
(This repository already has Bootstrap5 into it. It can be found in the `tracker/users/static/home`).

To allow media file uploads the project needs to have [Pillow installed](https://pillow.readthedocs.io/en/stable/installation.html). 

## Download

You can download the application from 
`/github.com/RS257/JIA-2112-Project/JIA-2112-Project.zip`

## Build
    There isn't a need for a build file in this application

## Installation 

There is a specifc file structure that the project can exist in.

W3 Schools has a good tutorial on setting up the file structure [here](https://www.w3schools.com/django/django_getstarted.php)

Once you have created the file structure as shown from the tutorial, create a new folder in the root directory with the title of the project. Inside that folder you can unzip the app or you can do a git clone if you are developing the code.  

## Running the Application 

To run the application from the terminal, cd into the root tracker folder. 
It should have a file by the name of `manage.py`

Once you have reached that folder run the following commands in order 

The following to commands need to be run anytime the Backend is updated during development
and initial setup.
1. `python .\manage.py makemigrations`

2. `python .\manage.py migrate`


The following command is needed to make an account that will have full Admin access to the project.
Only needs to be ran once for the initial setup. Afterwards this command can be skipped.

3. `python .\manage.py createsuperuser`

4. If the backend hasn't been updated than this is the go to command to run the project after the first initialization.
   If the backend has been updated run commands 1 and 2 before running this one.
`python .\manage.py runserver`


# How to use the Application

The documentation on how to use the application can be found in the PDFs found in `/documentation/pdf`.

If you are a new user please refer to the registration first before going into the specific How To for your use case 
