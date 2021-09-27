# Bastellösung, um serielle Schnittstellen in einem Docker Container unter Windows zu lesen

## Anleitung in Windows:

1. `com2tcp.exe` downloaden und in einen Ordner der Wahl packen.

2. Die Batch Datei `start_com2tcp.bat` ausführen.

3. Anschließend in der Dockerfile die Host IP-Adresse angeben.

4. `docker build -t name/imagename:tag` ausführen.

5. `docker run name/imagename:tag`

Viel Vergnügen!