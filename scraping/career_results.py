from database.models.career_result import CareerResult
from scraping.helpers import get_and_parse


def build_row_obj(tags):
    val = [tag.text for tag in tags]
    return CareerResult(
        code=val[0],
        names=val[1],
        eap=val[2],
        score=val[3],
        merit=val[4],
        obs=val[5],
    )


def get_row_objects(tag_rows):
    rows = []
    for tag_row in tag_rows:
        row = build_row_obj(tag_row.children)
        rows.append(row)
    return rows


def get_results_from_page(soup):
    tag_rows = soup.find("tbody").children
    return get_row_objects(tag_rows)


def scrap_results(url):
    soup = get_and_parse(url)
    objs = get_results_from_page(soup)


page_url = 'https://admision.unmsm.edu.pe/simple.old/Website/A/011/0.html'

