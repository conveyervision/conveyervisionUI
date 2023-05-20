# Pull the base image
FROM python:3.8-slim-buster

# Install git, ssh, and postgres client
RUN apt-get update && apt-get install -y git openssh-client libpq-dev gcc

# Set work directory
WORKDIR /code

# Copy the requirements file and SSH key into the image
COPY requirements.txt id_rsa /root/

# Install pip dependencies
RUN pip install --no-cache-dir -r /root/requirements.txt

# Set up SSH
RUN mkdir -p -m 0600 ~/.ssh && \
    cp /root/id_rsa ~/.ssh/id_rsa && \
    chmod 600 ~/.ssh/id_rsa && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts

# Clone the git repo
RUN ssh-agent bash -c 'ssh-add /root/.ssh/id_rsa; git clone git@github.com:conveyervision/conveyervisionUI.git .'

# Remove unnecessary packages
RUN apt-get autoremove -y gcc

# Command to run on container start
CMD [ "python", "conveyervisionUI/manage.py", "runserver", "0.0.0.0:8000" ]

