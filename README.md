# Vendor Management System (VMS) APIs :technologist:

Hey :wave:Welcome to the Vendor Management System (VMS) APIs repository. This repository contains the backend APIs for a vendor management system with a performance matrix.

## Getting Started

Follow the instructions below to get started with the VMS project:

## 1 **Add SSH Key to GitHub Account:** 
Before cloning the repository, ensure you have set up SSH key authentication with GitHub.

## 2 **Install Docker:** 
Make sure Docker is installed on your system. If not,
> [!TIP]
> download and install it from [here](https://www.docker.com/get-started).
    
## 3 . create a vertual env.
> [!IMPORTANT]
> Before proceeding, it's recommended to set up a Python virtual environment for the project.

## 4. **Clone the Repository:** 
Clone this repository to your local machine using the following command: 
 
  
  ```
 git clone git@github.com:Ashish8329/Vendor-Management-System.git
```

## 5.  Navigate to Project Directory: 
Go to the directory where you cloned the repository.
 
## 6.  Build and Run Docker: 
Ensure Docker is running in the background. Navigate to the main directory of the project and run:
##4. Navigate to Project Directory:
Go to the directory where you cloned the repository.
> [!NOTE]
> # For the first time

```
docker-compose up --build   # For the first time
```
Or
> [!NOTE]
> # For subsequent runs
```
docker-compose up   
```

## 7. Create Superuser: 
After the project is successfully set up, create a superuser using the following command:
```
python3 manage.py createsuperuser 
```
Follow the prompts to set up the superuser credentials.:grin:  :crossed_fingers:

## 8. Explore the VMS Project: :sparkles:'
:point_right: **Congratulations**:balloon:!:tada::tada: Your VMS project is now ready to explore.:confetti_ball:	:balloon: :point_left:

# Thank You :crossed_fingers:
:sparkles::sparkles:Thank you for using the Vendor Management System (VMS) APIs. If you encounter any issues or have any feedback, feel free to contact us.:sparkles::sparkles:
# :grinning:
