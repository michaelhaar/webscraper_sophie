# webscraper_sophie

```shell
# Build the docker containers
docker-compose build

# Start the docker containers
docker-compose up

# Bash into the webscraper container
docker-compose run --rm webscraper bash

# Re-build PIP requirements
docker-compose run --rm webscraper pip-compile requirements/requirements.in
```
