import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def extract_keywords(job_description, reference_keywords=None):
    # Convert the job description to lowercase
    job_description = job_description.lower()

    # Tokenize the job description
    words = word_tokenize(job_description)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if not word in stop_words]

    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Get the frequency distribution of the words
    freq_dist = nltk.FreqDist(words)

    # Get the most common words (excluding stop words and words with less than 3 characters)
    keywords = [word for word, freq in freq_dist.most_common() if not word in stop_words and len(word) > 2][:10]

    # Add reference keywords to the list
    if reference_keywords:
        keywords += reference_keywords

    # Remove duplicates
    keywords = list(set(keywords))

    return keywords

# Example usage
job_description = "We are looking for a software engineer with experience in Python, Java, and SQL. The ideal candidate should have a degree in Computer Science and at least 3 years of experience in software development."
reference_keywords = ["software", "engineer", "python", "java", "sql", "computer science", "experience", "development", "with"]
keywords = extract_keywords(job_description, reference_keywords)
print(keywords)
