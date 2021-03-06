# Procedural Oriented Programming

A program in a procedural language is a list of instructions 
where each statement tells the computer to do something. 

It focuses on procedure (function) & algorithm is needed 
to perform the derived computation.
Example: Fortran, Cobol...

> An analogy: One man restaurant. One man that do all the work alone step by step.

# Object Oriented Programming

Is a programming paradigm based on the concept of "objects", 
which can contain data and code: data in the form of fields 
(often known as attributes or properties), and code, in the form 
of procedures (often known as methods)

OOP allows the developer to break the whole project code into 
smaller pieces, called modules.

An analogy: A normal restaurant with a manager that leads the 
business with a specialized staff that executes specific functions on 
restaurant as waiter to get orders, chef to cook, cleaner to clean.

## Attributes and methods

OOP concept tries to model the reality.

An object HAS attributes and DOES something (methods)

Example: 
Waiter  
- attributes:
    - is_holding_plate = True
    - tables_responsible = [4, 5, 6]
- methods:
    - def take_orders(table, order)
    - def deliver_order(table, order)
    - def take_payment(amount)

> Adding new attributes beyond class attributes  
> Example:
> Imagine that class Car have only speed and fuel as attributes.  
> It is possible to set a name attribute for a car object:  
> `car.name = "toyota corolla"`  
> It is not common, but is possible.

## Class x Objects

In OOP will can have multiple instances of the same object.

In other words: 
    CLASS is a blueprint
    OBJECT is the constructed instance

 Example: The restaurant has 2 waiters (Henry and Betty)  
- Waiter is a CLASS
- Henry and Betty are OBJECTS (instances of the class)

Example in python:        
- Creating a car object from CarBlueprint class:

        car = CarBlueprint()

- Accessing object attributes:

        car.speed 
        car.fuel

- Using object methods:

        car.move()
        car.stop()

## Constructor Method (__init__ method)

The init method is called every time a new object is created from the class.  

The object will have the attributes passed by this function

Example: 

    class Car: 
        def __init__(self, seats):
            self.seats = seats

It is possible to define a default value for a attribute, so if 
the attribute is not specified on object creation, it uses that value

Example:

    class Car: 
    def __init__(self, seats = 5):
        self.seats = seats

It is possible to assign a attribute internally, 
not accessible to changing on creation:

    class Car: 
    def __init__(self):
        self.seats = 5

## Importing external modules

The great advantage of OOP is the reuse of classes.  
Modules are a bunch of classes condensed in a file

1. Importing classes directly

        from <module name> import <classes names>

    Example: module machine.py, classes Car, Truck:
    
    To import:

            from machines import Car, Truck
    To use:

            corolla = Car()
            print(corolla.speed)
            corolla.move()

2. Importing module but keeping module name

        import <module name>

    Example: module machine.py, classes Car, Bicycle    

    To import:            

            import machine  
    To use:

            corolla = machine.Car()
            print(corolla.speed)
            corolla.move()
            
3. Importing using alias

        import <module name> as <alias>
    
    Example: module machine.py, classes Car, Bicycle
    
    To import:

            import machine as m 
    To use:
    
            corolla = m.Car()
            print(corolla.speed)
            corolla.move()
    

