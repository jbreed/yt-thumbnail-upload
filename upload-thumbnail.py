#!/usr/bin/env python3
# Author:       jbreed
# Repo:         https://github.com/jbreed/yt-thumbnail-upload
# Purpose:      Upload YouTube thumbnail
# Note:         Place image in this directory and run script from there assuming you already have everything setup
#
# Prompts:      VideoID (IE: https://www.youtube.com/shorts/tb-1-Wi-ewA the Video ID is tb-1-Wi-ewA)
#               Image name: (IE: myimage.jpg)
import os
from PIL import Image
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


# Recommended size: 1280x720
def verify_image(image_path):
    """ Verify the image meets YouTube's thumbnail requirements for Shorts """
    with Image.open(image_path) as img:
        # Check image dimensions for 720x1280 resolution
        if img.size != (1280, 720):
            raise ValueError("Image dimensions are incorrect. Required size is 1280x720 pixels.")

        # Ensure aspect ratio is 16:9
        aspect_ratio = img.size[0] / img.size[1]
        required_aspect_ratio = 16 / 9
        if aspect_ratio != required_aspect_ratio:
            raise ValueError(f"Incorrect aspect ratio. Required aspect ratio is 16:9. Found {aspect_ratio:.2f}:1")

        # Check file size to be under 2MB
        if os.path.getsize(image_path) > 2 * 1024 * 1024:
            raise ValueError("File size must be under 2MB.")

        # Check file type
        if img.format not in ["JPEG", "PNG"]:
            raise ValueError("Invalid file type. Only JPEG, PNG, BMP, and GIF are allowed.")


def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    # User input for video ID and image filename
    video_id = input("Enter the YouTube video ID: ")
    image_filename = input("Enter the thumbnail image filename (e.g. thumbnail.jpg): ")

    image_path = os.path.join(os.getcwd(), image_filename)

    # Verify the image before uploading
    verify_image(image_path)

    # Call the API to set the thumbnail
    request = youtube.thumbnails().set(
        videoId=video_id,
        media_body=googleapiclient.http.MediaFileUpload(image_path)
    )
    response = request.execute()

    print("Thumbnail updated successfully.")
    print(response)


if __name__ == "__main__":
    main()
