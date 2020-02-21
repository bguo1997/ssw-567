from hw4 import print_commits,get_commit
import unittest
class TestHW(unittest.TestCase):

    def test_print_commits(self):
        self.assertEqual(print_commits(get_commit('bguo1997')), "Repo: HW09 Number of commits: 1, Repo: ssw-567 Number of commits: 2, Repo: Triangle-567 Number of commits: 5, Repo: GitHubApi567 Number of commits: 4, None")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
