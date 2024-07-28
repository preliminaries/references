import logging
import os

import config

import src.s3.ingress
import src.data.dictionary

import src.elements.s3_parameters as s3p
import src.elements.service as sr


class Interface:

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 (Simple Storage Service) parameters
                              settings of this project, e.g., region code name, buckets, etc.
        """

        self.__service = service
        self.__s3_parameters = s3_parameters

        # Amazon S3 keys, etc.
        self.__dictionary = src.data.dictionary.Dictionary()

        # Configurations
        self.__configurations = config.Config()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __references(self) -> list[str]:
        """

        :return:
        """

        prefix = self.__s3_parameters.path_external_references

        # Storage details for Amazon S3 (Simple Storage Service) transfer step
        strings = self.__dictionary.exc(path=os.path.join(os.getcwd(), 'data', 'references'),
                                         extension='csv', prefix=prefix)

        # Transferring to Amazon S3
        return src.s3.ingress.Ingress(
            service=self.__service, bucket_name=self.__s3_parameters.external
        ).exc(strings=strings)

    def __raw(self) -> list[str]:
        """

        :return:
        """

        prefix = self.__configurations.s3_prefix + 'raw/'

        # Storage details for Amazon S3 (Simple Storage Service) transfer step
        strings = self.__dictionary.exc(path=os.path.join(os.getcwd(), 'data', 'raw'),
                                         extension='xlsx', prefix=prefix)

        # Transferring to Amazon S3
        return src.s3.ingress.Ingress(
            service=self.__service, bucket_name=self.__s3_parameters.internal
        ).exc(strings=strings)


    def exc(self):
        """

        :return:
        """

        messages = self.__references()
        self.__logger.info(messages)

        messages = self.__raw()
        self.__logger.info(messages)
