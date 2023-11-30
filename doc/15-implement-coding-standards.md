# Coding Standards

Coding standards are a set of rules, guidelines, and best practices that help developers create code that is easy to read, understand, and maintain. Coding standards can vary depending on the organization, language, or platform. They cover aspects like formatting, naming, indentation, comments, and more. Coding standards have many benefits, such as improving code quality, increasing efficiency, facilitating collaboration and ensuring compatibility

The following coding standards are enforced for readability and consistency throughout the project:

# Naming Conventions

-Use descriptive and meaningful names for variables, functions, classes, and files.
-Use snake_case for variables and functions, and PascalCase for classes.
-Use lowercase letters for file names, and separate words with underscores.
-Use singular nouns for class names, and plural nouns for collection variables.
-Use verbs for function names, and nouns or adjectives for variable names.
-Use prefixes like is_, has_, or get_ for boolean or getter functions.
-Use suffixes like _url, _list, or _dict for variables that store URLs, lists, or dictionaries.
-Avoid using abbreviations, acronyms, or numbers in names, unless they are well-known or obvious.

# Code Structure

-Follow the PEP 8 style guide for Python code formatting and indentation.
-Use four spaces for indentation, and avoid using tabs.
-Use blank lines to separate logical blocks of code, and add comments to explain them.
-Use docstrings to document the purpose and parameters of functions and classes.
-Use parentheses to enclose complex expressions, and avoid using backslashes to break long lines.
-Use spaces around operators and commas, and avoid spaces before or after parentheses or brackets.
-Use single quotes for strings, unless they contain single quotes themselves.
-Use f-strings for string formatting, and use placeholders like {name} or {index}.
-Use list comprehensions or generator expressions for creating lists or iterating over them, instead of loops or map/filter functions.
-Use the requests library for sending HTTP requests, and handle exceptions with try/except blocks.
-Use the csv library for writing and reading CSV files, and use newline='' for opening files.
-Use the BeautifulSoup library for parsing HTML documents, and specify the html5lib parser.

# Commenting Guidelines

-Use comments to explain the logic and functionality of the code, not to repeat what the code does.
-Use # for single-line comments, and """ for multi-line comments or docstrings.
-Start comments with a capital letter, and end them with a period.
-Align comments with the code they refer to, and use the same indentation level.
-Write comments in English, and use proper grammar and spelling.
-Avoid commenting out code, unless it is for testing or debugging purposes.