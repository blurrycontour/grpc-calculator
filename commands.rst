zone=us-central1-c
cluster=slim-cluster

gcloud container clusters resize $cluster --zone=$zone --node-pool=default-pool --num-nodes=0
gcloud container clusters resize $cluster --zone=$zone --node-pool=small-pool --num-nodes=0
