FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py","runserver" ]