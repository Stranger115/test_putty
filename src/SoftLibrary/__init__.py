from .app_library import AppOperaLibrary
from .data_generate import DataGenerate


class SoftLibrary(AppOperaLibrary, DataGenerate):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

