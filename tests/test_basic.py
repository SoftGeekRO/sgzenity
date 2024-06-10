#  -*- coding: utf-8 -*-
import os
from pathlib import Path

import pytest


def file_contains_text(file: Path, text: str) -> bool:
    return open(file, "r").read().find(text) != -1


@pytest.fixture(scope="module")
def script_loc(request):
    """Return the directory of the currently running test script

    :param request:
    :return:
    """

    return Path(request.fspath).parent.parent


def test_cicd(script_loc):
    assert file_contains_text(
        script_loc.joinpath("Makefile"), "build-and-publish"
    ), "From the Makefile is missing the build-and-publish command"


def test_tox(script_loc):
    """

    :param script_loc:
    :return:
    """
    assert file_contains_text(
        script_loc.joinpath(".github/workflows/push_to_main.yml"),
        "poetry add tox-gh-actions",
    )
    assert os.path.isfile(script_loc.joinpath("tox.ini"))
