import requests


def get_commit(ID):
    result = {}
    r = requests.get("https://api.github.com/users/" + ID +"/repos")
    repos = r.json()

    for repo in repos:
        repo_name = repo["name"]
        r = requests.get("https://api.github.com/repos/" + ID + "/" + repo_name + "/commits")
        commits = r.json()
        result[repo_name] = len(commits)
    return result


def print_commits(result):
    for key, value in result.items():
        print(f'Repo: {key} Number of commits: {value}')


if __name__ == '__main__':
    ID = input('input an ID:')
    print(print_commits(get_commit(ID)))

