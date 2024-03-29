FROM python:3.9.7

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY app.py .

CMD ["python","app.py"]