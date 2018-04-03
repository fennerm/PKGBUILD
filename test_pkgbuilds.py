#!/usr/bin/env python
"""PKGBUILD test suite."""
from glob import glob

from plumbum import FG
from plumbum.cmd import docker
from pytest import fixture


def list_pkgbuilds():
    """List all the PKGBUILDs in the repo."""
    return glob('*/PKGBUILD')


@fixture(params=list_pkgbuilds())
def pkgbuild(request):
    """Parametrized fixture which returns paths to all PKGBUILDs in repo."""
    return request.param


def test_pkgbuilds(pkgbuild):
    docker['build', '-t', 'test_pkgbuild', '--build-arg',
           'pkgbuild=' + pkgbuild, '.'] & FG
    docker['run', '--rm', 'test_pkgbuild'] & FG
