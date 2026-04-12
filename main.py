import time
from fetcher import fetchMyArticles
from summarizer import generateSummary
from injector import injectArticleCard

def updateArticle():
    """
    This function handles the complete automation flow:
    1. Fetch latest articles
    2. Generate AI summary
    3. Inject article into portfolio
    """

    print("Starting portfolio update process...")

    # Fetching articles
    articles = fetchMyArticles()

    # If no articles found
    if not articles:
        print("No new articles found. Nothing to update.")
        return

    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            existingContent = f.read()
    except FileNotFoundError:
        existingContent = ""

    newArticles = [a for a in articles if a['url'] not in existingContent]

    if not newArticles:
        print("No new unique articles to add. Everything is up to date!")
        return
    
    # Picking the latest article
    latest = articles[0]
    print(f"Working on: {latest['title']}")

    # Generating summary
    print("Generating summary...")
    summary = generateSummary(latest['body_markdown'])

    # Injecting into HTML
    print("Updating portfolio UI...")
    isInserted = injectArticleCard(latest, summary)

    # Final status
    if isInserted:
        print(f"Done! Portfolio updated with: {latest['title']}")
    else:
        print("Something went wrong while updating the portfolio.")

if __name__ == "__main__":
    updateArticle()