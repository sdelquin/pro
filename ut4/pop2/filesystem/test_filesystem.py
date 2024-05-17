import pytest
from filesystem import FileSystem, FileSystemError

ERR_BASE_MSG = 'I/O error in filesystem'


@pytest.fixture
def fs():
    return FileSystem('ext4')


def test_build_filesystem(fs: FileSystem):
    assert isinstance(fs, FileSystem)
    assert isinstance(fs.root, dict)
    assert isinstance(fs.cwd, str)
    assert fs.format == 'ext4'

    fs2 = FileSystem('NTFS')
    assert fs2.format == 'ntfs'


def test_build_filesystem_fails_when_format_is_not_supported():
    with pytest.raises(FileSystemError) as err:
        FileSystem('matraca')
    assert str(err.value) == f'{ERR_BASE_MSG}: Given format is not supported'


def test_is_directory():
    assert FileSystem.is_directory('/')
    assert FileSystem.is_directory('/tmp')
    assert FileSystem.is_directory('/tmp/')
    assert not FileSystem.is_directory('tmp')
    assert not FileSystem.is_directory('/tmp/info.txt')


def test_is_file():
    assert FileSystem.is_file('matraca.dat')
    assert FileSystem.is_file('/tmp/matraca.dat')
    assert not FileSystem.is_file('/tmp')
    assert not FileSystem.is_file('/tmp/')


def test_directory_existence(fs: FileSystem):
    fs.root['/'] = None
    assert '/' in fs
    assert '/tmp' not in fs


def test_mkdir(fs: FileSystem):
    fs.mkdir('/')
    assert '/' in fs.root
    fs.mkdir('/var')
    assert '/var' in fs.root


def test_mkdir_fails_when_no_directory_is_given(fs: FileSystem):
    with pytest.raises(FileSystemError) as err:
        fs.mkdir('matraca.dat')
    assert str(err.value) == f'{ERR_BASE_MSG}: Given path is not a directory'


def test_mkdir_fails_when_directory_exists(fs: FileSystem):
    fs.mkdir('/')
    with pytest.raises(FileSystemError) as err:
        fs.mkdir('/')
    assert str(err.value) == f'{ERR_BASE_MSG}: Directory already exists'


def test_cd(fs: FileSystem):
    fs.mkdir('/tmp')
    fs.cd('/tmp')
    assert fs.cwd == '/tmp'


def test_cd_fails_when_no_directory_is_given(fs: FileSystem):
    with pytest.raises(FileSystemError) as err:
        fs.cd('matraca.dat')
    assert str(err.value) == f'{ERR_BASE_MSG}: Given path is not a directory'


def test_cd_fails_when_directory_does_not_exist(fs: FileSystem):
    with pytest.raises(FileSystemError) as err:
        fs.cd('/')
    assert str(err.value) == f'{ERR_BASE_MSG}: Directory does not exist'


def test_touch_works_with_absolute_path(fs: FileSystem):
    fs.mkdir('/tmp')
    fs.touch('/tmp/matraca.dat')
    assert 'matraca.dat' in fs.root['/tmp']


def test_touch_works_with_relative_path(fs: FileSystem):
    fs.mkdir('/tmp')
    fs.cd('/tmp')
    fs.touch('matraca.dat')
    assert 'matraca.dat' in fs.root['/tmp']


def test_touch_fails_when_no_file_is_given(fs: FileSystem):
    with pytest.raises(FileSystemError) as err:
        fs.touch('/tmp')
    assert str(err.value) == f'{ERR_BASE_MSG}: Given path is not a file'


def test_touch_fails_when_directory_does_not_exist(fs: FileSystem):
    with pytest.raises(FileSystemError) as err:
        fs.touch('/tmp/matraca.dat')
    assert str(err.value) == f'{ERR_BASE_MSG}: Directory does not exist'


def test_len(fs: FileSystem):
    NUM_DIRS = 3
    NUM_FILES = 10
    for i in range(NUM_DIRS):
        directory = f'/tmp{i}'
        fs.mkdir(directory)
        fs.cd(directory)
        for j in range(NUM_FILES):
            fs.touch(f'file{j:02d}.txt')
    assert len(fs) == NUM_DIRS * NUM_FILES


def test_str(fs: FileSystem):
    NUM_DIRS = 3
    NUM_FILES = 10
    for i in range(NUM_DIRS):
        directory = f'/tmp{i}'
        fs.mkdir(directory)
        fs.cd(directory)
        for j in range(NUM_FILES):
            fs.touch(f'file{j:02d}.txt')
    assert str(fs) == 'ext4 filesystem with 30 files'


def test_dirs(fs: FileSystem):
    fs.mkdir('/tmp')
    fs.mkdir('/var')
    fs.mkdir('/usr')
    fs.mkdir('/home')
    assert fs.dirs == ['/home', '/tmp', '/usr', '/var']


def test_files(fs: FileSystem):
    fs.mkdir('/tmp')
    fs.cd('/tmp')
    fs.touch('file3.dat')
    fs.touch('file2.dat')
    fs.touch('file1.dat')
    assert fs.files == ['file1.dat', 'file2.dat', 'file3.dat']


def test_iteration_protocol(fs: FileSystem):
    fs.mkdir('/var')
    fs.cd('/var')
    fs.touch('vardata3.txt')
    fs.touch('vardata1.txt')
    fs.touch('vardata2.txt')

    fs.mkdir('/tmp')
    fs.cd('/tmp')
    fs.touch('tmpdata3.txt')
    fs.touch('tmpdata1.txt')
    fs.touch('tmpdata2.txt')

    iterator = iter(fs)
    next(iterator) == 'tmpdata1.txt'
    next(iterator) == 'tmpdata2.txt'
    next(iterator) == 'tmpdata3.txt'
    next(iterator) == 'vardata1.txt'
    next(iterator) == 'vardata2.txt'
    next(iterator) == 'vardata3.txt'

    with pytest.raises(StopIteration):
        next(iterator)
