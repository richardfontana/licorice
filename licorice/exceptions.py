# Copyright (C) 2015  Tomas Radej <tradej@redhat.com> #
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

class LoadError(Exception):
    '''
    Class denoting an error while loading the project
    '''
    pass

class RunTimeException(Exception):
    '''
    Class denoting a run time exception
    '''
    pass
