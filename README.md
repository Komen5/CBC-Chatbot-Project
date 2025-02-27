# CBC-Chatbot-Project
## Overview

Chatbots are advanced programs designed to simulate human-like conversations, and their adoption is rapidly transforming industries worldwide. [Research](https://masterofcode.com/blog/chatbot-statistics) shows that by the end of 2023, over 75% of customer queries were expected to be resolved through chatbot solutions.

This project introduces SomaBot, which is tailored for Kenya's Competency-Based Curriculum (CBC). SomaBot will assist students, parents, and educators by providing instant, accurate information about curriculum details, assessments, and educational policies. It will enhance engagement, simplify learning pathways, and ensure seamless access to CBC-related resources through advanced natural language processing (NLP) and machine learning techniques.

By delivering intelligent, context-aware responses, SomaBot will empower users to navigate the CBC system effortlessly, transforming how educational information is accessed and understood.

## Business Understanding

The Competency-Based Curriculum (CBC) in Kenya is designed to equip learners with practical skills, but its implementation has faced challenges. Parents, teachers, and students often struggle to access accurate and timely information regarding the curriculum, assessment methods, and their respective roles. Currently, most CBC-related inquiries rely on government circulars, school meetings, or online discussions, which are often fragmented and inconsistent.

To address this, SomaBot will be developed to provide instant, reliable, and structured responses to CBC-related questions. This chatbot will serve as an interactive platform where users can seek information about curriculum structure, assessment criteria, parental involvement, and available teaching resources. The goal is to enhance accessibility, reduce misinformation, and improve user engagement by leveraging natural language processing (NLP) for dynamic, intelligent responses.

## Problem statement

Accessing accurate and timely information about Kenya’s Competency-Based Curriculum (CBC) remains a challenge for students, parents, and educators. Traditional sources, such as government websites and educational institutions, are often complex, difficult to navigate, or lack real-time engagement. Additionally, language barriers between English and Swahili further hinder accessibility. SomaBot addresses these challenges by providing an AI-powered, bilingual chatbot capable of answering CBC-related queries with precision and also ensures that users receive relevant responses. 

## Data Understanding

To ensure the chatbot delivers relevant and accurate responses, the data was gathered from multiple sources. Official curriculum documents from the Kenya Institute of Curriculum Development (KICD) serve as the primary data source, supplemented by Ministry of Education policies, circulars, and guidelines. The data is primarily  text-based, comprising of structured content from official documents and unstructured conversations from forums and user queries.

There are two datasets :
  - FAQs (Frequently Asked Questions) dataset.

  - Tweets dataset(scrapped tweets from X, formally known as twitter).

The FAQs dataset contains 2533 entries(rows) and 2 columns, the Question and Answer columns . 

The tweets dataset contains 1086 rows and 6 columns, the tweet_count, username, text, created at, retweets and likes. 

The tweet dataset contained CBC tweets  from the  January 2017 to February 2025.

### Summary of features in the datasets :

 #### FAQs dataset 

  **Question:** The user’s inquiry or the asked question.

  **Answer:** The predefined response corresponding to the question.

 #### Tweets dataset

  **Tweet_count:** The total number of tweets collected in a dataset or tracking count of tweets in a conversation/thread.

  **Username:** The Twitter handle of the person who posted the tweet.

  **Text:** The actual content of the tweet, including any hashtags, mentions or links.

  **Created at:** The timestamp when the tweet was posted,that is, year, date, day, time.

  **Retweets:** The number of times this tweet has been retweeted (shared by others).

  **Likes:** The number of likes (previously "favorites") the tweet has received.

### Sources of Data:

FAQs Dataset – Structured question-answer pairs.

Tweets Dataset – Extracted tweets for analysis from X, formally known as twitter.

Official Curriculum Documents – Kenya Institute of Curriculum Development (KICD) policies, Teachers Arena Document, National Curriculum  Policy, KNEC, Teacher ac, Darasa app, Citizen Digital, KDRIDP.

User Queries – Data from past interactions to improve chatbot responses.

### Collection Methods:

Web Scraping – Extracting FAQs from websites and tweets from X(formally known as twitter).

Manual Curation – Collecting FAQs from government documents.

## Objectives

1. To develop a chatbot, that is SomaBot, that leverages TF-IDF, Cosine Similarity and RASA model to match user queries with relevant responses and optimize the best possible answers, ensuring accurate and efficient query resolution .

2. To analyze the question column in the FAQS dataset to identify the most frequently asked queries and common keywords, enabling optimization of chatbot responses and improving user query resolution.

3. To apply an NLP-based sentiment analysis approach using VADER and TextBlob to classify CBC-related tweets as positive, negative, or neutral, providing strategic insights into the education system.

4. To analyze sentiment trends in tweets about the CBC education system, providing actionable insights to support strategic decision-making for policy development, curriculum improvements, and stakeholder engagement 

5. To build and evaluate predictive models (Random Forest, XGBoost, and Logistic Regression) for sentiment classification, comparing their performance in accurately classifying CBC-related tweets.

## Success Metrics

1. The ideal sentiment classification model should attain a minimum F1 score of 60%.
2. The top-performing chatbot model should achieve at least 90%.
3. To successfully classify tweets into different sentiments (Neutral, Positive, Negative).


## Modeling
The following predictive models (Random Forest, XGBoost, and Logistic Regression) were built for sentiment classification, and their performance in accurately classifying CBC-related tweets was compared.

### Evaluation of the models
1. Random Forest: This model struggles to classify Negative cases correctly, predicting all as Neutral or Positive. It performs well on Neutral and Positive cases but misclassifies some Positive cases as Neutral.

2. XGBoost: This model shows better balance, with more accurate classifications for Neutral and Positive cases. However, it still misclassifies some Negative cases as Neutral or Positive.

3. Logistic Regression: This model struggles the most, misclassifying many Negative cases and showing lower accuracy for Neutral and Positive predictions compared to XGBoost.


## Conclusion

1. In conclusion, the most common inquiries surrounding CBC implementation emphasize self-expression, agricultural education, rural support, creativity, civic responsibility, innovation, teacher support, extracurricular activities, ethical decision-making, and financial literacy. These concerns reflect the key areas stakeholders consider crucial for the curriculum's success and effectiveness.

2. The NLP-based sentiment analysis using VADER and TextBlob provided valuable insights into public perception of the education system, highlighting key sentiments that can inform strategic decision-making and policy improvements.

3. The analysis suggests that most people have a positive outlook on CBC, as positive sentiment has consistently led, peaking in 2024. While there are increasing neutral discussions and some mild concerns, the overall trend indicates that the majority of public sentiment is favorable.

4. The sentiment classification model that performed best was XGBoost, achieving a weighted F1-score of 0.65, indicating strong overall performance in sentiment prediction.

5. The Rasa model for the somabot demonstrates outstanding performance, achieving an F1 score of 95.7%  and 96.1% intent classification accuracy. With high precision and recall, it consistently makes correct predictions, with minimal misclassifications occurring in ambiguous cases.

## Recommendation

1. Strengthen CBC key focus areas: Self-expression, agricultural education, rural support, creativity, civic responsibility, innovation, teacher support, extracurricular activities, ethical decision-making, and financial literacy by developing targeted policies and resources to enhance curriculum effectiveness.

2. Policymakers should sustain and build on the positive sentiment peak in 2024 by addressing concerns in neutral and negative discussions through public awareness campaigns that clarify misconceptions and reinforce CBC’s benefits.

3. As neutral discussions rise, further analysis is needed to understand shifting public discourse and potential concerns, while implementing feedback mechanisms to continuously improve CBC based on evolving public opinion.

4. Enhance sentiment classification accuracy by incorporating additional training data, and exploring advanced NLP techniques like transformer-based models.

5. Enhance chatbot capabilities by training it on more data to improve real-time assistance, curriculum guidance, and automated responses to CBC-related queries.
