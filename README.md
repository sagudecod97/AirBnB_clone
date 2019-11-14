# AirBnB clone - The console

<p align="center">
    <img src="https://i.imgur.com/FAAIUWB.png">
</p>    

## Description

This team project is part of the Holberton School Full-Stack Software Engineer program.
This is the first step towards building a first full web application: an AirBnB clone.
This step consists of a command interpreter limited to a specific use-case.
We're to be able to manages:

    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file
    Do operations on objects (count, compute stats)
    Update attributes of an object
    Destroy an object

## Install
    Clone the repository

https://github.com/cavb28/AirBnB_clone.git

    How to it

Get into the AirBnB_clone folder and Run the executable file ./console, the command prompt now appears: (hbnb)


## Usage

This shell should work in interactive mode and also in non-interactive mode: (like the Shell project in C).
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit command to exit the program | ```(hbnb) quit```
EOF to exit the program | ```(hbnb) EOF```
Display the help for the console | ```(hbnb) help``` or ```(hbnb) ?```
Display the help for a command | ```(hbnb) help <command>```
Create an object and prints id generated | ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Count instances of a class | ```<class name>.count()```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

Non-interactive mode example

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```
## FileStorage

The folder [engine](/models/engine) manages serialization and deserialization of the data.
A FileStorage class is defined in [file_storage.py](/models/engine/file_storage.py) with methods to follow this model:
```<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>```

The file [__init__.py](/models/__init__.py) contains the instantiation of FileStorage class storage, followed by a call to the method reload() on that instance.
This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

## Models

The folder [models](/models) contains all the classes used in this project.

File | Description | Attributes
---- | ----------- | ----------
[base_model.py](/models/base_model.py) | BaseModel class defines common attributes/methods for other classes | id, created_at, updated_at
[amenity.py](/models/amenity.py) | Amenity class for amenity information | name
[city.py](/models/city.py) | City class for location (city) information | state_id, name
[place.py](/models/place.py) | Place class for lodgings information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](/models/review.py) | Review class for user review information | place_id, user_id, text
[state.py](/models/state.py) | State class for location (state) information | name
[user.py](/models/user.py) | User class for host information | email, password, first_name, last_name

## Class Diagram UML

<p align="center">
<img align="center" src="https://i.imgur.com/DQbzpUn.png">
</p>    


## Tests

The code is tested with the unittest module.
The test for the classes are in the folder [test_models](/tests/test_models).

## Authors

* **Cesar Velez** - [cavb.28@gmail.com](https://github.com/cavb28)
* **Santiago Agudelo** - [sagudecod97@gmail.com](https://github.com/sagudecod97@gmail.com)
