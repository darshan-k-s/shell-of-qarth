# SHELL OF QARTH

A custom *Game of Thrones* themed Linux shell, built using Python 3.6.9. It implements several default Linux commands as well as a few custom commands that we found as a useful addition to the shell. 
It was created as a mini project for the Operating Systems lab.

# Setting up the Shell of Qarth

### Prerequisties
- A working python installation with either `pip` or `conda`, at least Python version >= 3.6. Verify the installation by running `python3 -V`. 
- Access to a terminal to run the Python script.

## Getting it running
### Creating a virtual environment
- Verify that either `pip` or `conda` exists on your system by running either `conda -V` or `pip -V`. If not, correct your Python installation.
- To create a virtual environment with pip follow these steps:
    - Install virtualenv with the following command ```pip install virtualenv```.
    - After it installs, run ```virtualenv <env_name>``` to create your virtual environment for this project. Replace <env_name> with any name of your choice.
    - After the environment is created, run ```source <env_name>/bin/activate``` to activate your environment.
- Once the environment is created, you should see your environment name as a prefix to your prompt in your terminal. 

### Installing the required external modules
All the external modules required are present in the `requirements.txt` file. To install these required modules, follow these steps
- Open up a terminal in the root of the project.
- Activate your environment by running ```source <env_name>/bin/activate```, like in the previous step.
- Run ```pip install -r requirements.txt```
This should install all the required modules in your project environment.
Now you are all set to run the shell!

### Running the shell
Shell of Qarth currently does not have a GUI of its own. It runs as a sub-shell of your existing shell in Linux, but supports all its commands independently.
- Open a terminal in the root of the project.
- Run ```python3 shell.py``` to get the shell running.

If you have completed all the above steps successfully, then you should see a screen similar to the one below.


![](https://raw.githubusercontent.com/darshan-k-s/shell-of-qarth/master/extras/shell.png?token=GHSAT0AAAAAABZ5UY5AZWY4VFEP7HISBD2OY2YDCUA)

Congratulations! You have successfully run the Shell of Qarth!

# Contributors
The Shell of Qarth was built by a team of five people including [Darshan K S](https://github.com/darshan-k-s), Aayush Patney, Pushkar Anand, Mitul Agarwal and Samir Kurup.