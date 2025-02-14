import requests
# from newspaper import Article
import os
from dotenv import load_dotenv

load_dotenv()

def brave_search(query):
    news_articles = []
    headers = {"X-Subscription-Token": os.getenv("BRAVE_API_KEY")}
    params = {"q": query, "count": 5}  # Get top 5 results
    response = requests.get("https://api.search.brave.com/res/v1/news/search",
                           headers=headers, params=params)
    response = response.json()
    results = response['results']

    for result in results:
        news_articles.append(
            {
                'title': result['title'],
                'text': result['description'],
                'url': result['url']
            }
        )

    if news_articles:
        return news_articles
    return None

# def scrape_articles(urls):
#     articles = []
#     for url in urls:  # Scrape top 3
#         try:
#             article = Article(url)
#             article.download()
#             article.parse()
#             articles.append({
#                 "title": article.title,
#                 "text": article.text,
#                 "url": url
#             })
#         except:
#             continue
#     return articles

# web_result = brave_search("Elon musk has acquired Openai's non-profit?")['results']
# print("Direct titles from brave_search")
# for result in web_result:
#     print(f"TITLE:{result['title']}")
#     print(f"Description:{result['description']}")
# urls = [res['url'] for res in web_result]
# articles = scrape_articles(urls)
# print("Titles from newspaper3k")
# for article in articles:
#     print(article['title'])