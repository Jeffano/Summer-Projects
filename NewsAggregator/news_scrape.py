from newspaper import Article
from textblob import TextBlob


def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()

    article.download('punkt')
    article.nlp()

    print("Author: " + str(article.authors))

    date = article.publish_date

    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    print("Top Image Url: " + str(article.top_image))

    print("\nA Quick Summary")
    print("-------------------------------------------")
    print(article.summary)

    review = TextBlob(article.summary)
    print("\nPolarity & Subjectivity")
    print("-------------------------------------------")
    print(review.sentiment)

link = input("Enter The URL You Would Like To Analyze: ")
summarize_article(link)

