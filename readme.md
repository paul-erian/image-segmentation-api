# image-segmentation-api

## docker

```shell
docker build -t image-segmentation-api . # create image
docker run -it -v ${PWD}/app:/app -w /app -p 8000:80 image-segmentation-api bash # create a container
docker exec -it <container> /bin/bash # connect to container
```

## lauching local serveur

```shell
uvicorn main:app --host 0.0.0.0 --port 80
http://localhost:8000/
```
