# pull official base image
#Image slim-buster de python
FROM python:3.9.5-slim-buster 

# set working directory | Repertoire de travail 
WORKDIR /usr/src/RestaurantAPI

# set environment variables | Deux variables d'environnnements ==( python -B et python -u)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# install system dependencies  | for the database configuration
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

#copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/RestaurantAPI/entrypoint.sh
#RUN chmod a+x  /usr/src/RestaurantAPI/entrypoint.sh   
RUN ["chmod", "755", "/usr/src/RestaurantAPI/entrypoint.sh"]


# add app | Copie du projet django même
COPY RestaurantAPI .


#Execution du entrypoint.sh
ENTRYPOINT ["/usr/src/RestaurantAPI/entrypoint.sh" ]

# set working directory | ceci est en fonction de l'environnement (Donc optionel)
#RUN mkdir -p /usr/src/RestaurantAPI
#WORKDIR /usr/src/RestaurantAPI