from gtts import gTTS
import os
from dotenv import load_dotenv

# --- CONFIGURATION ---
# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

YOUR_GOOGLE_CLOUD_PROJECT_ID = os.getenv("YOUR_GOOGLE_CLOUD_PROJECT_ID")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_secrets.json"


# --- Example Usage for Google Cloud Text-to-Speech ---
if __name__ == "__main__":
    print("\n--- Using Google Cloud Text-to-Speech API (gTTS) ---")
    
    # Text you want to convert to speech
    gemini_response_filename = f"gemini_response_hi_gemini_response.txt"
    gemini_response_filename_hi = "gemini_response_hi.txt"
    with open(gemini_response_filename_hi, "r", encoding='utf-8') as res:
        gemini_response = res.read()

    # Language in which you want to convert (e.g., 'en' for English, 'fr' for French)
    language = 'hi'

    # Create a gTTS object
    print("You can also set slow=True for slower speech [5]")
    tts = gTTS(text=gemini_response, lang=language, slow=False)

    print("Save the converted audio to a file")
    output_filename = f"gemini_response_{language}.mp3"
    tts.save(output_filename)
    print(f"Audio file saved as {output_filename}.")