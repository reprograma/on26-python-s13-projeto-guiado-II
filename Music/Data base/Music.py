import sqlite3, csv

bank = sqlite3.connect("Best Songs on Spotify from 2000 2023.db")
cursor = bank.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Musics(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                Title INTEGER NOT NULL,\
                Artist TEXT NOT NULL,\
                Top_Genre TEXT,\
                Year INT,\
                BPM INT,\
                Energy INT,\
                Danceability INT,\
                dB INT,\
                Liveness INT,\
                Valence INT,\
                Duration INT,\
                Acousticness INT,\
                Speechiness INT,\
                Popularity)')

file = open('Best Songs on Spotify from 2000 2023.csv', encoding= "utf-8")
next(file)

content = csv.reader(file)

insert_content ="INSERT INTO Musics (Title, Artist, Top_Genre, Year, BPM, Energy, Danceability, dB, Liveness, Valence, Duration, Acousticness, Speechiness, Popularity) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM Musics"
enter = cursor.execute(select_all).fetchall()

bank.commit()
bank.close()

#...............................................................................................................

bank = sqlite3.connect("Spotify 2023.db")
cursor = bank.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Musics(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                Track_Name INTEGER NOT NULL,\
                Artist_Name TEXT NOT NULL,\
                Artist_Count INT,\
                Released_Year INT,\
                Released_Month INT,\
                Released_Day INT,\
                in_Spotify_playlist INT,\
                in_Spotify_charts INT,\
                Streams TEXT,\
                in_Apple_playlist INT,\
                in_Apple_charts INT,\
                in_Deezer_playlist TEXT,\
                in_Deezer_charts INT,\
                in_Shazam_charts TEXT,\
                BPM INT,\
                Key TEXT,\
                Mode TEXT,\
                Danceability INT,\
                Valence INT,\
                Energy INT,\
                Acousticness INT,\
                Instrumentalness INT,\
                Liveness INT,\
                Speechiness)')

file = open('Spotify 2023.csv', encoding= "latin1")
next(file)

content = csv.reader(file)

insert_content ="INSERT INTO Musics (Track_name, Artist_Name, Artist_Count,  Released_Year, Released_Month,  Released_Day,  in_Spotify_playlist, in_Spotify_charts, Streams, in_Apple_playlist, in_Apple_charts, in_Deezer_playlist, in_Deezer_charts, in_Shazam_charts, BPM, Key, Mode, Danceability, Valence, Energy, Acousticness, Instrumentalness, Liveness, Speechiness) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_content, content)

select_all = "SELECT * FROM Musics"
enter = cursor.execute(select_all).fetchall()

bank.commit()
bank.close()