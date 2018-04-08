#!/usr/bin/env python
"""PKGBUILD test suite."""
from glob import glob

from plumbum import FG
from plumbum.cmd import docker
from pytest import fixture


def list_pkgbuilds():
    """List all the PKGBUILDs in the repo."""
    return glob('*/PKGBUILD')

def pytest_addoption(parser):
    parser.addoption('--cmdopt', action='store', default='all',
                     help='PKGBUILD which should be tested (defaults to all)')


@fixture(params=list_pkgbuilds())
def pkgbuild(request):
    """Parametrized fixture which returns paths to all PKGBUILDs in repo.

    If the --cmdopt option was specified, it just returns that instead.
    """
    if request.config.getoption('--cmdopt') != 'all':
        return request.config.getoption('--cmdopt')
    else:
        return request.param


def test_pkgbuilds(pkgbuild):
    docker['build', '-t', 'test_pkgbuild', '--build-arg',
           'pkgbuild=' + pkgbuild, '.'] & FG
    docker['run', '--rm', '-t', 'test_pkgbuild'] & FG
