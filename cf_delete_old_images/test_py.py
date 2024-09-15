from google.cloud import artifactregistry_v1
from google.cloud.artifactregistry_v1.types import ListDockerImagesRequest
from google.oauth2 import service_account


client = artifactregistry_v1.ArtifactRegistryClient()

# Your specific project, location, repository
project_id = 'ml-in-prod-b1'
location = 'us-central1'
repository = 'cloud-run-source-deploy'
image_path = 'gce-fastapi'

# Full path to your repository in Artifact Registry
parent = f"projects/{project_id}/locations/{location}/repositories/{repository}"

# List all Docker images in the repository
request = ListDockerImagesRequest(parent=parent)
docker_images = client.list_docker_images(request=request)

# Filter images for the specific path "gce-fastapi"
images_list = [image for image in docker_images if image.name.endswith(f"/{image_path}")]
