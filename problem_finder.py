import os
import random
import json
import requests
import re
import html


def get_problems():
    path_to_json = "problems.json"
    with open(path_to_json, 'r') as file:
        data = json.load(file)
    return data['stat_status_pairs']


def get_random_problem(problems, difficulty):
    difficulty_levels = {'e': 1, 'easy': 1, 'm': 2, 'medium': 2, 'h': 3, 'hard': 3}
    filtered_problems = [problem for problem in problems if
                         problem['difficulty']['level'] == difficulty_levels[difficulty.lower()] and not problem[
                             'paid_only']]
    existing_dirs = {d.split('_')[0] for d in os.listdir() if os.path.isdir(d)}
    filtered_problems = [p for p in filtered_problems if str(p['stat']['frontend_question_id']) not in existing_dirs]

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
                            p['stat']['frontend_question_id'] == specific_problem_id and not p['paid_only']), None)
            if not problem:
                print(f"Problem ID {specific_problem_id} not found or is a paid problem.")
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

        title = problem['stat']['question__title']
        problem_id = problem['stat']['frontend_question_id']
        slug = problem['stat']['question__title_slug']
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
                return  # Breaks the outer loop and ends the function after handling one problem
            elif confirm_input in ['n', 'no']:
                print("Searching for another problem...")
                break  # Breaks only the inner loop to find another problem
            else:
                print("Invalid response. Please type 'Yes' (Y) or 'No' (N).")
                # Continues the inner loop to re-ask the yes/no question


if __name__ == "__main__":
    main()
