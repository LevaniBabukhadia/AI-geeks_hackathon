import webbrowser
import os

# Specify the path to your HTML file

file_path={"safe":'/home/levani/Desktop/safe.html', "maybe hazardous":'/home/levani/Desktop/maybe hazardous.html', "not safe":'/home/levani/Desktop/not safe.html'}

# Ensure the file path is absolute
absolute_path = os.path.abspath(file_path["not safe"])

# Open the HTML file in the default web browser
#webbrowser.open('file://' + absolute_path)


knowledge_base=["www.bankofgeorgia.ge","www.facebook.com","www.gpost.ge","www.google.com"] #knowledge base should be expanded
permutations=[] #of websites from knowledge base
def generate_substitutions(s, index=0, current=''):
    # Character mappings for substitutions
    substitutions = {
        'o': ['o', '0'],
        '0': ['0', 'o'],
        'l': ['l', 'i'],
        'i': ['i', 'l']
    }

    # Base case: if we've processed all characters, return the current string
    if index == len(s):
        return [current]

    # Current character
    char = s[index]

    # Generate substitutions for the current character
    if char in substitutions:
        results = []
        for substitute in substitutions[char]:
            results.extend(generate_substitutions(s, index + 1, current + substitute))
        return results
    else:
        return generate_substitutions(s, index + 1, current + char)


# Input string
for e in knowledge_base:

    input_string = e

    # Generate all possible strings by changing 'o' to '0' and 'l' to 'i' and vice versa
    all_substitutions = generate_substitutions(input_string)

    # Remove duplicates by converting the list to a set and back to a list
    unique_substitutions = list(set(all_substitutions))

    # Print all unique substitutions
    for substitution in unique_substitutions:
        permutations.append(substitution)

#we get possible permutations

url=input("enter url: ") #url should be


from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Initialize the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the isolated string and the array of strings
isolated_string = url
array_of_strings = permutations

# Generate embedding for the isolated string
isolated_embedding = model.encode(isolated_string, convert_to_tensor=True)

# Generate embeddings for the array of strings
array_embeddings = model.encode(array_of_strings, convert_to_tensor=True)

# Compute similarity scores
similarity_scores = util.pytorch_cos_sim(isolated_embedding, array_embeddings)

# Convert the similarity scores to a numpy array and flatten it
similarity_scores = similarity_scores.numpy().flatten()

# Create a DataFrame to display the similarity scores
similarity_df = pd.DataFrame({'String': array_of_strings, 'Similarity': similarity_scores})

# Print the similarity scores
#print(similarity_df)

print(similarity_scores)
print(type(similarity_scores))
similarity_scores=list(similarity_scores)
print(type(similarity_scores))


def decide():
    for e in similarity_scores:
        if e > 0.9:
            # Ensure the file path is absolute
            absolute_path = os.path.abspath(file_path["not safe"])

            # Open the HTML file in the default web browser
            return webbrowser.open('file://' + absolute_path)
        if  0.5<e and e <0.9:
            # Ensure the file path is absolute
            absolute_path = os.path.abspath(file_path["maybe hazardous"])

            # Open the HTML file in the default web browser
            return webbrowser.open('file://' + absolute_path)

    absolute_path = os.path.abspath(file_path["safe"])
    return webbrowser.open('file://' + absolute_path)


print(decide())

