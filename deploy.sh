export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml card-gen-stack
docker service update --replicas 3 card-gen-stack_front-end