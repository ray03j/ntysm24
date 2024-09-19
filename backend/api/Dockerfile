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
RUN pip install --no-cache-dir -r requirements.txt &&\
    rm -rf ~/.cache/pip

# expose the port.
EXPOSE 8000

# 自己署名証明書をコンテナにコピー


# command to run the app using uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]