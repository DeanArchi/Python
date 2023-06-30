import requests
import random

google = "google.com"
facebook = "facebook.com"
twitter = "twitter.com"
amazon = "amazon.com"
apple = "apple.com"

links = [google, facebook, twitter, amazon, apple]
random_choice = random.choice(links)

res = requests.get(f"https://{random_choice}")
print(f"Response status code: {res.status_code}")
print(f"Site name: {random_choice}")
print(f"Length of HTML-code: {len(res.text)}")
