# taggelator

1. Building the environment image
```bash
docker build -t taggelator_env .
```

2. Running the container
```bash
docker run --name taggelator -v /:/src -dt taggelator_env
```

3. Go to the container for data exploration
```bash
docker exec -it taggelator bash
```
