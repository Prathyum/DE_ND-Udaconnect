FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
RUN pip3 install --upgrade pip && \
        pip3 install -r requirements.txt

CMD ["python3", "main.py"]