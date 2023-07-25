IMAGE_NAME = mongodb
CONTAINER_NAME = docker-mongodb

default: build

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d -p 27017:27017 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

clean: stop
	docker rmi $(IMAGE_NAME)

restart: stop run

logs:
	docker logs $(CONTAINER_NAME)
