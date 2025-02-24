import google.generativeai as genai

# Set up Gemini API Key (use environment variables instead of hardcoding)
API_KEY = "AIzaSyAltwKDLDCavSIWCzCiTMjx3gxX-jXxgcw"
genai.configure(api_key=API_KEY)

# Function to get response from Gemini API
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Example Usage
prompt = "A group of tourist is visiting tadoba forest in chandrapur. List 5 precautions that they should take while enjoying jungle safari. List them point wise like 1,2,3,4,5 in that way."
print(get_gemini_response(prompt))
