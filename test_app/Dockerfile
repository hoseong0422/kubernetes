FROM python:3.9
WORKDIR /app
COPY requirements.txt .
COPY . ./

RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
