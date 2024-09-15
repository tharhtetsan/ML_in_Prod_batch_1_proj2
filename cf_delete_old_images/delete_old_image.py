from google.cloud import artifactregistry_v1
from google.cloud.artifactregistry_v1.types import ListDockerImagesRequest
from google.oauth2 import service_account

def delete_old_images(request):
    # Set up Artifact Registry client
    client = artifactregistry_v1.ArtifactRegistryClient()

    # Your specific project, location, repository
    project_id = 'ml-in-prod-b1'
    location = 'us-central1'
    repository = 'cloud-run-source-deploy'
    image_path = 'gce-fastapi'

    # Full path to your repository in Artifact Registry
    parent = f"{project_id}-docker.pkg.dev/{project_id}/{repository}/{image_path}"


    # List all Docker images in the repository
    request = ListDockerImagesRequest(parent=parent)
    docker_images = client.list_docker_images(request=request)

    # Filter images for the specific path "gce-fastapi"
    images_list = [image for image in docker_images if image.name.endswith(f"/{image_path}")]

    # Check if any images were found
    if not images_list:
        print(f"No images found in the path: {image_path}")
        return f"No images found in the path: {image_path}"

    # Sort images by creation time in descending order (latest first)
    images_list.sort(key=lambda img: img.update_time, reverse=True)

    # Keep only the latest 10 images
    images_to_keep = images_list[:10]
    images_to_delete = images_list[10:]


    print("##############")
    print(images_list)

    # Delete images that are older than the latest 10
    for image in images_to_delete:
        print(f"Deleting image: {image.name}")
        client.delete_docker_image(name=image.name)

    return f"Deleted {len(images_to_delete)} images, kept {len(images_to_keep)} latest ones."
