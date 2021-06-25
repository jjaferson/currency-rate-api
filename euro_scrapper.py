from urllib.request import urlopen
from bs4 import BeautifulSoup

class EuroScrapper(): 

    def get_brl(self):
        url = "https://dolarhoje.com/euro-hoje/"
        html = self.get_html(url)
        soup = BeautifulSoup(html, "html.parser")

        brlRate = soup.find(id='nacional').get("value")
        return brlRate

    def get_html(self, url):
        page = urlopen(url)
        html_bytes = page.read()
        return html_bytes.decode("utf-8")

