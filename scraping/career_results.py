from database.models.career_result import CareerResult
from scraping.helpers import get_and_parse, flatten, parse_float, clean_str, parse_int


def build_row_obj(tags):
    val = [tag.text for tag in tags]
    return CareerResult(
        code=clean_str(val[0]),
        names=clean_str(val[1]),
        eap=clean_str(val[2]),
        score=parse_float(val[3]),
        merit=parse_int(val[4]),
        obs=clean_str(val[5]),
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


def build_page_url(base, uri):
    return f"{base}/{uri}"


def get_all_page_urls(base_url, soup):
    tags_a = soup.find("tfoot").find_all("a")
    urls = []
    for tag_a in tags_a:
        url = build_page_url(base_url, tag_a.attrs['href'])
        urls.append(url)
    return urls


def scrap_results(base_url, first_page_url):
    soup = get_and_parse(first_page_url)
    urls = get_all_page_urls(base_url, soup)

    objs = []
    for url in urls:
        print(f'scraping: {url}', end=' = ')
        sp = get_and_parse(url)
        obj = get_results_from_page(sp)
        objs.append(obj)
        print(f'DONE ({len(obj)})')

    res = flatten(objs)
    print(f'total: {len(res)}')
    return res
