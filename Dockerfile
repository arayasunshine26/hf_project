FROM python:3.9
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 8000
COPY app/ /app
WORKDIR /app
CMD ["python", "main.py"]