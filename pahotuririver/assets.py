from pathlib import Path

from clld.web.assets import environment

import pahotuririver


environment.append_path(
    Path(pahotuririver.__file__).parent.joinpath('static').as_posix(),
    url='/pahotuririver:static/')
environment.load_path = list(reversed(environment.load_path))
