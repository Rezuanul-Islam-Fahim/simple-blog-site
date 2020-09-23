# Simple Blog Site

A simple blog website for blog posting. This website has authentication, database, post-create, post-update,
post-delete features. Sqlite3 is used as the database for this website.

## Installation

* [Clone Repository](#clone-repository)
* [Create Virtual Environment and Activate it](#create-virtual-environment-and-activate-it)
* [Set Flask app and environment](#set-flask-app-and-environment)
* [Initialize Database](#initialize-database)
* [Run app](#run-app)

### Clone Repository

```bash
# Clone the repository
$ git clone https://github.com/Rezuanul-Islam-Fahim/simple-blog-site

# Navigate to the project folder
$ cd simple-blog-site
```

### Create Virtual Environment and Activate it

**For macOS and linux:**

```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

**Or for windows PC:**

```bash
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

### Set Flask app and environment

**For macOS and linux:**

```bash
$ export FLASK_APP=app
$ export FLASK_ENV=development
```

**Or for windows PC:**

```bash
$ set FLASK_APP=app
$ set FLASK_ENV=development
```

### Initialize Database

To initialize database run this command from project's root folder:

```bash
$ flask init-db
```

### Run app

After initializing database, run this command to run app in a local server:

```bash
$ flask run
```

To view this app, open http://127.0.0.1:5000 or http://localhost:5000 in your browser.