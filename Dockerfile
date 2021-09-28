FROM python:3.9-slim

#IP Adresse vom Host
ENV IP_ADRESS = 0

#Socat + PySerial
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*
RUN pip install pyserial

#App-Ordner und Startdatei übertragen
COPY ./app /app
WORKDIR /app

#Port für Dash
EXPOSE 8050

#Startcommand
#Weitere Start Dinger, dann in der start.sh ändern
CMD ./start.sh ${IP_ADRESS}