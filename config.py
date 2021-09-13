import os
from dotenv import load_dotenv

load_dotenv()

DB_SQLITE_NAME = os.getenv('DB_SQLITE_NAME')
UNMSM_RESULTS_PAGE_URL = os.getenv('UNMSM_RESULTS_PAGE_URL')
