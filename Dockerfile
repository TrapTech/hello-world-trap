FROM curlimages/curl as trapcli

# Download and install TrapCLI
ARG TRAPCLI_VERSION=1.2.1
RUN curl -f https://downloads.traptech.pl/data/TrapCLI-musl-v${TRAPCLI_VERSION} -o /home/curl_user/TrapCLI \
    && chmod +x /home/curl_user/TrapCLI

FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

# These packages are needed on alpine to run TrapCLI
RUN apk add libgcc libstdc++

COPY --from=trapcli /home/curl_user/TrapCLI /usr/bin/TrapCLI

COPY . /app

EXPOSE 80

# Run TrapCLI as a background process (necessary for health ping and certain functions),
# and the python trap as a foreground process.
CMD TrapCLI daemon & python app.py
