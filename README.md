# three-tier-docker-app
# steps to run all tier

1) clone the repo 
2) download and install the docker based on your operating system.
3) download visual studio 
4) install docker extension in the vs code
5) open terminal in vs code
6) type command docker compose up --build 
7) click on localhost 3000 
8) docker compose down (to halt)

** docker compose up --build **

** docker compose down **

| Command                          | What it does                   |
| -------------------------------- | ------------------------------ |
| `docker compose down`            | Stop and remove all containers |
| `docker compose logs -f`         | View logs from all services    |
| `docker compose ps`              | Show running containers        |
| `docker compose stop backend`    | Stop only the backend service  |
| `docker compose restart backend` | Restart backend only           |

