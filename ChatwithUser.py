import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


dataframe = pandas.read_csv("covid_faq.csv")
dataframe.dropna(inplace=True)
vectorizer = TfidfVectorizer()

vectorizer.fit(numpy.concatenate((dataframe.Question,dataframe.Answer)))
vectorized_questions = vectorizer.transform(dataframe.Question)

def reply(user_input):

    vectorized_user_input = vectorizer.transform([user_input])
    similarities = cosine_similarity(vectorized_user_input,vectorized_questions)
    closest_question = numpy.argmax(similarities,axis=1)
    # print("Closest question: ", closest_question)
    answer = dataframe.Answer.iloc[closest_question].values[0]
    # print("Answer: ", answer)
    return answer, closest_question
