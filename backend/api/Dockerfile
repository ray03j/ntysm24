# set up the container.
FROM python:3.12-slim

# set the working dir.
WORKDIR /api

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

# copy the app dir.
COPY . .

# install libraries.
RUN pip install --no-cache-dir -r requirements.txt

# expose the port.
EXPOSE 8000

# command to run the app using uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", \
     "--ssl-keyfile", "/app/localhost.key", "--ssl-certfile", "/app/localhost.crt"]
