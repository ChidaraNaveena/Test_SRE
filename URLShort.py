import random
import string
import webbrowser
import pickle

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.load_data()

    def save_data(self):
        with open('url_map.pkl', 'wb') as f:
            pickle.dump(self.url_map, f)

    def load_data(self):
        try:
            with open('url_map.pkl', 'rb') as f:
                self.url_map = pickle.load(f)
        except FileNotFoundError:
            self.url_map = {}

    def generate_short_url(self, long_url):
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[short_code] = long_url
        self.save_data()
        return f"https://short.url/{short_code}"

    def navigate_to_url(self, short_url):
        short_code = short_url.split('/')[-1]
        long_url = self.url_map.get(short_code)
        if long_url:
            webbrowser.open(long_url)
        else:
            print("Short URL not found.")

# Example Usage
shortener = URLShortener()
short_url = shortener.generate_short_url('https://www.example.com')
print("Short URL:", short_url)
shortener.navigate_to_url(short_url)
