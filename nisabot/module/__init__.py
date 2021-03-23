# Nisabot
# Copyright (C) 2021 I Do Not Know, <https://github.com/agung267/NEWNISA.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from nisabot import LOAD, LOGGER, NO_LOAD


def __list_all_module():
    import glob
    from os.path import basename, dirname, isfile

    # This generates a list of module in this folder for the * in __main__ to
    # work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_module = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(
                any(mod == module_name for module_name in all_module)
                for mod in to_load
            ):
                LOGGER.error("Invalid loadorder names. Quitting.")
                sys.exit(1)

        else:
            to_load = all_module

        if NO_LOAD:
            LOGGER.info("Not loading: {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]

        return to_load

    return all_module


ALL_MODULE = sorted(__list_all_module())
LOGGER.info("Modules to load: %s", str(ALL_MODULE))
__all__ = ALL_MODULE + ["ALL_MODULE"]
