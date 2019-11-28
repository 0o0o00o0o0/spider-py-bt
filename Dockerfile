FROM python:3.6
COPY ./Hongkong /etc/localtime
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install pymysql
# CMD ["python3", "index.py"]

# CMD ['source',' venv/bin/activate']