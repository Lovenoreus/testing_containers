FROM python:3.11-slim

WORKDIR /app

#Install dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3-pip && pip3 install -r requirements.txt

#Copy the app code
COPY . .

EXPOSE 5000
CMD ["python3", "app.py"]

