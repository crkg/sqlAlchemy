from learnpy.resources.sample_os_cmd import work
import pytest
import mock

class TestSampleOsCmd:
    def test_work(self, mocker):
        mocker.patch('learnpy.resources.sample_os_cmd.os.getcwd', return_value='C:\\Program Files')
        assert work() == 'C:\\Program Files'

    def test_work_other(self, mocker):
        mock_getcwd = mocker.patch('learnpy.resources.sample_os_cmd.os.getcwd')
        mock_getcwd.return_value = 'C:\\Program Files'
        assert work() == 'C:\\Program Files'

    @mock.patch('learnpy.resources.sample_os_cmd.os.getcwd')
    def test_work_with_patch(self, mock_cwd):
        mock_cwd.return_value = 'C:\\Program Files'
        assert work() == 'C:\\Program Files'