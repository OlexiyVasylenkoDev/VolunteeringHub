FROM python:3.10

RUN apt update


RUN mkdir /VolunteeringHub

WORKDIR /VolunteeringHub

COPY /src ./src
COPY /commands ./commands
COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["bash", "--reload"]

# docker run --rm -d -p 8000:8008 --name vol_hub hub
# docker logs -f vol_hub
# localhost:8000