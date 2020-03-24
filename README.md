# taggelator

** Building the image
docker build -t taggelator_env .

** Running the container:
docker run --name taggelator -v /:/src -dt taggelator_env

** Go to the container for data exploration
docker exec -it taggelator bash