import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires verification.
CLIENT_SECRETS_FILE = "client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    """
    Authenticates the user and returns a YouTube API service object.
    """
    credentials = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(credentials, token)
            
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def upload_video(youtube, file_path, title, description, category_id, tags, privacy_status):
    """
    Uploads a video to YouTube.

    Args:
        youtube: The authenticated YouTube API service object.
        file_path (str): The path to the video file.
        title (str): The video's title.
        description (str): The video's description.
        category_id (str): The video's category ID.
        tags (list of str): A list of tags for the video.
        privacy_status (str): The video's privacy status ('public', 'private', or 'unlisted').
    """
    if not os.path.exists(file_path):
        print(f"Error: Video file not found at '{file_path}'")
        return

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': privacy_status
        }
    }

    try:
        # Create a MediaFileUpload object for the video file.
        # This object handles chunked uploads, which is necessary for large files.
        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

        # Call the API's videos.insert method to create and upload the video.
        print("Uploading video...")
        request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=media
        )

        # Execute the request and print upload progress.
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%")
        
        print(f"Video uploaded successfully! Video ID: {response['id']}")
        print(f"Watch your video at: https://www.youtube.com/watch?v={response['id']}")

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")


if __name__ == '__main__':
    # --- CONFIGURATION ---
    # Replace with the actual path to your video file
    VIDEO_FILE_PATH = "my_video.mp4" 
    
    # Video details
    video_title = "My Awesome Python-Uploaded Video"
    video_description = "This video was uploaded automatically using a Python script and the YouTube Data API v3."
    video_tags = ["youtube api", "automation" , "aistories"]
    
    # Numeric video category. See an updated list here:
    # https://developers.google.com/youtube/v3/docs/videoCategories/list
    # For example: 22=People & Blogs, 27=Education, 28=Science & Technology
    video_category_id = "28" 
    
    # 'public', 'private', or 'unlisted'
    video_privacy_status = "private" 
    # -------------------
    
    # Authenticate and get the service object
    youtube_service = get_authenticated_service()
    
    # Call the upload function
    upload_video(
        youtube=youtube_service,
        file_path=VIDEO_FILE_PATH,
        title=video_title,
        description=video_description,
        category_id=video_category_id,
        tags=video_tags,
        privacy_status=video_privacy_status
    )