from __future__ import absolute_import as _

from ._read import read_plink, read_plink1_bin
from ._testit import test

__version__ = "1.3.0"


def example_file_prefix():
    r"""Data files prefix."""
    import os

    p = __import__("pandas_plink").__path__[0]
    return os.path.join(p, "test", "data_files", "data")


__all__ = [
    "__version__",
    "test",
    "example_file_prefix",
    "read_plink",
    "read_plink1_bin",
]
