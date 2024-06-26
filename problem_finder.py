import os
import random
import requests
import re
import html
from datetime import date


def get_problems():
    url = "https://raw.githubusercontent.com/juyingnan/leetcode_problems/main/simplified_problems.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        return data['stat_status_pairs']
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")

    return []


def get_random_problem(problems, difficulty):
    difficulty_levels = {'e': 1, 'easy': 1, 'm': 2, 'medium': 2, 'h': 3, 'hard': 3}
    filtered_problems = [problem for problem in problems if
                         problem['level'] == difficulty_levels[difficulty.lower()]]
    existing_dirs = {d.split('_')[0] for d in os.listdir() if os.path.isdir(d)}
    filtered_problems = [p for p in filtered_problems if str(p['id']) not in existing_dirs]

    if not filtered_problems:
        print("No more new problems available for this difficulty.")
        return None

    return random.choice(filtered_problems)


def fetch_problem_description(slug):
    url = "https://leetcode.com/graphql"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    json_data = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": slug
        },
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            content
            difficulty
          }
        }
        """
    }

    try:
        response = requests.post(url, json=json_data, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        question_data = response.json()
        html_content = question_data['data']['question']['content']

        if not html_content:
            return "Description not available or is a paid content."

        # Removing all HTML tags using regular expression
        text_content = re.sub('<[^<]+?>', '', html_content).replace('&nbsp;', ' ')
        text_content = html.unescape(text_content)

        return text_content.strip()

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")

    return "Failed to fetch the description due to a network error."


def main():
    difficulty_map = {
        '1': 'Easy', 'e': 'Easy', 'easy': 'Easy',
        '2': 'Medium', 'm': 'Medium', 'medium': 'Medium',
        '3': 'Hard', 'h': 'Hard', 'hard': 'Hard'
    }

    problems = get_problems()  # Assume this function is defined to fetch all problems

    while True:
        user_input = input(
            "Enter difficulty: Easy (E), Medium (M), Hard (H) [Medium]\nor a specific Problem ID: ").strip().lower() or 'm'

        if user_input.isdigit():  # User inputs a specific problem ID
            specific_problem_id = int(user_input)
            problem = next((p for p in problems if
                            p['id'] == specific_problem_id), None)
            if not problem:
                print(f"Problem ID {specific_problem_id} not found.")
                print("Maybe the problems file is outdated.")
                print("Please go to https://leetcode.com/api/problems/all/ to get the latest problem content.")
                print("Paste the content into the file named 'raw.json' in "
                      "https://github.com/juyingnan/leetcode_problems/tree/main" )
                print("Then run the simplified_problems.json script to format the JSON file.")
                print("Or you can call Bunny to solve this problem.")
                continue
        else:
            if user_input in difficulty_map:  # Valid difficulty entered
                difficulty = difficulty_map[user_input]
                problem = get_random_problem(problems, difficulty)
                if not problem:
                    print("No more new problems available for this difficulty.")
                    return
            else:
                print("Invalid response. Please enter Easy (E), Medium (M), or Hard (H), or a specific problem ID.")
                continue  # Continue asking for input

        title = problem['title']
        problem_id = problem['id']
        slug = problem['slug']
        problem_url = f"https://leetcode.com/problems/{slug}"

        while True:  # Inner loop for yes/no confirmation
            prompt_confirm = (f"Found problem {problem_id}: {title}: \n{problem_url}\n Proceed? [Yes (Y)/No (N)] ["
                              f"Yes]: ")
            confirm_input = input(prompt_confirm).strip().lower() or 'yes'
            if confirm_input in ['y', 'yes']:
                directory_name = f"{problem_id}_{title.replace(' ', '_').replace(',', '').replace('?', '').replace(':', '').replace('/', '_')}"
                os.makedirs(directory_name, exist_ok=True)

                description = fetch_problem_description(slug)
                description_file_path = os.path.join(directory_name, "description.txt")
                with open(description_file_path, 'w', encoding='utf-8') as file:
                    file.write(description)

                print(f"Folder '{directory_name}' created with description.")
                print(f"Please review the problem description from this file: {description_file_path}")
                today_date = date.today().strftime('%Y/%m/%d')
                log_entry = (
                    f"- **{today_date}** - [Problem {problem_id}: {title}]({problem_url})\n"
                )
                with open("README.md", "a") as file:
                    file.write(log_entry)
                print(f"Added daily log to readme: Problem {problem_id}: {title}")
                return  # Breaks the outer loop and ends the function after handling one problem
            elif confirm_input in ['n', 'no']:
                print("Searching for another problem...")
                break  # Breaks only the inner loop to find another problem
            else:
                print("Invalid response. Please type 'Yes' (Y) or 'No' (N).")
                # Continues the inner loop to re-ask the yes/no question


if __name__ == "__main__":
    main()
