# 🎵 Time-Traveling Billboard Playlist Creator 🕰️

Ever wondered what the Billboard Hot 100 looked like on your birthday?
🚀 This nifty little script will scrape the Billboard Hot 100 for any date you want,
then create a Spotify playlist just for you! 🥳

## How It Works 🔧
1. Scrape Billboard 100 🕵️‍♂️:
   * The script uses BeautifulSoup to scrape the Billboard Hot 100 for your chosen date. 📅
   * Get ready to be teleported back in time! 🌌

2. Spotify Authentication 🔑:
    * Using Spotipy, the script authenticates with your Spotify account. 🎧
    * Don’t worry, your secrets are safe with us! 🤐

3. Song Searching 🔍:
    * The script searches Spotify for each song from the Billboard list. 🎶
    * If a song doesn’t exist on Spotify, it’ll be skipped (sorry, rare gem hunters!). 💎

4. Playlist Creation 📝:

    * A new private playlist is created in your Spotify account. 🕺
    * All found songs are added to this playlist. Your personal time capsule is ready! 🚀

## Installation 🛠️

1. Clone the repo:

```shell
https://github.com/YNhuLe/API.git
```
2. Install dependencies:

```shell
pip install -r requirements
```
3. Set up environment variables (make sure to keep your secrets secret 🤫):

```shell
export CLIENT_ID='your_spotify_client_id'
export CLIENT_SECRET='your_spotify_client_secret'

```
## Usage 🚀

1. Run the script: run the script from the Spotifier module
```shell
python -m Stock_Trading.Spotifier.music
```

2. Input the date in the format YYYY-MM-DD when prompted. 📅
3. Enjoy your new playlist and take a musical journey back in time! 🎧

## Fun Fact 🤓
Did you know? This script could bring back forgotten bangers and one-hit wonders! 🎵

## Disclaimer 📝
* Use responsibly. Time-traveling playlists might cause severe nostalgia. 😭
* We are not responsible for any embarrassing dance moves this script might inspire. 🕺💃

## Contributing 🤝
Feel free to submit pull requests or fork this repo. Let’s make time-traveling music even more fun! 🎶

Enjoy your musical time machine! 🎉🕰️
## Dev 👩‍💻
[Jenny Le]