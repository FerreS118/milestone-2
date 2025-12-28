# Basis image met Python 3.11
FROM python:3.11   

#Zet de werkdirectory in de container op /app                   
WORKDIR /app                          

# Kopieer main.py naar de werkdirectory
COPY main.py /app                    

 # Installeer benodigde Python packages
RUN pip install --no-cache-dir fastapi uvicorn motor 

#Open poort 8000 voor toegang van buitenaf
EXPOSE 8000                            

# Start de FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  