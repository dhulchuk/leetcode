import os
import re
import sys
import asyncio
from dataclasses import dataclass

import aiohttp

GRAPHQL_QUERY = {
    "operationName": "questionData",
    "variables": {
        'titleSlug': '',
    },
    "query": "query questionData($titleSlug: String!) {"
             "  question(titleSlug: $titleSlug) {"
             "    questionId"
             "    title"
             "    difficulty"
             "    topicTags {slug}"
             "  }"
             "}"
}

FILE_TEMPLATE = '''#  {tags}


class Solution:
    pass


if __name__ == '__main__':
    assert False
'''


def to_unders(s):
    return s.replace('-', '_')


@dataclass
class Templater:
    slug: str
    link: str
    question_id: str = ''
    title: str = ''
    difficulty: str = ''
    tags: str = ''
    directory: str = ''
    path: str = ''

    async def get_data(self):
        GRAPHQL_QUERY['variables']['titleSlug'] = self.slug
        async with aiohttp.ClientSession() as session:
            async with session.post('https://leetcode.com/graphql', json=GRAPHQL_QUERY) as response:
                resp_data = await response.json()
                data = resp_data['data']['question']
                self.question_id = data['questionId']
                self.title = data['title']
                self.difficulty = data['difficulty']
                self.tags = ' '.join(
                    f'{to_unders(topic["slug"])}'
                    for topic in data['topicTags']
                )
        print('Got data from leetcode!\n')

    def create_solution_file(self):
        self.directory = to_unders(self.slug)
        os.mkdir(self.directory)
        self.path = self.directory + '/main.py'
        with open(self.path, 'w') as f:
            f.write(FILE_TEMPLATE.format(tags=self.tags))
        print(f'{self.path} created!\n')

    def save_to_readme(self):
        placeholder = '| -- |'
        desc = f'| {self.question_id} | [{self.title}]({self.link}) | [Python](./{self.path}) | {self.difficulty} |'
        print(desc)
        with open('README.md', 'r') as f:
            readme = f.read()
        readme = readme.replace(placeholder, f'{desc}\n{placeholder}')
        with open('README.md', 'w') as f:
            f.write(readme)
        print('README.md updated!\n')

    def print_commit_message(self):
        print(f'#{self.question_id}: {self.title}\n')

    def format_workspace(self):
        self.create_solution_file()
        self.save_to_readme()
        self.print_commit_message()


async def main():
    try:
        link = sys.argv[1]
        slug = re.findall(r'https://leetcode.com/problems/(.*)/', link)[0]
    except IndexError:
        print('Provide link to leedcode problem as argument.')
        print('Example: https://leetcode.com/problems/house-robber/\n')
        return
    t = Templater(slug=slug, link=link)
    await t.get_data()
    t.format_workspace()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
