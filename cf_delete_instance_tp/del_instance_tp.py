import functions_framework
from googleapiclient import discovery
from google.oauth2 import service_account

# Initialize the Google Compute Engine API client
credentials = service_account.Credentials.from_service_account_file('service-account.json')
compute = discovery.build('compute', 'v1', credentials=credentials)


PROJECT = "ml-in-prod-b1"
ZONE = "asia-east1-b"
INSTANCE_GROUP_NAME = "instance-group-prod"
prefix = "instance-gp-tp-prod"

@functions_framework.http
def delete_unused_instance_templates(request):
  
    instance_group = compute.instanceGroupManagers().get(
        project = PROJECT,
        zone = ZONE,
        instanceGroupManager = INSTANCE_GROUP_NAME).execute()
    
    # Get the currently used instance template
    used_template = instance_group['instanceTemplate']


    templates = compute.instanceTemplates().list(project=PROJECT).execute()

    for template in templates.get('items',[]):
        if template["selfLink"] != used_template:
            # filter the only related unused images
            if prefix in  template["name"] :
                print(f"Deleting unused template : {template['name']}")
                compute.instanceTemplates().delete(project=PROJECT, instanceTemplate=template['name']).execute()


    return "Unused instance templates deleted...."




