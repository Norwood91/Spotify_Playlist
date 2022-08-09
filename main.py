import requests
from bs4 import BeautifulSoup


playlist_date = input('Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ')
response = requests.get(url=f'https://billboard.com/charts/hot-100/{playlist_date}')
response.raise_for_status()
playlist_data = response.text

soup = BeautifulSoup(playlist_data, 'html.parser')
song_titles = soup.find_all(name='h3', class_='c-title')
song_title_list = []


for title in song_titles:
    song_title = title.getText().strip()
    song_title_list.append(song_title)

remove_writer = 'Songwriter(s):'
remove_label = 'Imprint/Promotion Label:'
remove_gains = 'Gains in Weekly Performance'
remove_awards = 'Additional Awards'
remove_producer = 'Producer(s):'

# These list comprehensions filter the main song_title_list to exclude the above 'strings' saved to the variables.
song_title_list = [i for i in song_title_list if i != remove_writer]
song_title_list = [i for i in song_title_list if i != remove_label]
song_title_list = [i for i in song_title_list if i != remove_gains]
song_title_list = [i for i in song_title_list if i != remove_awards]
song_title_list = [i for i in song_title_list if i != remove_producer]

new_song_title_list = song_title_list[1:]
print(new_song_title_list)
