# Import the OS module to handle file operations like opening files
import os

# Import necessary modules from the Sumy library for text summarization
from sumy.parsers.plaintext import PlaintextParser      # Parses plain text into a format sumy can use
from sumy.nlp.tokenizers import Tokenizer               # Tokenizes the input text into sentences/words
from sumy.summarizers.lsa import LsaSummarizer          # Uses Latent Semantic Analysis (LSA) to summarize text

# Function to summarize input raw text using the LSA summarizer
def do_summary(raw_text):
    try:
        # Parse the input text using Sumy’s parser and tokenizer
        parser = PlaintextParser.from_string(raw_text, Tokenizer("english"))
        
        # Create an instance of the LSA summarizer
        summarizer = LsaSummarizer()
        
        # Generate a summary consisting of the top 2 sentences
        summary = summarizer(parser.document, 2)
        
        # Return the summary as a single string
        return " ".join(str(sentence) for sentence in summary)
    
    except:
        # If summarization fails, print an error message and return the original text
        print("Summary failed, just returning original text")
        return raw_text

# Function to save output text to a file and open it automatically
def save_output(text, filename="output.txt"):
    # Write the given text to a file with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    try:
        # Try to open the file using the default system application (Windows only)
        os.startfile(filename)
    except:
        # If opening fails (e.g., on Linux/Mac), silently ignore
        pass
