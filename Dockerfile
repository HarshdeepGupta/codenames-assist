# set base image (host OS)
FROM python:alpine3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# Add metadata to the image to describe that the container is listening on port 5000
EXPOSE 5000
# copy the content of the local src directory to the working directory
COPY src/ src

# command to run on container start
CMD [ "python", "./src/server.py" ]