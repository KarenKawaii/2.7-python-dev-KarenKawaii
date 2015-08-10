# 2.7-python-dev-KarenKawaii
This project includes exercises from the book Python for everyone by Raúl González Duque.
The exercises range from the first chapter to the Regular Expressions (regex) chapter.

You can also install bpython for learning.

NOTE: Your exercises can be tested by flake8 and pylint.


You can install with next commands:

```bash
# apt-get install pylint python-flake8
```
You need the file:
.pylint.cfg (if you don't have it, don't worry the commands still work)

e.g.
You can execute test locally with the next commands after copy and paste the .pylint.cfg file (if you have it) to the folder:
```bash
cd /home/user/2.7-python-dev-KarenKawaii/pythonexercises/introduction
flake8 . --exclude=__init__.py && echo $?  # python guidelines
pylint --rcfile=.pylint.cfg *.py && echo $?  # python guidelines
```
"If exit with 0 (zero) each command and don't show errors your code is very good!" (moylop260)

WARNING: The prints in the following examples are for didactic principles. Do not send your code with prints or raw_input, etc. to production.
