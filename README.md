# Python App Starter Kit

## Get Started

### Prerequisites

- >= Python 3.6

### Clone this repo

```bash
git clone https://github.com/sravanrekandar/swim-train-app.git && cd swim-train-app
```

### Install dependencies

This stater kit assumes you have 'python' as the interpreter.
If your python interpreter is 'python3', rename 'python' with 'python3' in ```start.sh``` and ```start.bat```

#### For windows users

```bash
setup.bat
```

#### For Linux/Mac users

Set the permissions: This is required only one time

```bash
chmod 777 setup.sh
```

Run the Setup

```bash
./setup.sh
```

## Activate virtual environment

For Windows Users

```bat
.venv/Scripts/activate
```

For mac/Linux Users

```bash
source .venv/bin/activate
```

## Start the app

```bash
uvicorn main:app --reload
```

Now navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs#/)
