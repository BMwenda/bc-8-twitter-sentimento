# bc-8-twitter-sentimento
A python app that fetches a user's tweets from the Twitter API and performs a sentiments analysis.

The appication gets as input the username and the maximum number of tweets to be retrieved

After the retrieval the application notifies for a completion message and a message of the total tweets retrieved

Analysis Done

  - Word frequency in descending order
  - Get the top ten words in the tweets
  - Get the hash tags in the tweets
Additional feature:
  Removal of keywords

All the dependencies needed by the application are in the requirements.txt. Just run
 - cd project_root_folder/
 - pip install -r requirements.txt

Move the nltk folder to user/home. This is files are needed by the nltk library
