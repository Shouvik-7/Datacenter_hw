FROM python:3.8

WORKDIR /app

COPY main.py main_cp.py

RUN pip install pandas

CMD ["python", "main_cp.py", "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Weather%20Data/temperature.csv" ,"output.csv"]

