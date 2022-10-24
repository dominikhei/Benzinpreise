## Airflow & Docker

### Airflow

Damit das Skript alle 15 Minuten ausgeführt wird, habe ich Apache Airflow veewendet.
Airflow selbst muss noch über einen Docker Container installiert werden. Eine
gute Anleitung hierzu findet sich hier:
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

Sobald Airflow über Docker installiert wurde, muss man den ![a](airflow_dag/tankdaten_dag.py) File
in den Dag-Ordner von Apache Airflow verschieben.
Der DAG bedient sich des Docker Operators um das Image des Skriptes auszuführen.
Wie man das Docker Image erstellt, werde ich im folgenden beschreiben.

### Docker

Ich verwende Docker, da ich somit Funktionalität über verschiedene Systeme sicherstellen
kann. Der Container wird selbst von Airflow mit dem Docker Operator erstellt und ausgeführt.
Das Image, also sozusagen die Blaupause für den Container enthält den Code und alle Bibiliotheken.
Der Container führt dann den Code aus.

Um das Image zu erstellen muss man über die Kommandozeile mit dem cd Kommando in
den loading_script Ordner navigieren, in welchem sich der Dockerfile, das Skript
und der Secrets File befinden. In diesem Ordner muss das Kommando:

<ins>docker build -t "tanke" .</ins>

Das Image besitzt somit den Namen tanke und wird über diesen Namen auch von Airflow
ausgeführt. 
