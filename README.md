# Simple Blog Site

A simple blog website for blog posting. This website has authentication, database, post-create, post-update,
post-delete features. `Sqlite3` is used as the database for this website.

### Support this project

[![GitHub stars](https://img.shields.io/github/stars/rezuanul-islam-fahim/simple-blog-site?style=social)](https://github.com/Rezuanul-Islam-Fahim/simple-blog-site/stargazers) [![GitHub forks](https://img.shields.io/github/forks/rezuanul-islam-fahim/simple-blog-site?style=social)](https://github.com/Rezuanul-Islam-Fahim/simple-blog-site/network/members) [![GitHub watchers](https://img.shields.io/github/watchers/rezuanul-islam-fahim/simple-blog-site?style=social)](https://github.com/Rezuanul-Islam-Fahim/simple-blog-site/watchers) [![License](https://img.shields.io/github/license/rezuanul-islam-fahim/simple-blog-site)](https://github.com/Rezuanul-Islam-Fahim/simple-blog-site/blob/stable/LICENSE)

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

For `macOS` and `linux`:

```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Or for `windows` PC:

```bash
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

### Set Flask app and environment

For `macOS` and `linux`:

```bash
$ export FLASK_APP=app
$ export FLASK_ENV=development
```

Or for `windows` PC:

```bash
$ set FLASK_APP=app
$ set FLASK_ENV=development
```

### Initialize Database

To initialize database run this command:

```bash
$ flask init-db
```

### Run app

After initializing database, run this command to run app in a `local` server:

```bash
$ flask run
```

To view this app, open http://127.0.0.1:5000 or http://localhost:5000 in your browser.

## License

```bash
MIT License

Copyright (c) 2020 Rezuanul Islam Fahim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```