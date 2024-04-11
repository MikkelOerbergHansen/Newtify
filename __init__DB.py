


import sqlite3


#### DDL operations


drop_table_Subscriptions = """DROP TABLE IF EXISTS Subscriptions"""

create_table_Subscriptions = """CREATE TABLE Subscriptions (
                        Subscription_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Subscription_Name TEXT NOT NULL,
                        Price TEXT NOT NULL
                        );
                        """



drop_table_Avatars = """DROP TABLE IF EXISTS Avatars"""

create_table_Avatars = """CREATE TABLE Avatars (
                        Avatar_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Avatar_Name TEXT NOT NULL,
                        File_Path TEXT NOT NULL
                        );
                        """




drop_table_USERS = """DROP TABLE IF EXISTS USERS"""

create_table_USERS = """CREATE TABLE USERS (
                        User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Email TEXT NOT NULL,
                        Password TEXT NOT NULL,
                        Subscription_ID INTEGER NOT NULL,
                        Newsletter TEXT NOT NULL,
                        SignUp_Date TEXT NOT NULL,
                        Username TEXT NOT NULL,
                        Credits TEXT NOT NULL,
                        Avatar_ID INTEGER NOT NULL,
                        FOREIGN KEY (Subscription_ID) REFERENCES Subscriptions(Subscription_ID),
                        FOREIGN KEY (Avatar_ID) REFERENCES Avatars(Avatar_ID)
                        );
                        """




drop_table_Artists = """DROP TABLE IF EXISTS Artists"""

create_table_Artists = """CREATE TABLE Artists (
                        Artist_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Email TEXT NOT NULL,
                        Password TEXT NOT NULL,
                        ArtistName TEXT NOT NULL,
                        Subscription_ID TEXT NOT NULL,
                        SignUp_Date TEXT NOT NULL,
                        CoverArt_filepath TEXT NOT NULL,
                        FOREIGN KEY (Subscription_ID) REFERENCES Subscriptions(Subscription_ID)
                        );
                        """


drop_table_Following = """DROP TABLE IF EXISTS Following"""

create_table_Following = """CREATE TABLE Following (
                        Follow_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        User_ID TEXT NOT NULL,
                        Artist_ID TEXT NOT NULL,
                        FOREIGN KEY (User_ID) REFERENCES USERS(User_ID),
                        FOREIGN KEY (Artist_ID) REFERENCES Artists(Artist_ID)
                        );
                        """


drop_table_Donations = """DROP TABLE IF EXISTS Donations"""

create_table_Donations = """CREATE TABLE Donations (
                        Donation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        User_ID TEXT NOT NULL,
                        Artist_ID TEXT NOT NULL,
                        Credit_amount Integer NOT NULL,
                        Date TEXT NOT NULL,
                        FOREIGN KEY (User_ID) REFERENCES USERS(User_ID),
                        FOREIGN KEY (Artist_ID) REFERENCES Artists(Artist_ID)
                        );
                        """



drop_table_Playlist = """DROP TABLE IF EXISTS Playlist"""

create_table_Playlist = """CREATE TABLE Playlist (
                        Playlist_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Playlist_Name TEXT NOT NULL,
                        Creation_Date TEXT NOT NULL,
                        User_ID TEXT NOT NULL,
                        FOREIGN KEY (User_ID) REFERENCES USERS(User_ID)
                        );
                        """




drop_table_Album = """DROP TABLE IF EXISTS Album"""

create_table_Album = """CREATE TABLE Album (
                        Album_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Album_name TEXT NOT NULL,
                        Release_date TEXT NOT NULL,
                        Artist_ID TEXT NOT NULL,
                        AlbumCoverArt_filepath TEXT NOT NULL,
                        FOREIGN KEY (Artist_ID) REFERENCES Artists(Artist_ID)
                        );
                        """



drop_table_Songs = """DROP TABLE IF EXISTS Songs"""

create_table_Songs = """CREATE TABLE Songs (
                        Song_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Song_name TEXT NOT NULL,
                        Duration TEXT Not NULL,
                        Album_ID INTEGER NOT NULL,
                        Artist_ID INTEGER NOT NULL,
                        Track_num INTEGER NOT NULL,
                        filepath TEXT NOT NULL,
                        FOREIGN KEY (Album_ID) REFERENCES Album(Album_ID),
                        FOREIGN KEY (Artist_ID) REFERENCES Artists(Artist_ID)
                        );
                        """




drop_table_PlaylistSongs = """DROP TABLE IF EXISTS PlaylistSongs"""

create_table_PlaylistSongs = """CREATE TABLE PlaylistSongs (
                        Entry_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Playlist_ID TEXT NOT NULL,
                        Song_ID TEXT NOT NULL,
                        FOREIGN KEY (Playlist_ID) REFERENCES Playlist(Playlist_ID),
                        FOREIGN KEY (Song_ID) REFERENCES Songs(Song_ID)
                        );
                        """


drop_table_Likes = """DROP TABLE IF EXISTS Likes"""

create_table_Likes = """CREATE TABLE Likes (
                        Likes_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        User_ID INTEGER NOT NULL,
                        Song_ID INTEGER NOT NULL,
                        FOREIGN KEY (User_ID) REFERENCES USERS(User_ID),
                        FOREIGN KEY (Song_ID) REFERENCES Songs(Song_ID)
                        );
                        """








with sqlite3.connect('static/DB_Newtify.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table_Subscriptions)
    cur.execute(create_table_Subscriptions)
    
    cur.execute(drop_table_Avatars)
    cur.execute(create_table_Avatars)
        
    cur.execute(drop_table_USERS)
    cur.execute(create_table_USERS)

    cur.execute(drop_table_Artists)
    cur.execute(create_table_Artists)

    cur.execute(drop_table_Following)
    cur.execute(create_table_Following)

    cur.execute(drop_table_Donations)
    cur.execute(create_table_Donations)

    cur.execute(drop_table_Playlist)
    cur.execute(create_table_Playlist)

    cur.execute(drop_table_Album)
    cur.execute(create_table_Album)

    cur.execute(drop_table_Songs)
    cur.execute(create_table_Songs)

    cur.execute(drop_table_PlaylistSongs)
    cur.execute(create_table_PlaylistSongs)

    cur.execute(drop_table_Likes)
    cur.execute(create_table_Likes)




































