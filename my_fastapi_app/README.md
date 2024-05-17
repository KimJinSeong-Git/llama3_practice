## Getting Started
### Prerequisites
- Docker

### Build
```
docker build -t jsbyeo/ais-paper-factory .
```

### Run
```
docker run -d -p 8000:8000 jsbyeo/ais-paper-factory
```

### Accessing the Application
```
http://0.0.0.0:8000
```

### Stopping the Docker Container
```
docker ps
```
```
docker stop <container_id>
```