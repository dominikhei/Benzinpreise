## MySQL Datenbank

Die Daten werden in eine MySQL Datenbank geladen, welche auf dem lokalen System
ist und nicht in einem Docker Container. Man muss also MySQL auf dem Host
installiert haben. Die Tabelle wird automatisch durch das
Skript erstellt, allerdings muss man noch ein neues Datenbankschema erstellen.
Dieses sollte den Namen <ins>Benzinpreise</ins> haben.

Das Skript verbindet sich über MySQLConnector mit der lokalen Datenbank.
Das Datenbankpasswort sollte vom Benutzer selbst in dem benzinpreis_secrets.py
File, unter der Variable DB_PW festgelegt werden.
