from bs4 import BeautifulSoup # type: ignore
import sys
import requests # type: ignore

url = "https://data.1337ai.org/"

def main():
    response = requests.get(url)
    if response.status_code != 200:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    title_1 = soup.find_all("th")
    with open("file2.csv", "w") as f:
        for td_1 in title_1:
              f.write(td_1.text.strip() + ", ")
        f.write("\n")
        titles = soup.find_all("tr")
        for title in titles:
            title_2 = title.find_all("td")
            for td in title_2:
                f.write(td.text.strip() + ", ")
            f.write("\n")

if __name__ == "__main__":
    main()