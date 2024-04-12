# yt-thumbnail-upload

Simple script leveraging Google's YouTube v3 API to update a YouTube thumbnail (including YouTube shorts). After publishing YouTube shorts and later realizing how horrible my thumbnails are, I need a mechanism to update these since the YouTube Studio and YouTube sites/apps had no option to update this. I have found this to be a quick solution to update thumbnails for YouTube Shorts.

<br><br>

# Setup

1. Setup Google Cloud Account and Enable the API for Youtube Data API v3 (https://console.cloud.google.com/)
  - Create new project
  - APIs & Services > Dashboard > enable YouTube Data API v3
  - Create credentials (External/public, desktop app, then download/export the JSON file)
  - Options: external/public, desktop app, dont need domains, need your youtube email added as a tester, need the scope added for https://www.googleapis.com/auth/youtube.force-ssl as this gives the access needed to your channel when it authenticates to your API client
  - Copy, or move, this json file to where the script lives and make sure it is named 'client.json'
  - Add your account you use for YouTube as a test account (IE: your email)
2. Install Python 3.10+ if not already installed on your system
3. Use pip (pip3) to install dependencies noted in the requirements.txt file

<br><br>

# Usage
1. Create your new image thumbnail in any editing software. 
   - Canvas/image size should be: 1280:720 pixels. (as well as for shorts, but only the center of this will use used for shorts on small devices). This image also needs to be under 2M for the file size. If your file is large, try saving it as a JPG to compress it.
   - Get the Video ID for the YouTube video you plan on updating the thumbnail on
   - Place the image in the same directory as the script
   - From terminal, or cmd, navigate to the directory in which the script resides
   - Run it (python3 upload-thumbnail.py)
   - Browser should open and you need to login to the YouTube account that controls that youtube channel. The prompts should give whatever information of your project you create in the google cloud console. If not published and logging in using your email you added as a test user, read carefully the buttons to make sure to continue and properly login.
   - After login, the script will move to a user prompt asking what the video ID is. If you open the video in a browser window, the URL will look something like the follow: https://www.youtube.com/shorts/tb-1-Wi-ewA, in which the Video ID is tb-1-Wi-ewA
   - Next prompt is the filename of the image you want to upload as the thumbnail. Type in the filename (IE: myimage.jpg)
