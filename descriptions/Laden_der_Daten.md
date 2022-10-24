## Selektieren der Daten

Das Skript bedient sich einer API

- https://creativecommons.tankerkoenig.de

Diese API stellt die Benzinpreise bereit. Hierfür muss man einen Key beantragen,
welcher in dem benzinpreis_secrets.py File gespeicherrt werden sollte, mit der
Variable: API_KEY.


Die Selektierten Daten werden dann noch gefiltert, so dass man nur die Preise
der offenen Tankstellen verwendet und dann wird mithilfe einer Schleife der
Durchschnittspreis für diesen Zeitpunkt und Ort berechnet.

Falls dieser null ist, wird er ersetzt durch den bisherigen Durchschnittspreis
für alle Einträge zu dieser Zeit. Falls dies Null ist, wird das Skript beendet,
da man somit zu diesem Zeitpunkt keinen sinnvollen Preis errechnen kann. 

Im nächsten Schritt werden die Daten in eine MySQL Datenbank geladen, mehr dazu hier:

![a](MySQL Datenbank)
