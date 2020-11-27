import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

username_food = os.environ['afip_username_food']
password_food = os.environ['afip_password_food']

username_anser = os.environ['afip_username_anser']
password_anser = os.environ['afip_password_anser']

galicia_username_food = os.environ['galicia_username_food']
galicia_password_food = os.environ['galicia_password_food']
