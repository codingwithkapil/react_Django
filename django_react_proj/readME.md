# react_Django
react with Django 


first change the DIR 

 ```linux
cd .\django_react_proj\
```

for run the project install the requiremnet

```python
pip install -t requirements.txt
```

after that change the DIR to 
 
```linux
cd .\react_app\
```
then run the react build with the command

```node
serve -s build
``` 
then change the DIR 
```
cd ..
```
and in the second terminal run the manage.py with the command 

```pytohn
python manage.py runserver localhost:5000
```

I use the localhost port 5000 because the react build run on localhost 5000 port.

