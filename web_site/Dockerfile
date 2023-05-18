FROM python:3.9-alpine3.14

WORKDIR /usr/src/app

ENV FLASK_HOST="0.0.0.0"
ENV FLASK_APP=app
ENV FLASK_DEBUG=0

RUN apk add libffi-dev
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
