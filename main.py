from config import UNMSM_RESULTS_PAGE_URL
from scraping.persist import persist_results


def scraping_unmsm_results():
    persist_results()


if __name__ == '__main__':
    scraping_unmsm_results()
