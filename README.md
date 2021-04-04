# Iniciar o docker de dev

docker run --rm -it --name caverna-web -v $(pwd):/caverna  -p 8080:8080 caverna:alfa

# Entrar no docker 

docker container exec -it caverna-web /bin/sh

# Deploy do site

make github