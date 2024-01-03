import requests
import time
import logging
from typing import List, Dict

GITHUB_API_URL = "https://api.github.com"
GITHUB_ACCESS_TOKEN = ''
USER_NAME = "rivka236"

logging.basicConfig(level=logging.INFO)

def get_public_repositories(access_token: str) -> Dict[str, List[str]]:
    headers = {'Authorization': f'token {access_token}'}
    url = f'{GITHUB_API_URL}/user/repos'
    urls = []
    repositories_name = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        repo_data = response.json()
        for repo in repo_data:
            if repo['visibility'] == "private":
                logging.info(f"The repository {repo['name']} is set to private, ensuring data safety")
            else:
                logging.warning(f"Misconfiguration Detected! The repository: {repo['name']} is set to public.")
                repositories_name.append(repo["name"])
                urls.append(repo['url'])

    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")

    return {"urls": urls, "repositories_name": repositories_name}

def make_repositories_private(urls: List[str], access_token: str) -> None:
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"private": True}

    for url in urls:
        try:
            response = requests.patch(url, headers=headers, json=data)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")

def print_repository_contents(username: str, repositories_name: List[str]) -> None:
    try:
        for repository_name in repositories_name:
            api_url = f'{GITHUB_API_URL}/repos/{username}/{repository_name}/contents'

            response = requests.get(api_url)
            response.raise_for_status()

            data = response.json()
            logging.info(data)

    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")

def run() -> None:
    logging.info("Checking repositories for visibility...")
    public_repositories = get_public_repositories(GITHUB_ACCESS_TOKEN)
    if public_repositories["repositories_name"]:
        logging.warning("Risk on public repositories, There is access to repository contents")
        print_repository_contents(USER_NAME, public_repositories["repositories_name"])
        make_repositories_private(public_repositories["urls"], GITHUB_ACCESS_TOKEN)

        logging.info("Waiting for changes to propagate...")
        time.sleep(30) 
        logging.info("After making the repository private, checking access")
        print_repository_contents(USER_NAME, public_repositories["repositories_name"])
        logging.info("Configuration Update Complete! All repositories have been successfully set to private.")
    else:
        logging.info("All Repositories Private: Congratulations! All repositories are set to private, ensuring maximum security. No misconfigurations detected.")

if __name__ == "__main__":
    run()
