FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Users/intre/python/game-site/ms/
COPY ./req.txt /Users/intre/python/game-site/ms/req.txt
RUN pip install -r /Users/intre/python/game-site/ms/req.txt

COPY . /Users/intre/python/game-site/ms/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]