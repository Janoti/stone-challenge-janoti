local:
	eval $(minikube docker-env)
	docker build ./ -t challenge-janoti
	docker run -p 5000:5000 challenge-janoti

k8s:
	eval $(minikube docker-env)
	kubectl apply -f deployment.yaml

stop:
	docker-compose stop
