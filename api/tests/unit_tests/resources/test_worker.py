from learnpy.resources.worker import Helper, WorkerService
import pytest

class FakeHelper:

    def get_path(self):
        return "C:\\Program Files\\db"


class TestHelper:
    def test_helper(self, mocker):
        a = Helper('db')
        assert isinstance(a, Helper)

    def test_get_path(self, mocker):
        mocker.patch('learnpy.resources.worker.os.getcwd', return_value='C:\\Program Files')
        a = Helper('db')
        assert a.get_path() == 'C:\\Program Files\\db'


class TestWorker:
    def test_worker_instaance_creation(self, mocker):
        mocker.patch('learnpy.resources.worker.Helper', return_value=FakeHelper())
        w = WorkerService()
        assert isinstance(w, WorkerService)

    def test_worker_work(self,mocker):
        mocker.patch('learnpy.resources.worker.Helper', return_value=FakeHelper())
        w = WorkerService()
        assert w.work() == 'C:\\Program Files\\db'

    def test_worker_work_without_fake_helper(self,mocker):
        mock_helper = mocker.patch('learnpy.resources.worker.Helper', autospec=True)
        mock_helper.return_value.get_path.return_value = 'C:\\Program Files\\db'
        w = WorkerService()
        assert w.work() == 'C:\\Program Files\\db'
