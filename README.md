# Tasks for Canal Service

## Preparation

### Step 1
Clone repository:
```sh
git clone https://github.com/arshegor/canal_service_tasks
```
### Step 2
Create source directory
```sh
cd canal_service_tasks
mkdir source
```
### Step 3
- Put into source directory **json**-file from **Google Drive Api** 
You may try this tutorial https://forbiz-online.org/kak-iz-python-podklyuchitsya-k-google-sheet/

- Change telegram TOKEN in **.env**-file

### Step 4
Install requirements

Linux/MacOS:
```sh
pip3 install -r req.txt
```
Windows:
```sh
pip install -r req.txt
```
### Step 5 
Create PostgreSQL DB from file **postgres.sql**
## Run
### Run without telegram bot
Run command:
```sh
python3 main.py --database <db name> --keyfile <path to json-file from Google Drive Api> --table <Google Sheet name> --host <DB address(localhost or another ip)> --port <db port> --env <path to .env-file>
```
### Run with telegram bot
Run command:
```sh
python3 main.py --database <db name> --keyfile <path to json-file from Google Drive Api> --table <Google Sheet name> --host <DB address(localhost or another ip)> --port <db port>
```
Example:
```sh
python3 main.py --database arshegor --env source/.env
```

# Contacts
email: arshegor@gmail.com
telegram: @kekgor

