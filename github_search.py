#!/usr/bin/env python3
import requests
import sys

def search_github_tool(query):
    """
    This function searches GitHub for a repository that matches the query.
    """
    url = f"https://api.github.com/search/repositories?q={query}"
    
    # Sending the request to GitHub API
    response = requests.get(url)
    
    # Checking the response status
    if response.status_code == 200:
        data = response.json()
        
        # If there are results, print the first one
        if data["total_count"] > 0:
            print(f"Found {data['total_count']} result(s):")
            for repo in data["items"]:
                print(f"Repository Name: {repo['name']}")
                print(f"Description: {repo.get('description', 'No description available')}")
                print(f"Repository URL: {repo['html_url']}")
                print("-" * 50)
        else:
            print("No results found.")
    else:
        print(f"An error occurred while connecting to GitHub. Status code: {response.status_code}")

def main():
    while True:
        if len(sys.argv) < 2:
            print("Please enter a repository name or topic to search on GitHub.")
            break
        else:
            search_query = " ".join(sys.argv[1:])
            search_github_tool(search_query)
        
        # Ask user whether to continue or exit
        user_input = input("\nDo you want to continue searching? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
