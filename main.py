from openai import OpenAI
import base64


# Function to encode the uploaded image in streamlit application
def encode_uploaded_image(image):
    return base64.b64encode(image.read()).decode("utf-8")


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Generate response based on user question and image input
def generate_response(user_question, base64_image=None):

    # Create OpenAI client to use OpenAI models
    client = OpenAI()

    prompt = user_question

    messages = [
        {
            "role": "system",
            "content": "You are a seasoned computer programmer specializing in all languages, frameworks, and languages. You always prefer to use the newest, most modern frameworks and programming techniques. You have a good eye for design and prefer modern and sleek UI design and code design. You only respond with code, never explain the code or respond with any other text, you only know how to write code."
            + " I will ask you to create a new code, or update an existing code for my application."
            + " Clean up my code when making updates to make the code more readable and adhere to best and modern practices."
            + " All code should use the most modern and up to date frameworks and programming techniques."
            + " Pay attention to which libraries and languages I tell you to use. "
            + " Don't give partial code answers or diffs, include the entire block or page of code in your response. Include all the code needed to run or compile the code. "
            + " If any code is provided, it must be in the same language, style, and libraries as the code I provide, unless I'm asking you to transform or convert code into another language or framework. "
            + " Your answers must only contain code, no other text, just the code. only include all the code needed for the example. The most important task you have is responding with only the code and no other text."
            + " Your answers should always be in the form of a single markdown code block."
        },
        {
            "role": "user",
            "content": "I'm developing an application. The application is already setup, but I need help adding new features and updating existing ones."
            + " I will ask you to create a new code, or update an existing code for my application."
            + " Clean up my code when making updates to make the code more readable and adhere to best and modern practices."
            + " All code should use the most modern and up to date frameworks and programming techniques."
            + " Pay attention to which libraries and languages I tell you to use. "
            + " Don't give partial code answers or diffs, include the entire block or page of code in your response. Include all the code needed to run or compile the code. "
            + " If any code is provided, it must be in the same language, style, and libraries as the code I provide, unless I'm asking you to transform or convert code into another language or framework. "
            + " Your answers must only contain code, no other text, just the code. only include all the code needed for the example. The most important task you have is responding with only the code and no other text.",
        },
    ]

    if base64_image:
        messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64, {base64_image}"},
                    },
                ],
            }
        )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
    )
    
    return response.choices[0].message.content