import os
from dotenv import load_dotenv

load_dotenv()

SCRAPING_PAGE_URL = os.getenv('UNMSM_RESULTS_PAGE_URL')
