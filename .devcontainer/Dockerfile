FROM aizzi/devcontainers:python.3.12
ENV DEBIAN_FRONTEND noninteractive

# Install sqlite3
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends sqlite3

# Update and upgrade
RUN apt-get update -y \
    && apt-get upgrade -y

# Clean up
RUN apt-get purge -y imagemagick imagemagick-6-common \
    && apt-get clean