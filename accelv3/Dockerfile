# importing base image
FROM python:3.10.5-alpine

# changing current working directory to /usr/src/app
WORKDIR /app

# copying requirement.txt file to present working directory
COPY requirements.txt ./

# installing dependency in container
RUN pip install -r requirements.txt

# copying all the files to present working directory
COPY . .

# informing Docker that the container listens on the
# specified network ports at runtime i.e 8000.
EXPOSE 8000

# running server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]