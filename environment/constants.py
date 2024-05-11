from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the variables
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
DATABASE_HOST = os.getenv('DATABASE_HOST')

# Now you can use these variables in your code