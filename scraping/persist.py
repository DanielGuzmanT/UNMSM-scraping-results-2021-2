from database.connection import DBSession
from scraping.career_results import scrap_results

base_page_url  = 'https://admision.unmsm.edu.pe/simple.old/Website/A/011'
first_page_url = 'https://admision.unmsm.edu.pe/simple.old/Website/A/011/0.html'


def persist_results():
    objs = scrap_results(base_page_url, first_page_url)
    session = DBSession()
    session.bulk_save_objects(objs)
    session.commit()
