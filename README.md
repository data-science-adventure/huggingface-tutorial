# Full pipeline for Text Data Exploration


## Pre-requisities
- [Python](https://www.python.org/downloads/) is installed
- [Virtual enviroment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for python is installed


## Prepare environment

### Create virtual environment

```shell
python3 -m venv .venv
```

### Activate virtual environment:

```shell
source .venv/bin/activate
```
### Create requirements.txt file (optional)

If you are the maintainer of the project and you have to add new libraries, then you must follow the next steps in order to create the `requirements.txt` file

1. Install pip-tools with the command `pip install pip-tools`
2. Add, update or delete a dependency in the file `requirements.in`
3. Create the file requirements.txt with the command `pip-compile requirements.in`

### Install all the dependencies

In order to install all the project dependencies you must execute the next commands:

```shell
pip install -r requirements.txt
```

## Pipeline description

The proposed pipeline  has 8 steps:

1. Data Loading and Initial Inspection
2. Basic Text Statistics
3. Text Preprocessing (for Exploration)
4. Vocabulary Analysis
5. Part-of-Speech (POS) Tagging
6. Named Entity Recognition (NER)
7. Sentiment Analysis (if applicable)
8. Topic Modeling (High-level exploration)

The dataset used for this tutorial can be downloaded from [Product reviews from Amazon](https://zenodo.org/records/10157504)

## 1. Data Loading and Initial Inspection

**Common Task**: Load your text data and get a first glance at its structure and content.

**Tips**:
- Start with a sample if your dataset is massive.
- Understand the format: Is it a CSV, JSON, database, etc.?
- Check for missing values immediately.

# 2. Basic Text Statistics

**Common Tasks**: Calculate fundamental statistics about your text data to understand its overall characteristics.

**Tips**:
- Character count can indicate brevity or verbosity.
- Word count and sentence count provide insights into text length and complexity.
- Average word length can hint at the formality or simplicity of the language.


## 3. Text Preprocessing (for Exploration)

**Common Tasks**: Clean and normalize text to prepare it for frequency analysis and other exploratory tasks. This is a lighter preprocessing step compared to what you might do for modeling.

**Tips**:
- Lowercasing prevents treating "The" and "the" as different words.
- Punctuation removal reduces noise.
- Stopword removal focuses on meaningful content words.
- Stemming/Lemmatization reduces words to their root forms, consolidating variations.

## 4. Vocabulary Analysis

**Common Tasks**: Understand the unique words, their frequencies, and patterns.

**Tips**:

- Word clouds provide a quick visual summary of frequent terms.
- Bar charts of top N words show exact frequencies.
- Analyzing n-grams (bigrams, trigrams) reveals common phrases.

## 5. Part-of-Speech (POS) Tagging

**Common Task**: Analyze the distribution of grammatical categories (nouns, verbs, adjectives, etc.) in your text.

**Tips**:

- Provides insights into the linguistic structure of your corpus.
- Can highlight if your text is descriptive (many adjectives), action-oriented (many verbs), or topic-focused (many nouns).


## 6. Named Entity Recognition (NER)

**Common Task**: Identify and categorize named entities (people, organizations, locations, dates, etc.) in your text.

**Tips**:

- Reveals key subjects and concepts in your data.
- Useful for extracting structured information from unstructured text.


## 7. Sentiment Analysis (if applicable)

**Common Task**: Determine the emotional tone (positive, negative, neutral) of your text data.

**Tips**:

- Provides a high-level understanding of the sentiment distribution.
- Can be done with simple lexicon-based models or more complex pre-trained models.

## 8. Topic Modeling (High-level exploration)

**Common Task**: Discover abstract "topics" that occur in a collection of documents.

**Tips**:

- LDA (Latent Dirichlet Allocation) is a common algorithm.
- Requires a document-term matrix.
- Provides a sense of the main themes present in your corpus.


## Conclusion of Data Exploration Phase

This comprehensive pipeline covers the essential aspects of text data exploration. By following these steps, you'll gain a deep understanding of your text data's characteristics, common themes, linguistic patterns, and potential challenges, which will guide your subsequent NLP modeling efforts. Remember that data exploration is an iterative process, and you might revisit earlier steps as new insights emerge.

