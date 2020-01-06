# flask-mongo

A CRUD sample with flask-restfull, pymongo driver and some unity tests with pytest. 


## Requirements
* [A python environment with Python 3.7](https://github.com/pyenv/pyenv)
* [MongoDB](https://www.mongodb.com/download-center/community)


## Running project 

1. Install all dependencies:

```
$ pipenv install
```

2. Start your mongoDB instance : 

```
$ sudo ./mongod
```

3. Run in development mode:

```
$ python app.py
```

## Run tests

```
$ pytest test/
```

## Todo list

- [ ] Integration tests for the digimon resource
- [ ] Create a pipeline
- [ ] Add Flask Security 

## Docs

* https://flask-restful.readthedocs.io/en/latest/
* https://pymongo.readthedocs.io/en/stable/
* https://www.mongodb.com/cloud/atlas
* https://devcenter.heroku.com/categories/reference
* https://docs.pytest.org/en/latest/




