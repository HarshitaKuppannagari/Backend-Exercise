from typing import Tuple, List
from lxml import etree

def extract_non_academic_authors(article: etree._Element) -> Tuple[List[str], List[str], List[str]]:
    authors = []
    companies = []
    emails = []
    
    for author in article.findall(".//Author"):
        name = author.findtext("LastName", default="") + ", " + author.findtext("ForeName", default="")
        affiliation = author.findtext(".//AffiliationInfo/Affiliation", default="").lower()

        if not any(keyword in affiliation for keyword in ["university", "college", "school", "institute", "hospital", "centre", "center"]):
            authors.append(name)
            companies.append(affiliation.title())
        
        if "@" in affiliation:
            import re
            found_emails = re.findall(r"[\w\.-]+@[\w\.-]+", affiliation)
            emails.extend(found_emails)

    return authors, companies, list(set(emails))
