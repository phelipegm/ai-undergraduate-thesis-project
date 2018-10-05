from nltk.tokenize import word_tokenize
from collections import Counter #Object
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

text = "The cat is in the box. The cat likes the box. The box is over the cat."
counter = Counter(word_tokenize(text))
print(counter)
print(counter.most_common(2))

article = """IBM announced last week it has moved its cognitive computing system into the cloud to form the Watson Discovery Advisor, allowing researchers, academics and anyone else trying to leverage big data the ability to test programs and hypotheses at speeds never before seen.

Since Watson is built to understand the nuance of natural language, this new service allows researchers to process millions of data points normally impossible for humans to handle. This can reduce project timelines from years to weeks or days.

“We’re entering an extraordinary age of data-driven discovery,” said Mike Rhodin, senior vice president for IBM Watson Group, in a release. “[This] announcement is a natural extension of Watson’s cognitive computing capability. We’re empowering researchers with a powerful tool which will help increase the impact of investments organizations make in R&D, leading to significant breakthroughs.”

https://www.youtube.com/watch?v=qry_zGZFjOc

IBM has been honing Watson’s capabilities over the last three years, reducing its size and upping its power since its famous appearance on “Jeopardy!” in 2011. The Watson of today is drastically different, operating at 24 times its power from Jeopardy while shrinking 90 times smaller. Earlier this year, IBM invested $1 billion into the project to form the Watson Group, with $100 million going to entrepreneurs and companies to build applications to run on Waston.

“I think there have been a number of ways that we have improved the system since Jeopardy,” said John Gordon, vice president of IBM Watson Systems. “What you saw on Jeopardy was a system that could provide answers to questions. While the range of topics was very broad, there was always a relatively succinct question and succinct answer. In the phase after Jeopardy, through the beginning of this year, we were validating that we could extend the technology from doing a broad set of fairly straightforward questions to do some real important commercial cases. Based on the results with that, we validated this was very possible.”

A few ongoing research projects are already leveraging Watson’s new capabilities. A peer-reviewed study released last week by the Baylor College of Medicine identified a protein that modifies another protein related to many cancers, giving doctors a chance to fine-tune drug efficacy or create new treatments. The study was completed in part due to Watson’s ability to process 70,000 scientific articles about the protein, a feat that researchers could only dream to accomplish. According to the National Institutes of Health, a typical researcher only has time to read about 300 studies per year.

“Even if I’m reading five papers a day, it could take me 38 years to completely understand all of the research already available today on this protein,” said Dr. Olivier Lichtarge, the principal investigator and professor at Baylor College of Medicine. “Watson has demonstrated the potential to accelerate the rate and the quality of breakthrough discoveries.”

The Watson Discovery Advisor team has also been used in research projects for Johnson & Johnson, Sanofi and New York’s Genome center, processing millions of scientific papers in order to shave months off completion dates.

IBM believes in Watson’s capabilities beyond medical laboratories, finding applicable use cases in everything from finance to law to restaurant kitchens. Gordon, who formerly worked on IBM’s Smarter Cities project, believes Watson can help close a digital divide that will allow governments to better serve their constituents.

“Part of Smarter Cities was working with different municipalities and governments to determine how technology could help them provide better services to their constituents,” Gordon said. “One of the things that became apparent to me was the digital divide between those who were able to use technology and those who were not. Watson, to me, represented the beginnings of computing systems that didn’t require people to conform to technology. So I really thought of Watson as propelling more people into the information economy across all of the ways we help citizens. I think Watson will bridge that digital divide.”

With a combination of power never before released at a scale that is now widely accessible, Gordon believes Watson serves as a tipping point for cognitive computing.

“We are at the absolute beginning of this cognitive era of computing,” Gordon said. “I expect it to go on for the next 50 years. This could be more transformative than when we saw the Internet come forward and drive connectivity. Systems that can learn, systems that we can teach and that can help us not only understand the information around us, but inspire us to be more creative and drive innovation. I think we are just at the very beginning of this, but with our ecosystem and opening it up to the entrepreneurial base, I’m sure the ingenuity of all the people that are going to have the ability to integrate with Watson will build up solutions we’ve never even considered before.”"""

# Tokenize the article: tokens
tokens = word_tokenize(article)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

# Text comprehension
# isalpha() => only return alphabetic strings
tokens = [w for w in word_tokenize(text.lower()) if w.isalpha()]
print(text)
print(tokens)

no_stops = [t for t in tokens if t not in stopwords.words('english')]
print(no_stops)

print(Counter(no_stops).most_common(2))

lower_tokens = word_tokenize(article)

# Retain alphabetic words: alpha_only
alpha_only = [w for w in lower_tokens if w.isalpha()]
print(alpha_only)
# Remove all stop words: no_stops
no_stops2 = [w for w in alpha_only if w not in stopwords.words('english')]
print(no_stops2)

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops2]
print(lemmatized)

# Create the bag-of-words: bow
bow = Counter(lemmatized)
print(bow)

