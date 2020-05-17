FROM debian:buster-20200514

RUN apt update && apt install -y git

COPY . /app
CMD ["/app/run.sh"]
