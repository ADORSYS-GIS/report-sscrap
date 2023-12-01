When we talk about code modularization it is all about separating the given project into separate portions in our case scraping which would be broken down into smaller portions or task to carry out to make it easier to understand. we could follow the following:

- Firstly in our project we would import different libraries in our code which would help us carry out different task. here we would be using beautifulsoup, pandas, flask, notebook, chart js etc
to install our library we would do
```pip install <library-name>```

- Furthermore, we move next in building our modules in each module we create functions and where necessary import a library that would help us to the specific task and in that way we can create our function and save it which can be called in other modules for use
an example of the module is
# app.py
import <library-name>
def fuction():
    #unknown implementations

- Inaddition, after writing the intended module we have to do a documentation it is help the non developers understand the way our output is

- Also, it is necessary to catch errors in our modules and be able to handle the errors which has been foumd and as such we would make use of the try and except in handling errors and exceptions in our codes

- Finally, we can not say our scripts are perfect if we do not carry out testing. the testing would enable use to know that our modules function correctly and also that it produces the intended result for which it was written for