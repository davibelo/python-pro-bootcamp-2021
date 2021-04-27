# IDE - Integrated Development Environment
It is a tool that help to write, test, debug and run code.

# Linter
lint, or a linter, is a static code analysis tool 
used to flag programming errors, bugs, stylistic errors, 
and suspicious constructs

# Python Cloud IDE: 
https://replit.com/

# PyCharm 
IDE for Professional Python Developers with:
- Spell Check
- More Space to Develop
- built-in linter including python styling guide (PEP8)
- use local code history (access your edited code)
- view the structure of your code
- refactor rename (refactor feature on right click)
- and much more...

## Setting your local environment (PyCharm)
1. Install python
    - Windows:  
        Download installer on https://www.python.org/  
        > Select option "Install python to PATH"
    - Linux:  
            
            $ sudo apt install python3
    OBS: Some new version already come with pre-installed python
    To test it, use:

        $ python3 --version
        
    In linux pre-installed versions, could be necessary 
    to install some other packages, like:            

        $ sudo apt install python3-distutils
        $ sudo apt install python3-pip

2. Install PyCharm - Community version  
    - Download at https://www.jetbrains.com/pycharm/download/  
    - Or install with Snap Store (Ubuntu):      
    Look for it on Ubuntu Software or use command to install:
        
            $ sudo snap install pycharm-community --classic
    
3. Create a new project:  
    - Choose last python interpreter
    - Choose virtual environment            
    - Create a main.py

4. Start to code, using PyCharm features:    
    - Press Shift+F10 to execute it or replace it with your code.
    - Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
    - Use break points to debug your code (click next to the line number)
    - Press Ctrl+F8 to toggle the breakpoint.
    and much more... https://www.jetbrains.com/help/pycharm/

> PyCharm keyboard shortcuts:  
> https://www.jetbrains.com/help/pycharm/running-and-debugging-shortcuts.html?keymap=secondary_windows

> PyCharm TODO feature:  
> https://www.jetbrains.com/help/pycharm/using-todo.html

## Setting your local environment (Visual Studio Code)
1. Install python:
    - Windows:  
        - Download installer on https://www.python.org/
        - Install python to PATH
    - Linux:
     
            $ sudo apt install python3
        
        > OBS: Some new version already come with pre-installed python
        > To test it, use:

            $ python3 --version
        
        > In linux pre-installed versions, could be necessary 
        to install some other packages, distutils and pip:            

            $ sudo apt install python3-distutils
            $ sudo apt install python3-pip

2. Install Visual Code
3. Install Python and Jupyter extensions      
4. Install virtual environments package

        $ sudo apt install python3-venv

5. Create a virtual environment on your project folder named .venv
    
        $ python3 -m venv .venv        
    
    > OBS: To remove a virtual environment, just delete the .venv folder.  
    > After creating or deleting, reboot VS Code

6. Go to code command line (Ctrl+Shift+P) and type:  

        Python: Select Interpreter  
    > and select your recently created environment

7. Remember to add .venv on .gitignore (.venv/**) project file

8. Set code formatter on VSCode settings
    - Choose autopep8 or black (see observation below)
    > black formatter does not give you possibilites, it apply always the same rules.  
    > for example: autopep8 permits you to choose how to break lines and corrects indentation  
    > black will revert your break lines and make everything its way

9. Set code linter on VSCode settings
    - Enable pylint, pylama or flask8 (one at time)
    - Disable others: bandit, mypy, etc

10. Setup language server on VSCode settings
    - Choose pylance

> Using keyboard shortcuts to run parts of the code on VS Code
> - Select the lines you want to execute
> - Press Shift+Enter
> - It will open a python terminal and run the selected code
> - You can continue to select other lines and run them
>> Remember: If you want to restart the kernel, press Crtl+Z

# Python Packages:
Packages are a bunch of modules packaged together that serves some kind of functionality        
> Python packages could be found on an index:
> https://pypi.org/

## Installing python packages on Virtual Environment with VS Code:
1. If your virtual environment is not selected:
    - Go to commands field on VS Code
    - Use it to select Python interpreter with your virtual enviroment:

            Python: Select interpreter

2. Activate Virtual Environment (on VS Code Terminal): 

        $ source <venv_relative_path>/bin/activate


3. Use command line to install python packages (on VS Code Terminal)
- Example of install tk (Tkinter) package:
    - Installing on local venv .venv:

            (.venv) davibelo@ubuntu: ~/...$ python3 -m pip install tk
    - or simply:
    
            (.venv) davibelo@ubuntu: ~/...$ pip install tk
    
    > (NOT RECOMMEND, but that is possible...)  
    > Installing globally (only for packages supported by ubuntu)  
    > `(.venv) davibelo@ubuntu: ~/...$ sudo apt-get install python3-tk`  
    > More about it:  
    > https://askubuntu.com/questions/431780/apt-get-install-vs-pip-install

# Style convections on python:
- MACRO CASE = used to define constant values
- PascalCase = used in classes
- snake_case = used in objects, variables, etc...
- camelCase = not so used in python
- kebab-case = not so used in python