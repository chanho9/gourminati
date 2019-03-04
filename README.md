# Gourminati

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Releases](https://img.shields.io/github/release/chanho9/gourminati/all.svg?style=flat-square)](https://github.com/chanho9/gourminati/releases)
[![LICENSE](https://img.shields.io/github/license/chanho9/gourminati.svg?style=flat-square)](https://github.com/chanho9/gourminati/blob/master/LICENSE)

Gourminati is a compound word of gourmet and illuminati. 
We want to produce a restaurant guide only consisting of insider's information against the overflowing wrong restaurant information.

## Getting Started

##### Step 1: Download the code, prepare for deployment.
To get the latest code and prepare a virtual environment.

```
$ git clone https://github.com/chanho9/gourminati.git
$ cd gourminati
$ virtualenv venv
```

##### Step 2: Deploy a server.

```
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ export FLASK_APP=gourminati.py
(venv) $ flask run

/* If you want to stop server, press ctrl+c. */

(venv) $ deactivate
```
