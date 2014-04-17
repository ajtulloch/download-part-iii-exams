import requests
from bs4 import BeautifulSoup
import urlparse
from collections import defaultdict
import os
import shutil

def get_pdf_link_subject(soup, subject):
    for el in soup.findAll("th"):
        if el.get_text().strip() != subject:
            continue
        candidate = el.parent.find("a")
        if candidate is None or not candidate.has_attr("href") \
           or not candidate["href"].endswith(".pdf"):
            return None
        return candidate["href"]


def find_and_save_pdf(index, year, soup, subject):
    pdf_rel_link = get_pdf_link_subject(soup, subject)
    if pdf_rel_link is None:
        return False
    pdf_full_link = urlparse.urljoin(index, pdf_rel_link)
    filename = "pdfs/{} - {}.pdf".format(subject, year)
    download_pdf(pdf_full_link, filename)
    return True


def download_pdf(pdf_full_link, filename):
    req = requests.get(pdf_full_link)
    if req.status_code != 200:
        return False
    with open(filename, "w") as f:
        f.write(req.content)
    return True


def download_all_past_exams(years, root, subjects):
    if os.path.exists("pdfs/"):
        shutil.rmtree("pdfs/")
    os.makedirs("pdfs/")

    failures = defaultdict(list)
    successes = defaultdict(list)
    for year in years:
        index = urlparse.urljoin(root, "{}/".format(year))
        req = requests.get(index)
        soup = BeautifulSoup(req.content)
        for subject in subjects:
            if not find_and_save_pdf(index, year, soup, subject):
                failures[subject].append(year)
            else:
                successes[subject].append(year)
    print successes, failures
    print "Making archive with %s".format(successes)
    return shutil.make_archive("pdfs", "zip", root_dir="pdfs/")
