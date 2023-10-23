FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000


ENV DJANGO_SETTINGS_MODULE=stocks_products.settings
ENV DATABASE_URL=sqlite:///db.sqlite3


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]