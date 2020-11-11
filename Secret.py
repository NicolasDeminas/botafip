import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

password = "887Estudio"
username = "20184719968"

username_food = os.environ['username_food']
password_food = os.environ['password_food']

username_anser = os.environ['username_anser']
password_anser = os.environ['password_anser']
