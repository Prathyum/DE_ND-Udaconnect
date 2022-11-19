kubectl delete deployment connection-api
kubectl delete deployment location-api
kubectl delete deployment person-api
kubectl delete deployment location-consumer
kubectl delete deployment location-producer
kubectl delete deployment postgres
kubectl delete deployment udaconnect-app

helm delete udaconnect #for kafka helm chart