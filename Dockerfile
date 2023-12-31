FROM python:3-alpine3.15

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -U pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]