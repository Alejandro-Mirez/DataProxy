# Project preparation:

Install:

* `pipenv`
* `pip install "uvicorn[standard]"`

Run:

* `pipenv sync`
* `uvicorn main:app --reload --app-dir app --reload-dir app`
