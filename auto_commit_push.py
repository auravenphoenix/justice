#!/usr/bin/env python3

import os
import git.config
from git import Repo


class AutoCommitPush:
    def __init__(self, repository_path):
        print(f"INFO - Load git repository.")
        self.__repository = Repo(repository_path)
        self.__git: git.Git = self.__repository.git

    def commit_and_push_all(self):
        for item in self.__repository.index.diff(None):
            self.commit_and_push_file(item.a_path, item.change_type)
        for item in self.__repository.untracked_files:
            self.commit_and_push_file(item)

    def commit_and_push_file(self, file, change_type='A'):
        commit_msg = f"{change_type} {file}"
        print(f"### {commit_msg}")
        match change_type:
            case 'D':
                self.__repository.index.remove([file])
            case _:
                self.__repository.index.add([file])
        self.__repository.index.commit(commit_msg)
        self.__repository.remote().push()


if __name__ == '__main__':
    auto_commit_pusher = AutoCommitPush('.')
    auto_commit_pusher.commit_and_push_all()
    os.system('(bell&)')
