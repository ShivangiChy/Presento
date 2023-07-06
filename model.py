import openai
import json
import re
from scrape import extract_text_from_medium
import sys

openai.api_key = "YOUR API KEY"

prompt = '''you are a presentation maker. I will be giving you article text and you have to convert that into presentation, try to make it concise and crisp and also make it in point form and strictly follow the format that I will be giving you. The format of returning is json format 
FORMAT:
{
"presentationTitle": "title of presentation",
"slide": [{
"title": "Title of the slide goes here",
"points": ['all the points will go in this list.Write complete and descriptive sentences for each slide maximum 10-15 words long, explaining the concepts told in the text. Remember that content should be in points to enhance readability.'],
"imageDescription" : "suggest an image description that complements the written content and enhances the visual appeal of the slide, promoting audience understanding and engagement.You can write as 15-30 words long description."
},...]
}
In the response, return the json object of the above told format(Slides should be strictly more that 5, but u can write as many required according to the given text). Do not skip any part of the format. If you are not able to generate the answer, return the json object with None object.
'''

def api_call(text, prompt):
    completion = openai.ChatCompletion.create(
    model ="gpt-3.5-turbo",
    temperature = 0.8,
    max_tokens = 2000,
    messages = [
    {"role": "system", "content":prompt},
    {"role": "user", "content": text}
    ]
    )

    response = completion.choices[0].message
    return response

def get_content(url):
    extracted_text = extract_text_from_medium(url)
    return extracted_text


if __name__ == "__main__":
    # url = "https://medium.com/@ibrahimzahir7/12-websites-youll-love-as-a-developer-1e4180d0a729"
    # url = "https://medium.com/@riteshgupta.ai/10-most-common-machine-learning-algorithms-explained-2023-d7cfe41c2616"
    # url = "https://medium.com/python-in-plain-english/top-8-algorithms-every-programmer-should-know-93c826267938"
    # url = "https://medium.com/codingthesmartway-com-blog/docker-beginners-guide-part-1-images-containers-6f3507fffc98"
    # url = "https://medium.com/@chenyumei8866/10-killer-python-automation-scripts-f305d7261d55"
    # url = "https://medium.com/@naemazam/best-computer-vision-projects-with-source-code-and-dataset-6af1aa457df7"
    # url = "https://medium.com/@reachpriyaa/how-to-crack-machine-learning-interviews-at-faang-78a2882a05c5"
    # url = "https://medium.com/towards-data-science/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53"
    url = "https://medium.com/@normponte/short-intro-to-gans-9359c888b806"
    text = get_content(url)
    # with open("summaries.txt", "a") as f:
    #     print(content, file=f)
    #     print('exit', file=f)
    print(text)
    response = api_call(text, prompt)
    responseOutput = response.content
    # print("\n")
    print(responseOutput)
    

    # Check if the output file name is provided as a command-line argument
    # if len(sys.argv) > 1:
    #     output_file = sys.argv[1]
    # else:
    #     # Default output file name if not provided
    #     output_file = "output.txt"

    # Use the output_file variable in your script for future operations
    # For example:
    # with open(output_file, "w") as file:
    #     file.write("This is the output file.")

    # You can use the output_file variable wherever you need to refer to the output file name
    # print("Output file name:", output_file)
    # responseOutput = re.sub("\\n", "", responseOutput)
    # print("\n")
    # print(responseOutput)
    # jsonOutput = json.loads(responseOutput)
    # print(jsonOutput)
    # print(json.dumps(responseOutput, indent=4))
    