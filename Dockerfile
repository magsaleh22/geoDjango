# Pull base image
FROM python:3.10.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN chmod +x ./setup_server.sh
RUN pip install -r requirements.txt

# Setup GDAL
RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    --no-install-recommends \
    binutils libproj-dev gdal-bin python3-gdal \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

# set work directory
WORKDIR /app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT = ['/app/setup_server.sh']
CMD ["python"]
