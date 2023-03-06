# INFO

Script for running multipe maven microservices in one terminal window. Working on Windows.

## Additional info

- The script will run the frontend microservice last
- The script will run the microservices in the order they are listed in the MICROSERVICES_DIRS variable
- When script is placed in the same directory with DEV_DIR, the script will run the microservices from the DEV_DIR directory. Otherwise, the script will ask for the directory where the microservices are located.
- The script was prepared for maven microservices with npm at front, but it can be easily modified to run other types of microservices

# USAGE

1. Clone the repository
2. Change MICROSERVICES_DIRS variable in run.py to your microservices directories. The last directory should be the frontend directory.
3. (Optional) Replace PROJECT_NAME variable in run.py with your project name
4. (Optional) Replace DEV_DIR variable in run.py with your development directory
5. Run the script with python run.py

# REQUIREMENTS

- Python 3
- Windows Terminal (https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)
