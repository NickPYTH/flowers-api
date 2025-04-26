FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
WORKDIR /app/flowersshop
CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]