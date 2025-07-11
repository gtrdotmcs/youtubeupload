import os
from google.cloud import texttospeech

# Set the path to your service account key file
# Replace 'path_to_your_service_account_key.json' with the actual path to your downloaded JSON key file.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_secrets.json"

def synthesize_text_to_speech(text, output_filename):
    """Synthesizes speech from the input text and saves it to an audio file."""
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Select the type of voice (e.g., 'en-US' for US English)
    # You can specify ssml_gender (MALE, FEMALE, NEUTRAL) and a specific voice name [1, 8]
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want to generate (e.g., MP3) [1, 2]
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write the response audio content to a file
    with open(output_filename, "wb") as out_file:
        out_file.write(response.audio_content)
        print(f"Audio content written to file '{output_filename}'")

# Example usage:
text_for_cloud_tts = "This is a demonstration of Google Cloud Text-to-Speech API."
synthesize_text_to_speech(text_for_cloud_tts, "cloud_output.mp3")