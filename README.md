# Music Recommendation System

Welcome to the Music Recommendation System! This project leverages the power of the Spotify API to deliver personalized song recommendations and detailed playlist analyses. Whether you're looking to discover new music tailored to your taste or delve deeper into the characteristics of your favorite playlists, this application has got you covered.

## Features

### Get Recommendations
Enter the URL of your playlist, specify the number of songs you want, and let our recommendation engine do the rest. Using the Spotify model, the system will provide a curated selection of songs tailored to your unique musical preferences.

### Playlist Analysis
Explore your playlist in detail. The analysis feature reveals every song in your playlist along with the respective artist, giving you a comprehensive view of your musical collection.

## Project Structure

### Flask Web Application
The web application is built using Flask, providing a user-friendly interface to interact with the recommendation system. Users can input their playlist ID, request song recommendations, or analyze their playlist directly through the web interface.

### Python Scripts
The core functionality is implemented in Python, leveraging the Spotipy library to interact with the Spotify API. The scripts handle authentication, fetch playlist data, generate recommendations, and perform detailed analyses.

### HTML, CSS, and JavaScript
The front-end is crafted using HTML, CSS, and JavaScript to ensure a responsive and engaging user experience. The sidebar offers an overview of the project's features and an easy-to-navigate form for user input.

## Getting Started

### Prerequisites
- Python 3.6+
- Flask
- Spotipy
- A Spotify Developer account with client ID and client secret

### Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/music-recommendation-system.git
    cd music-recommendation-system
    ```

2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
   Create a `.env` file in the project root and add your Spotify client ID and client secret:
    ```env
    CLIENT_ID='your_spotify_client_id'
    CLIENT_SECRET='your_spotify_client_secret'
    ```

4. **Run the Application**
    ```sh
    python app.py
    ```

5. **Access the Application**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Enter Playlist ID**
   - Copy the Spotify playlist ID from your Spotify app.
   - Paste it into the "Playlist ID" field on the web app.

2. **Get Recommendations**
   - Specify the number of songs you want to be recommended.
   - Click "Get Recommendations" to receive a curated list of songs.

3. **Analyze Playlist**
   - Click "Playlist Analysis" to get detailed information about each song in your playlist.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Spotify for Developers](https://developer.spotify.com/)
- [Spotipy Library](https://spotipy.readthedocs.io/)

---

Feel free to modify the sections to better fit your specific project details and requirements.

https://github.com/harshiniraj311/spotify-based-music-recommendation-system/assets/155360804/5d4a59be-391b-4660-95e8-e54de53fc838

