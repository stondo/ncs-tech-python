# Nordcloud Test


## Run with docker

Build the image:

```
docker build -f Dockerfile.run -t ncs-run .
```

Run the image that will execute the code and print the solution:

```
docker run -it ncs-run
```

## Test with docker

Tests are written with pytest and Tox is used to execute them.
Take a look at `tox.ini` for the testing configuration used.


Build the image:

```
docker build -f Dockerfile.test -t ncs-test .
```

Run the image that will execute `tox -e lint` and `tox`:

```
docker run -it ncs-test
```

## Virtualenv: install dependencies, test and run

If preferred or docker is not installed, a virtualenv can be created with python3:
```
python3 -m venv /path/to/new/virtual/environment
```

activate it:
```
source <venv>/bin/activate
```

Pip install dev-requirements.txt:
```
pip install -r dev-requirements.txt
```

Run the linter:
```
tox -e lint
```

Run the tests:
```
tox
```

Run the progam:
```
python main.py
```

## Notes

Before building docker images, make sure to run `clean_pycache.py`:
```
./clean_pycache.py
```

to clean any previous local tests execution.

Also make sure `PYTHONPATH` is a valid `env` variable and it is set, otherwise `tox` will fail.

To set `PYTHONPATH` if it's empty:
```
cd /root/of/the/project && export PYTHONPATH=`pwd`
```