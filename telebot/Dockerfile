FROM python:3.9

WORKDIR /usr/src/telebot

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .

CMD ["python3", "./bot.py"]


