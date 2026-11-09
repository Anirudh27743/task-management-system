
import unittest
import sys
from io import StringIO
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.task_pool = TaskPool()

    def test_add_task(self):
        task = Task("Complete assignment")
        self.task_pool.add_task(task)
        self.assertEqual(len(self.task_pool.tasks), 1)

    def test_get_open_tasks(self):
        self.task_pool.populate()
        open_tasks = self.task_pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)

    def test_get_done_tasks(self):
        self.task_pool.populate()
        done_tasks = self.task_pool.get_done_tasks()
        self.assertEqual(len(done_tasks), 3)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(
        stream=sys.stdout,
        verbosity=2
    )
    unittest.main(testRunner=runner)
