FROM debian:buster-20200514

ENV LANG="en_US.UTF-8"
RUN apt update && apt install -y curl

RUN apt install -y \
    bc \
    build-essential \
    chromium \
    python-dev \
    python-pip \
    python3-dev \
    unzip

### Install chromedriver, make sure chromium version matches driver support version ###
RUN if ! curl -fL -o chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip; then \
        echo >&2 "error: failed to download chromedriver binary"; \
        exit 1; \
    fi; \
    \
    unzip \
        chromedriver_linux64.zip \
        chromedriver \
        -d /usr/local/bin/ \
        ; \
    rm chromedriver_linux64.zip; \
chmod +x /usr/local/bin/chromedriver

RUN pip install selenium
COPY . /app
CMD ["/app/run.sh"]
