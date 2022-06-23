Subscription service Allocate route version 1.0 beta for file uploads
=====================================
Public repository of assistance to users of Grasp Subscription-service allocate route.

.. contents::

- General information
- Authorization
- Usage
- Project structure

General Information
-------------------

- Website: https://www.grasplabs.no
- Contact: <mailto:hello@grasplabs.no>
- Issue tracker: https://github.com/grasp-labs/AllocateFiles/issues
- Documentation: https://grasp-daas.com/api/subscription/v1/docs#/Allocate/allocate_file_api_subscription_v1_allocate_upload_file__post

Authorization
-----------------------

Using Grasp service assets in general require a registered account. To use Subscription service
in particular you will need client_id and secret for a Oauth2.0 client credential authorization flow.

Usage
-----------------------
### Clone repo
Open a terminal window.
CD into your project folder (or mkdir <your-folder-name> if you want a new one)
call git clone https://github.com/grasp-labs/AllocateFiles.git
CD into AllocateFiles
...

### Setup python virtual environment
...
We have setup this project for simple calls from project root.
To setup a python virtual environment we suggest using pipenv and Pipfile's (the lock should be up to date).
call pipenv install from root and a python 3.8 environment should be setup with the required libraries.
Once

#### Environment variables
Client ID and client secret needs to be collected to authorization purposed.
If you find yourself in want of credentials, please contact us.

Current shell and all processes started from current shell:
(windows)
set GRASP_DEMO_CLIENT_ID = <your client id>

set GRASP_DEMO_CLIENT_SECRET =<your secret>

(bash)
export GRASP_DEMO_CLIENT_ID="<your client id>"

export GRASP_DEMO_CLIENT_SECRET="<your secret>"

### Scripts
To execute scripts you should only need to update config.py with your credentials, but
feel free to change configurations (/config.py) or execution settings (scripts/allocate_csv.py etc),
or the parsing of arguments (allocate.py).

Argparse is setup to parse command-line arguments when calling script from python.

call -h (help) to output instructions
````commandline
pipenv run python scripts\allocate.py --h

usage: Subscription service allocate file assets [-h] [--f F] [--o O] [--d D] [--i I]

Sample script for uploading files.

optional arguments:
  -h, --help  show this help message and exit
  --f F       Specify file format suffix
  --o O       Json file orientation
  --d D       CSV file delimiter
  --i I       Primary key in file

File should momentarily be available for consumption.

````
call --f csv to run program uploading a sample csv file.
where --f == format, options are csv, json & parquet
````commandline
pipenv run python scripts\allocate.py --f csv --d , --i id
Success! .. sample.csv uploaded.

pipenv run python scripts\allocate.py --f json --o column --i id
Success! .. sample.json uploaded.

pipenv run python scripts\allocate.py --f parquet --i id
Success! .. sample.parquet uploaded.
````

### Run your own files
Simply change the sample file content and run script.

Project structure
-----------------------

├───libs
│   └───authorization
├───samples
│   └─── sample.csv
│   └─── sample.json
│   └─── sample.parquet
└───scripts
│   └─── allocate_csv.py
│   └─── allocate_json.py
│   └─── allocate_parquet.py
config.py <-- this
