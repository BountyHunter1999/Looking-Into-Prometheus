FROM python:alpine3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# application run here
EXPOSE 8001

# prometheus related metrics here
EXPOSE 8000

COPY hello.py .

CMD [ "python", "hello.py" ]

