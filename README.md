#users-service

##build docker image
>docker build . -t users-service:latest

##run docker image in a container
>docker run -itd --network redis_default -p 8002:8000 --name users-service-container -e users-db-name=users-db -e users-db-pass=usersDbPass users-service:latest
