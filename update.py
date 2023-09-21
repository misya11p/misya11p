import json
from typing import List


README = 'README.md'
TEMPLATE = 'template.md'
REPOS = 'repos.json'
USER_ID = 'misya11p'
LEARNING_BLOCK = '<learning-block>'
DEVELOPMENT_BLOCK = '<development-block>'
limit = 10

def main():
    with open(REPOS) as f:
        repos = json.load(f)
    learning_repos = repos['learning']
    development_repos = repos['development']

    with open(TEMPLATE) as f:
        readme = f.read()
    learning_block = generate_block(learning_repos[:limit])
    development_block = generate_block(development_repos[:limit])
    readme = readme.replace(LEARNING_BLOCK, learning_block)
    readme = readme.replace(DEVELOPMENT_BLOCK, development_block)

    with open(README, 'w') as f:
        f.write(readme)


def generate_card(repo_name: str):
    href = f'https://github.com/{USER_ID}/{repo_name}'
    scr = \
        'https://github-readme-stats.vercel.app/api/pin/'\
        f'?username={USER_ID}&repo={repo_name}'
    card = f'<a href="{href}"><img src="{scr}" /></a>'
    return card

def generate_block(repos: List[str]):
    block = '<p>\n'
    for repo in repos:
        block += generate_card(repo) + '\n'
    block += '</p>'
    return block


if __name__ == '__main__':
    main()
