"""Module key_strings.py"""
import logging
import glob
import os

import pathlib
import pandas as pd

import src.functions.objects


class KeyStrings:
    """
    Class KeyStrings
    """

    def __init__(self):
        pass

        self.__objects = src.functions.objects.Objects()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)
        
    def __metadata(self, path: str, vertices: list[str]):

        details = [{'vertex': vertex,
                    'metadata': self.__objects.read(uri=os.path.join(path, f'{pathlib.Path(vertex).stem}.json'))}
                   for vertex in vertices]
        self.__logger.info(details)

        frame = pd.DataFrame.from_records(details)
        self.__logger.info(frame)

    def exc(self, path: str, extension: str, prefix: str):
        """

        :param path: The path wherein the files of interest lie
        :param extension: The extension type of the files of interest
        :param prefix: The Amazon S3 (Simple Storage Service) where the files of path are heading
        :return:
        """

        # The list of files within the path directory, including its child directories.
        files: list[str] = glob.glob(pathname=os.path.join(path, '**',  f'*.{extension}'), recursive=True)
        self.__logger.info(files)
        
        vertices: list[str] = [file.rsplit(os.path.sep, maxsplit=1)[1] for file in files]
        self.__logger.info(vertices)

        self.__metadata(path=path, vertices=vertices)

        # Building the Amazon S3 strings
        keys: list[str] = [f'{prefix}{vertex}' for vertex in vertices]
        self.__logger.info(keys)
