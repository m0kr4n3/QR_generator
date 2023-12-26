# QR_generator
A simple QR code generator application developed with Flask.

![app](app.png)

Python version: 3.11.0


## Installation and usage
- clone the repository
```bash
git clone git@github.com:m0kr4n3/simple_qr_generator.git
cd QR_generator/app/
```
1) Using python
- use `venv` virtual environment
```bash
pip3 install venv
python3 -m venv venv
source $PWD/venv/bin/activate
```

- Install dependencies
```bash
pip install -r requirements.txt
```

- Run main.py
```bash
python3 main.py
```

2) Using docker
Install docker-compose if it's not  done already
```bash
sudo apt install docker-compose
```
- Run docker-compose in the repo root directory :
```bash
sudo docker-compose up
```