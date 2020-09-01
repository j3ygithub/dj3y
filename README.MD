# dj3y
A practice project about a CRM system using Django, Django REST Framework and Vue.js

## Installation

OS X & Linux:

```
python3 -m venv /Users/jimmy_lin/envs/dj3y
source /Users/jimmy_lin/envs/dj3y/bin/activate
git clone https://github.com/j3ygithub/dj3y /Users/jimmy_lin/repos/dj3y
pip install -r /Users/jimmy_lin/repos/dj3y/requirements.txt
python /Users/jimmy_lin/repos/dj3y/manage.py runserver
```

Windows:

```
python -m venv C:\Users\jimmy_lin\envs\dj3y
C:\Users\jimmy_lin\envs\dj3y\Scripts\activate
git clone https://github.com/j3ygithub/dj3y C:\Users\jimmy_lin\repos\dj3y
pip install -r C:\Users\jimmy_lin\repos\dj3y\requirements.txt
python C:\Users\jimmy_lin\repos\dj3y\manage.py runserver
```

## History

### 2020/4/28 17:20
the package pillow may be not needed if no image field
### 2020/4/28 15:17
finished the urls namespace thing
### 2020/4/28 09:53
try reverting commit by github desktop, create database.7z
### 2020/4/27 00:19
test commit on github website page
### 2020/4/27 00:17
test commit on mac using github desktop
### 2020/4/26 21:45
make api browser url and delete work
### 2020/4/26 16:02
add model-device
### 2020/4/26 11:52 940855
update the requirement.txt
### 2020/4/26 00:41 cb55b1
adjust setting.py for leaving the DATABASES a seperate .py file and add some .gitignore configs

## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/j3ygithub/](https://github.com/j3ygithub/)

## Contributing

1. Fork it (<https://github.com/j3ygithub/dj3y/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
