FROM python:3.7

WORKDIR /app

# Install System Dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       apt-utils \
       build-essential \
       curl \
       xvfb \
       ffmpeg \
       xorg-dev \
       libsdl2-dev \
       swig \
       python3-pip \
       python3-setuptools \
       cmake \
       python-opengl \
       dos2unix

# Output Dir
RUN mkdir -p /mnt/rw-output

# Upgrade pip
RUN /usr/bin/python3 -m pip install --upgrade pip

# Download Roadwork Server Dependencies
ADD requirements.txt .
RUN pip install -r requirements.txt

# Copy Source Code to WORKDIR
COPY . .

# Download and Install Sim Dependencies
RUN dos2unix docker/install_sim_dependencies.sh
RUN chmod a+xr docker/install_sim_dependencies.sh
RUN ./docker/install_sim_dependencies.sh

# Main Entry
RUN dos2unix docker/entrypoint.sh
RUN chmod a+xr docker/entrypoint.sh

ENTRYPOINT ["./docker/entrypoint.sh"]
CMD [ "uvicorn", "--port 3000 main:app" ]