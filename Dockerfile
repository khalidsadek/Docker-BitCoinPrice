FROM python:3.9.7

WORKDIR /dk-project

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY bitcoin.py .

CMD ["python","bitcoin.py"]