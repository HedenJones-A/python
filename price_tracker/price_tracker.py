
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/dp/B07ZJB29YK/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B07ZJB29YK&pd_rd_w=0oX1n&content-id=amzn1.sym.413ef885-ae1b-472f-afa4-d683cda6ad0d&pf_rd_p=413ef885-ae1b-472f-afa4-d683cda6ad0d&pf_rd_r=1QYE30D4Z5WE3WQ4M6JA&pd_rd_wg=TNbSY&pd_rd_r=d7078e3b-842d-4c5d-b708-faba5e5c1804&s=books&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&smid=A2JSVZIM0C7SA7"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price_element = soup.find("span", class_="a-price-whole")
if price_element:
    price = price_element.get_text().strip()
    print(f"Product Price: ₹{price}")
else:
    print("Price not found. Amazon might be blocking the request.")
