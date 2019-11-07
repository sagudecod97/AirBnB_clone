# AirBnB clone - The console

## Description
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

    A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    A website (the front-end) that shows the final product to everybody: static and dynamic
    A database or files that store data (data = objects)
    An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## Authors
* **Cesar Augusto Velez** 
* **Santiago Agudelo Alvarez**
## Files

### Lorem Ipsum
Dummy text of the printing and typesetting industry

### _quisquam.c
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a
type specimen book. It has survived not only five centuries, but also the
leap into electronic typesetting, remaining essentially unchanged.

### dolorem.h
Header file.
* Prototypes and
* Struct definition

### size_printf.c
* Main size function.
* Handling of format string
* Call through struct to auxiliary size functions

### str_printf.c
Main string write function
Handling of format string
Call through struct to auxiliary string generation functions

### _printf_func_0.c
Auxiliary size and string generation function for
* characters (c) and
* strings (s)

### _printf_func_1.c
Auxiliary size and string generation functions for
* decimals (d) and
* integers (i)

### _printf_func_2.c
Auxiliary size and string generation function for
* bynary (b),
* unsigned (u) and
* octal (o) numbers.

### _printf_func_3.c
Auxiliary size and string generation function for
* unsigned (u) and
* hexadecimal (x, X) numbers.

### _printf_func_14.c
Auxiliary string generation function for
* reverse string (r).

### _printf_func_15.c
Auxiliary string generation function for
* string rot13 conversion (R).

### number_printf.c
Auxiliary function for numbers sizing and number conversion acording to base (b, o , x, X).
## Task
### Task 0
I'm not going anywhere. You can print that wherever you want to. I'm here and I'm a Spur for life

Function that produces output according to a format.

Prototype: int _printf(const char *format, ...);
Returns: the number of characters printed (excluding the null byte used to end output to strings)
write output to stdout, the standard output stream
format is a character string. The format string is composed of zero or more directives. See man 3 printf for more detail. 
Handles the following conversion specifiers:
c
s
%


### Task 1
Education is when you read the fine print. Experience is what you get if you don't 

Handles the following conversion specifiers:
d
i


### Task 2
Just because it's in print doesn't mean it's the gospel

Man page for the function.

### Task 3
With a face like mine, I do better in print.

Handles the following custom conversion specifiers:

b: the unsigned int argument is converted to binary 


### Task 4
What one has not experienced, one will never understand in print 

Handls the following conversion specifiers:
u
o
x
X

### Task 5
Nothing in fine print is ever good news

Uses a local buffer in order to call write as little as possible.



### Task 14
Print is the sharpest and the strongest weapon of our party

Handles the following custom conversion specifier:

r : prints the reversed string


### Task 15
The flood of print has turned reading into a process of gulping rather than savoring

Handles the following custom conversion specifier:

R: prints the rot13'ed string
