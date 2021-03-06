# IDE - Integrated Development Environment
It is a tool that help to write, test, debug and run code.

# Python Cloud IDE: 
https://replit.com/

# Visual Studio Code

## Setting your local environment (Visual Studio Code) - Debian Linux

1. Install python:
     
            $ sudo apt install python3
        
        > OBS: Some new version already come with pre-installed python.<br>
        > To test it, use:

            $ python3 --version
        
        > In linux pre-installed versions, could be necessary 
        to install some other packages, distutils and pip:            

            $ sudo apt install python3-distutils
            $ sudo apt install python3-pip

> Installing on Windows: 
> - Download installer on https://www.python.org/
> - Check "Install python to PATH" option <br>
> - For futher steps, just have in mind that principals are similar, but commands are different.

2. Install Visual Code
3. Install Python and Jupyter extensions      
4. Install virtual environments package

        $ sudo apt install python3-venv

5. Create a virtual environment on your project folder named .venv
    
        $ python3 -m venv .venv        
    
    > OBS: To remove a virtual environment, just delete the .venv folder  
    > After creating or deleting, reboot VS Code

6. Activate virtual environment:
    - Go to code command line (Ctrl+Shift+P) and type:  

        Python: Select Interpreter  
        > and select your recently created environment

    - or open a terminal and type:

            source .venv/bin/activate

7. Remember to add .venv on .gitignore (.venv/**) project file

8. Set code formatter on VSCode settings
    - Choose yapf, autopep8 or black (see observation below)
    > autopep8 is the more flexible formatter<br>
    > black formatter does not give you possibilites, it apply always the same rules and rules are fixed.<br>
    > for example: autopep8 permits you to choose how to break lines and corrects indentation, black will revert your break lines and make everything its way<br>
    > yapf acts similar to black, but the style is better than black and it has options to personalize it

9. Set code linter on VSCode settings
    - Enable pylint, pylama or flask8 (one at time)
    - Disable others: bandit, mypy, etc

    > Linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors, and suspicious constructs.



10. Setup language server on VSCode settings    

    - Choose jedi 
    > I tested in 2021-05, and only jedi have autocomplete for classes in local modules
    

    - or choose pylance, in this case, install language server extensions:
        - Pylance
        - Visual Studio IntelliCode    
    
    > Language server provide Completions, Definitions, Hover, References, Signature Help, and Symbols

11. Setup jupyter notebooks with virtual enviroments

    - after creating and activating a venv (as described above), do:
        - Install ipykernel package:

                pip install ipykernel

        - Install a new kernel:

                ipython kernel install --user --name=.venv

        > Remember to restart the Visual Studio Code and select the new kernel on jupyter notebook



> ### Using keyboard shortcuts to run parts of the code on VS Code
> - Select the lines you want to execute
> - Press Shift+Enter
> - It will open a python terminal and run the selected code
> - You can continue to select other lines and run them  
> Remember: If you want to restart the kernel, press Crtl+Z

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
    
    > (NOT RECOMMEND, but that is possible...)<br>
    > Installing globally (only for packages supported by ubuntu)<br>
    > `(.venv) davibelo@ubuntu: ~/...$ sudo apt-get install python3-tk`<br>
    > More about it:<br>
    > https://askubuntu.com/questions/431780/apt-get-install-vs-pip-install

# Creating a dependencies requirements file:

1. Use the command below to create a requirements.txt file that contains all modules installed in your environment

        $ pip freeze > requirements.txt

2. Use the command below to install all modules listed inside requirements file:

        $ pip install -r requirements.txt

# Style convections on python:
- MACRO CASE = used to define constant values
- PascalCase = used in classes
- snake_case = used in objects, variables, etc...
- camelCase = not so used in python
- kebab-case = not so used in python

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
    - Windows:<br>
        Download installer on https://www.python.org/  
        > Select option "Install python to PATH"
    - Linux:<br>
            
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

