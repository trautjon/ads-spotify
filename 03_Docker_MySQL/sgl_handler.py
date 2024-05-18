from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# Verbindung zur MySQL-Datenbank herstellen
# Benutzer: root, Passwort: example, Host: localhost oder IP-Adresse des Hosts, Port: 3306
engine = create_engine('mysql://root:example@localhost:3306/spotify_data')

# Eine Tabelle definieren
metadata = MetaData()
my_table = Table('my_table', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String(50))
                 )

# Tabelle in der Datenbank erstellen
metadata.create_all(engine)
