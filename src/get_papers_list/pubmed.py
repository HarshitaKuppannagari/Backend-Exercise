import requests
from typing import List, Dict
from get_papers_list.utils import extract_non_academic_authors

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # You can increase this
    }
    search_res = requests.get(url, params=params).json()
    ids = search_res["esearchresult"].get("idlist", [])
    
    if not ids:
        return []

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    xml_data = requests.get(fetch_url, params=fetch_params).text

    # parse with lxml
    from lxml import etree
    root = etree.fromstring(bytes(xml_data, encoding='utf-8'))

    records = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year")
        authors, companies, emails = extract_non_academic_authors(article)

        records.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(authors),
            "Company Affiliation(s)": "; ".join(companies),
            "Corresponding Author Email": "; ".join(emails)
        })

    return records
