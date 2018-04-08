def pytest_addoption(parser):
    parser.addoption('--cmdopt', action='store', default='all',
                     help='PKGBUILD which should be tested (defaults to all)')

