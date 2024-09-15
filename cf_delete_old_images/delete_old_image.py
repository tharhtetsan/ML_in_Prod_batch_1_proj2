from google.cloud import artifactregistry_v1
from google.cloud.artifactregistry_v1.types import ListDockerImagesRequest
from google.oauth2 import service_account

def delete_old_images(request):
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
    print("docker_images : ",(docker_images))

    # Filter images for the specific path "gce-fastapi"
    images_list =[]
    for cur_image in docker_images:
        related_image_name = parent+f"/dockerImages/{image_path}"
        if related_image_name in cur_image.name:
            #print(cur_image.name) 
            images_list.append(cur_image)

    if not images_list:
        print(f"No images found for the image: {image_name_prefix}")
        return f"No images found for the image: {image_name_prefix}"

    # Sort images by update time (latest first)
    images_list.sort(key=lambda img: img.update_time, reverse=True)

    # Keep only the latest 10 images
    images_to_keep = images_list[:5]
    images_to_delete = images_list[5:]

    # Delete images that are older than the latest 10
    for image in images_to_delete:
        print(f"Deleting image: {image.name}")
      
    return f"Deleted {len(images_to_delete)} images, kept {len(images_to_keep)} latest ones."
