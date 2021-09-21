## General python
- GIL
- Collections
- pytest/nose
- decorators
- values by ref

## General NLP Questions

1. Can you talk us through some common preprocessing steps for text documents?

2. Tokenisation
    1. Can you describe the role of tokenisation?
    2. How would you do tokenisation in a document?
    3. What issues might occur if you train a tokeniser on news articles and then use it on scientific papers?

3. Stemming
    1. could you explain why stemming is considered to be crude in comparison to lemmatization?
    2. What extra information does lemmatization use that stemming does not?

4. You are given a data set containing tf-idf vectors for articles about birds and fish. 
The articles are labelled. How would you create a classification model for them?

5. Word Embeddings
    1. Can you describe word embeddings?
    2. As word embeddings can be expensive to train, it is sometimes more suitable to use pre-trained embeddings. 
Can you think of a limitation or negative to using pre-trained embeddings?
    3. How would you overcome this problem? 


## Document Comparison
1. Given a corpus of CVs how would you divide the text into smaller pieces, 
     and what information would you use to do it?
	- just spaces or commas, hyphens, etc.?
	
2. Can you think of some common issues that may make this difficult? 
	- Inflections, casing
	
3. How would you resolve those issues? 

4. What sort of features would you extract?

5. how would you identify job titles?

6. How would this change if you were given a list of skills and job titles?

7. How could we add some structure to the skills and link them to job titles? (how to merge variants, etc.)

## Recommendation Systems

8. How could you use these features to create a recommender?

9. How would you evaluate the results of your recommender?
	- relevant given that we often don't have labelled data when ranking
	- Look to see if they are just interested in picking a single relevant document or they consider ranking
	
10. If we take on a new client that is in a sector that is not represented in the original data set. 
What could cause problems for the recommender?


### Feedback
