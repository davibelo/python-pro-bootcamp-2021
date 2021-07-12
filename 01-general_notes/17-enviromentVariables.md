# Environment Variables

An environment variable is a dynamic-named value that can affect 
the way running processes will behave on a computer. 
They are part of the environment in which a process runs

## USING SYSTEM ENVIRONMENT VARIABLES (LINUX)

To see linux environment variables type on console:

        $ env

To add environment varible on linux type on console:

        $ export VARIABLE=VALUE

> or edit /usr/bin/env, adding your variables

To load a environment variable on python file, you can use:      

        import os
        variable = os.environ.get("VARIABLE")


If you want to protect some information using environment variables:

1. load your information manually on system environment Variables
    and after that, call it inside your code, or
    
2. load your information automatically adding export command lines on 
    scheduled tasks with variables information:
    
    example: 

        export KEY="your key here"; python3 main.py

## USING .ENV FILES

Instead of using system environment variables, you can use .env files:

To use .env variables on python:
1. Install dotenv module on your project:
        
        (venv1) $ pip install python-dotenv

2. Create a .env file with variables will want to load:

        VARIABLE1 = "string"
        VARIABLE2 = 10

3. Call .env variables inside your main.py:
        

        # importing required modules
        from dotenv import load_dotenv
        import os

        # getting actual directory and making a rel path
        REL_PATH = f"{os.path.dirname(__file__)}/"

        # loading environment variables
        load_dotenv(dotenv_path=f"{REL_PATH}.env")


4. Protect .env file on gitignore to don't send it to your repository:        

        # environment files
        .env


## OTHER SITUATIONS

Depending on the web site service that you will put your code to,
it can use a different way to load system environment variables.