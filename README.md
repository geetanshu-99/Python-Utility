# CALLING CODE OF DIFFERENT LANGUAGES USING PYTHON - .NET, Java, Javascript, Julia


# Calling C# code from Python

This is a simple execution of the code, where we can execute a Code of a Calculator written in C# by calling it in Python.

For this purpose we are using [Pythonnet](https://github.com/pythonnet)

There are some pre-requistes that need to be kept in mind before executing the code:

1. You must be aware of how C# works and how to execute a C# Code.
2. You must know how to create a `.dll` file and what is its use.
3. Must be familiar with Python and how to import and use external modules.
4. Patience and Will to make the code run.

## Getting Started

1. Firstly write a very simple code to execute Addition and Subtraction of 2 numbers, in C#.

2. Now create a `.dll` file for the C# class using `csc -target:library Calculate.cs`

3. After that, install `pythonnet` using `pip install pythonnet`. For more reference on how to install pythonnet and if you face any errors, refer [here](http://pythonnet.github.io/).

4. After the installation of `pythonnet`, write the code to call C# function in Python.

5. For using the `.dll` file, use `sys.path` and mention the correct path for the `Calculate.dll` file in this case.

6. After writing the code in the python file, press `F5` to run the debugger and execute the code.

7. You should you be able to see an output like this:


![demo](/images/output.png)


## References:

1. [Pythonnet](http://pythonnet.github.io/)
2. [C#](https://docs.microsoft.com/en-us/dotnet/csharp/)
3. [Python](https://www.python.org/) 

---

# Calling Javascript code from Python

For calling JavaScript code from python, we will be using a package - __Js2Py__.


What this package does it that it _translates JavaScript code to Python code_. __Js2Py__ is able to translate and execute virtually any JavaScript code.

__Js2Py__ is written in pure python and does not have any dependencies. Basically an implementation of JavaScript core in pure python. For this example we will be using __python3__.

## Install Js2py for python
1. Open command prompt
2. Install the package using __pip__ : `pip install js2py`

## How to run
1. Open Command Prompt
2. Go to the file directory where python script is present using-
   `cd path/where/javascript_code_is_written`
3. 
```bash
python javascript.py - concat strings
python javascript1.py - area of triangle
```


![demo](/images/javascriptoutput.PNG)

## Reference

1. [Js2Py](https://github.com/PiotrDabkowski/Js2Py)
2. [Python](https://www.python.org/)

---

# Calling Java from Python

JPype

JPype is a Python module to provide full access to Java from within Python.

## Install JPype for python

1. Open command prompt
2. pip install JPype1

## How to run

1. Open Command Prompt
2. Go to the file directory where python script is present using-
   cd path/to/directory
3. python java.py


![demo](/images/javaoutput.PNG)

---

# Calling Julia from Python

pyjulia,Pycall,Julia

PyJulia provides a high-level interface which assumes a “normal” setup (e.g., julia program is in your PATH ) 

and a low-level interface which can be used in a customized setup.

## First install Julia
1. install julia from -->(https://julialang.org/)
2. Add Julia to path in environment variable

## Install Julia for Python
1. Open command prompt
2. pip install julia

## Install Packages for Julia
1. Pkg.add("PyCall")

## How to run 
1. Open Command Prompt
2. Go to the file directory where python script is present using-
   cd path/to/directory
3. python test1.py


![demo](/images/juliaoutput.PNG)

---
