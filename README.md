# CBC-Chatbot-Project
## Overview
This project involved building a chatbot to  automate responses for the new education system in Kenya (CBC), assisting  students, parents, and educators with curriculum details, assessments, and policies. It enhances engagement, provides instant information, and simplifies learning pathways using AI-driven conversational support tailored to user needs.

## Business Understanding
The Competency-Based Curriculum (CBC) in Kenya is designed to equip learners with practical skills, but its implementation has faced challenges. Parents, teachers, and students often struggle to access accurate and timely information regarding the curriculum, assessment methods, and their respective roles. Currently, most CBC-related inquiries rely on government circulars, school meetings, or online discussions, which are often fragmented and inconsistent.

To address this, an AI-powered chatbot will be developed to provide instant, reliable, and structured responses to CBC-related questions. This chatbot will serve as an interactive platform where users can seek information about curriculum structure, assessment criteria, parental involvement, and available teaching resources. The goal is to enhance accessibility, reduce misinformation, and improve user engagement by leveraging natural language processing (NLP) for dynamic, intelligent responses.

## Data Understanding
To ensure the chatbot delivers relevant and accurate responses, data will be gathered from multiple sources. Official curriculum documents from the Kenya Institute of Curriculum Development (KICD) will serve as the primary data source, supplemented by Ministry of Education policies, circulars, and guidelines. 
The data will primarily be text-based, comprising structured content from official documents and unstructured conversations from forums and user queries. 

## Objectives
1. To develop a chatbot that leverages TF-IDF and Cosine Similarity to match user queries with relevant responses, while utilizing Random Forest/XGBoost to rank and optimize the best possible answers, ensuring accurate and efficient query resolution

2. To analyze the question column in the FAQS dataset to identify the most frequently asked queries and common keywords, enabling optimization of chatbot responses and improving user query resolution.

3. To apply an NLP-based sentiment analysis approach using VADER and TextBlob to classify CBC-related tweets as positive, negative, or neutral, providing strategic insights into the education system.

4. To analyze sentiment trends in tweets about the CBC education system, providing actionable insights to support strategic decision-making for policy development, curriculum improvements, and stakeholder engagement 

5. To build and evaluate predictive models (Random Forest, XGBoost, and Logistic Regression) for sentiment classification, comparing their performance in accurately classifying CBC-related tweets.
