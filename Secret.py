import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

usernameFood = os.environ['afip_username_food']
passwordFood = os.environ['afip_password_food']

usernameAnser = os.environ['afip_username_anser']
passwordAnser = os.environ['afip_password_anser']

galicia_username_food = os.environ['galicia_username_food']
galicia_password_food = os.environ['galicia_password_food']
