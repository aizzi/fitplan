FROM aizzi/devcontainers:ubuntu24.04.python3.12.poetry1.8

# Update and upgrade
RUN apt-get update -y \
    && apt-get upgrade -y

# Install sqlite3
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends sqlite3