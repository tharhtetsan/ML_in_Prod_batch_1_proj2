# ML_in_Prod_batch_1_proj2


### Sample gcloud commands
```bash
gcloud compute instance-templates list 

gcloud compute instance-templates create-with-container instance-gp-tp-prod-123 --custom-cpu=2 --custom-memory=8GB --boot-disk-size=20GB --region=asia-east --container-image $_AR_HOSTNAME/$_PROJECT_ID/cloud-run-source-deploy/gce-fastapi:prod




gcloud compute instance-groups managed rolling-action start-update instance-group-prod --version=template=instance-gp-tp-prod-48c00c9 --zone=asia-east1-b
```