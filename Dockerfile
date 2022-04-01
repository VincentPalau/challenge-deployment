FROM python:3.10
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flask numpy pandas sklearn
RUN mkdir /app
RUN mkdir /app/challenge-deployment
COPY . /app/challenge-deployment
WORKDIR /app/challenge-deployment
CMD ["python", "app.py"]
