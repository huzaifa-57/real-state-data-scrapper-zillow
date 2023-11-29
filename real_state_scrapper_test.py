import requests
from bs4 import BeautifulSoup
import json
import os

class RealEstateScraper:
    def __init__(self, location: str = "delaware"):
        self.location = location
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }

    def get_real_estate_data(self):
        url = f'https://www.zillow.com/homes/{self.location}_rb/'
        try:
            with requests.Session() as session:
                response = session.get(url, headers=self.headers)
                if response.status_code == 200:
                    print('Connection Establishment Success')
                    soup = BeautifulSoup(response.content, 'html.parser')
                    listings = soup.find_all('li')

                    data = []
                    i = 1
                    for listing in listings:
                        if listing is not None:
                            property_url = listing.find('a', attrs={'data-test': 'property-card-link'})
                            if property_url is not None:
                                property_url = property_url.attrs['href']
                                address = listing.find('address', attrs={'data-test': 'property-card-addr'}).text
                                title = f'Property in {self.location.capitalize()} # {i}'
                                price = listing.find('span', attrs={'data-test': 'property-card-price'}).text
                                data.append({
                                    'Title': title,
                                    'Price': price,
                                    'Address': address,
                                    'URL': property_url
                                })
                                i += 1

                    return data
                else:
                    print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
                    return None
        except requests.RequestException as e:
            print(f"Request Exception: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class DataProcessor:
    @staticmethod
    def save_to_json(data: list, filepath: str):
        if data:
            try:
                with open(filepath, 'w', encoding='utf-8') as json_file:
                    json_file.write(json.dumps(data))
                print(f'Success in saving file {filepath}')
            except IOError as e:
                print(f"IOError while saving to JSON: {e}")
            except Exception as e:
                print(f"Error while saving to JSON: {e}")


if __name__ == "__main__":
    location = 'austin' # can be changeable

    scraper = RealEstateScraper(location)
    real_estate_data = scraper.get_real_estate_data()

    if real_estate_data:
        cwd = os.getcwd()
        filename = "real_estate_data.json"
        file_path = os.path.join(cwd, filename)
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            DataProcessor.save_to_json(real_estate_data, file_path)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except Exception as e:
            print(f"An Error occurred: {e}")
