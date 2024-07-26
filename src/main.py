"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry point
    """

    # Logging
    logger: logging.Logger = logging.getLogger(name=__name__)
    logger.info('references')

    # Empty/Create Buckets
    src.setup.Setup(service=service, s3_parameters=s3_parameters, warehouse=configurations.warehouse).exc(
        bucket_name=s3_parameters.external, prefix=s3_parameters.path_external_references)

    # Explore
    strings = src.data.key_strings.KeyStrings().exc(
        path=os.path.join(root, 'data', 'references'),
        extension='csv', prefix=s3_parameters.path_external_references)
    logger.info(strings.to_dict('records'))
    for string in strings.to_dict(orient='records'):
        logger.info(string['metadata'])

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Setting-up
    root: str = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.captureWarnings(capture=True)

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import config
    import src.data.key_strings
    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.service
    import src.s3.s3_parameters
    import src.setup

    configurations = config.Config()

    # S3 S3Parameters, Service
    s3_parameters: s3p.S3Parameters = src.s3.s3_parameters.S3Parameters().exc()
    service: sr.Service = src.functions.service.Service(region_name=s3_parameters.region_name).exc()

    main()
