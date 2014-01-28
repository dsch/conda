from __future__ import print_function, absolute_import, division

from test_cli import run_conda_command

def test_info():
    conda_info = run_conda_command('info')
    for name in ['platform', 'conda version', 'root environment',
        'default environment', 'envs directories', 'package cache',
        'channel URLs', 'config file', 'is foreign system']:
        assert name in conda_info

    conda_info_e = run_conda_command('info', '-e')
    assert 'root' in conda_info

    conda_info_s = run_conda_command('info', '-s')
    for name in ['sys.version', 'sys.prefix', 'sys.executable', 'conda location',
        'conda-build', 'CIO_TEST', 'CONDA_DEFAULT_ENV', 'LD_LIBRARY_PATH',
        'PATH', 'PYTHONPATH']:
        assert name in conda_info_s

    conda_info_all = run_conda_command('info', '--all')
    assert conda_info in conda_info_all
    assert conda_info_e in conda_info_all
    assert conda_info_s in conda_info_all
