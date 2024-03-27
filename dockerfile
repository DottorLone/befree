# usa una versione Python 
FROM python:3.11.5

# Setta la directory del container
WORKDIR /app

# Copia requirements.txt file nel container
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install -r requirements.txt

# Copia il codice nel container
COPY . .

# Esponi la porta dove il tuo backend girerà (cambiala con quella desiderata)
EXPOSE 8080

# fai partire il server django con manage.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
