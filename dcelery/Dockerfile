FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# Prevent Python from writing .pyc files and ensure unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy the entrypoint script
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copy the entire application code
COPY . /usr/src/app/

# Set execution permissions for entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
