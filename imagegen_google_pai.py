import google.generativeai as genai
import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# --- CONFIGURATION ---
# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
model_to_use = os.getenv("GEMINI_MODEL")

# Set your API key from an environment variable (recommended)
# genai.configure(api_key=api_key)

# Or, if you need to hardcode for a quick test (not recommended for production)
genai.configure(api_key=api_key) # Replace YOUR_API_KEY with your actual API key

try:
    # Select the model for image generation
    # Note: Model names and availability can change, refer to Google AI documentation.
    model = genai.GenerativeModel('gemini-2.0-flash-preview-image-generation')

    # Generate content with an image prompt
    response = model.generate_content(
        "Generate a vibrant image of a futuristic city at sunset with flying cars and tall, glowing skyscrapers."
    )

    generated_images = []
    generated_text = []

    # Check if any content candidates were returned
    if response._candidate_count > 0:
        for candidate in response.candidates:
            if candidate.content and candidate.content.parts:
                for part in candidate.content.parts:
                    # Check if the part is an image (BlobPart)
                    if hasattr(part, 'blob') and part.blob and part.blob.mime_type.startswith('image/'):
                        generated_images.append(part.blob.data)  # Get the raw image bytes
                        print(f"Found an image part in the response (MIME type: {part.blob.mime_type}).")
                    # Check if the part is text (TextPart)
                    elif hasattr(part, 'text') and part.text:
                        generated_text.append(part.text)
                        print(f"Found a text part in the response: {part.text}")
                    else:
                        print(f"Found an unhandled part type in response: {type(part)}")
            else:
                print("Candidate has no content or parts.")
    else:
        print("No candidates returned in the response.")
        # If no candidates, there might be prompt feedback indicating why.
        if response.prompt_feedback:
            print(f"Prompt feedback: {response.prompt_feedback.block_reason}")
        print(f"Full response object for debugging: {response}")

    # Process and save generated images
    if generated_images:
        for i, image_bytes in enumerate(generated_images):
            try:
                image = Image.open(BytesIO(image_bytes))
                image.save(f"generated_image_gemini_{i}.png")
                print(f"Saved generated_image_gemini_{i}.png successfully.")
            except Exception as e_save:
                print(f"Error saving image {i}: {e_save}")
    else:
        print("No images were found in the response. The model might not have generated an image or the prompt was misunderstood.")

    # Print any generated text
    if generated_text:
        print("\n--- Generated Text Content ---")
        for text in generated_text:
            print(text)
    else:
        print("No text content was generated.")

except genai.types.BlockedPromptException as e:
    print(f"The prompt was blocked due to safety reasons: {e.response.prompt_feedback.block_reason}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
        
except Exception as e:
    print(f"An error occurred: {e}")