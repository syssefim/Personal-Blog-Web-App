import json
from app import app, db, Article

def seed_database():
    # 1. Open and read the JSON file
    try:
        with open('articles.json', 'r') as file:
            articles_data = json.load(file)
    except FileNotFoundError:
        print("Error: Could not find articles.json file.")
        return

    # 2. Add data to the database inside the application context
    with app.app_context():
        print("Checking connection...")
        
        # 1. DELETE ALL EXISTING ARTICLES
        db.session.query(Article).delete()
        print("Existing articles deleted.")
        
        # 2. Add the new ones
        for item in articles_data:
            print(f"Adding article: {item['title']}")
            
            # Create a new Article object
            # We map the JSON keys (right) to the Database columns (left)
            new_article = Article(
                title=item['title'],
                date=item['publication_date'],  # Maps 'publication_date' to 'date'
                content=item['body']            # Maps 'body' to 'content'
            )
            
            # Add to the session
            db.session.add(new_article)
        
        # 3. Commit the changes to save them to the database
        try:
            db.session.commit()
            print("Success! Database populated.")
        except Exception as e:
            db.session.rollback()
            print(f"Error saving to database: {e}")

if __name__ == "__main__":
    seed_database()