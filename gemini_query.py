import os
import asyncio
import google.generativeai as genai
from googletrans import Translator, LANGUAGES
from dotenv import load_dotenv

# --- CONFIGURATION ---
# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

# Configure the Gemini API with your key
try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    exit()

# --- HELPER FUNCTIONS ---

def query_gemini(prompt: str) -> str | None:
    """
    Sends a prompt to the Gemini Pro model and returns the response.
    Args:
        prompt: The question or instruction for the model.
    Returns:
        The text response from Gemini, or None if an error occurred.
    """
    print("1. Querying Gemini gemini-2.5-flash...")
    try:
        # Using the 'gemini-2.5-flash' model
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while querying Gemini: {e}")
        return None

def translate_text(text: str, target_language: str) -> str | None:
    """
    Translates text to a specified target language.
    Args:
        text: The text to translate.
        target_language: The language code to translate to (e.g., 'es', 'fr').
    Returns:
        The translated text, or None if an error occurred.
    """
    if target_language not in LANGUAGES:
        print(f"Error: Invalid target language code '{target_language}'.")
        print(f"See available codes here: https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")
        return None
        
    print(f"2. Translating text to '{LANGUAGES.get(target_language, 'Unknown').title()}' ({target_language})...")
    try:
        translator = Translator()
        translated = translator.translate(text, src='auto', dest=target_language)
        return translated.text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return None

def save_to_file(filename: str, content: str):
    """
    Saves content to a text file, ensuring UTF-8 encoding.
    Args:
        filename: The name of the file to save.
        content: The text content to write to the file.
    """
    print(f"3. Saving translated content to '{filename}'...")
    try:
        # 'utf-8' encoding is crucial for handling special characters in different languages
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print("   File saved successfully.")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # --- STEP 1: DEFINE YOUR INPUTS ---
    # Your question for the Gemini API
    user_prompt = "Give me 1500 words simple inspring story in simple plain english about poor man become rich with single line conclusion"

    # The language you want to translate the response into.
    # Common codes: 'es' (Spanish), 'fr' (French), 'de' (German), 'ja' (Japanese), 
    # 'hi' (Hindi), 'zh-cn' (Chinese Simplified)
    target_lang_code = 'hi' 

    # The name of the output file
    output_filename = f"gemini_response_{target_lang_code}.txt"
    gemini_response_filename = f"gemini_response_{target_lang_code}_gemini_response.txt"
    
    print("-" * 50)
    print(f"PROMPT: {user_prompt}")
    print(f"TARGET LANGUAGE: {target_lang_code}")
    print("-" * 50)

    API_MODLES_GEMMA = ["gemma-3n-e4b-it"]  
    # --- STEP 2: GET RESPONSE FROM GEMINI ---
    #gemini_response = query_gemini(user_prompt)
    with open(gemini_response_filename, "r") as res:
       gemini_response = res.read() 
    if gemini_response:
        print("\n--- Gemini's Original Response (English) ---")
        print(gemini_response)
        print("-" * 50)
        #save_to_file(gemini_response_filename, gemini_response)
        
        # --- STEP 3: TRANSLATE THE RESPONSE ---
        translated_response = translate_text(gemini_response, target_lang_code)

        if translated_response:
            print(f"\n--- Translated Response ({target_lang_code}) ---")
            print(translated_response)
            print("-" * 50)

            # --- STEP 4: SAVE THE TRANSLATED RESPONSE TO A FILE ---
            save_to_file(output_filename, translated_response)
    
    print("\nProcess finished.")