[![CircleCI](https://circleci.com/gh/tsoporan/fittrack/tree/master.svg?style=shield)](https://circleci.com/gh/tsoporan/fittrack/tree/master)

A no-frills fitness tracking tool for the stats inclined.

### Requirements

- [Python](https://www.python.org/) 3.6
- [pipenv](https://github.com/pypa/pipenv)
- [yarn](https://yarnpkg.com/en/)

### Set up

The backend consists of a [Django](https://www.djangoproject.com/) powered Python application which exposes a 
[GraphQL](https://graphql.org/learn/) API using [Graphene](http://graphene-python.org/).

To get it up and running:

1. Install required packages
```bash
pipenv install
pipenv shell
cd fittrak
```

2. Configure a `SECRET_KEY`
```bash
echo SECRET_KEY=\"PlsChangeMe\" > fittrak/secrets.py
```

3. Initial migration
```bash
./manage.py migrate
```

4. Set up the first user and load some fixture data
```bash
./manage.py createsuperuser
./manage.py loaddata workout
```

4. Serve
```bash
./manage.py runserver_plus # Werkzeug dev server
```

---

The frontend is a [Vue](https://vuejs.org/) powered Javascript application which uses [Apollo](https://www.apollographql.com/) as its GraphQL
client.

To get it up and running:

1. TBD
