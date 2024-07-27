"""Module main.py"""
import os
import sys


def main():
    """
    Entry point
    """

    # Empty/Create Bucket
    src.setup.Setup(service=service, s3_parameters=s3_parameters, warehouse=configurations.warehouse).exc(
        bucket_name=s3_parameters.external, prefix=s3_parameters.path_external_references)

    # Storage details for Amazon S3 (Simple Storage Service) transfer step
    strings = src.data.key_strings.KeyStrings().exc(
        path=os.path.join(root, 'data', 'references'),
        extension='csv', prefix=s3_parameters.path_external_references)

    # Transferring to Amazon S3
    src.s3.ingress.Ingress(
        service=service, bucket_name=s3_parameters.external).exc(strings=strings)

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Setting-up
    root: str = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Modules
    import config
    import src.data.key_strings
    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.service
    import src.s3.ingress
    import src.s3.s3_parameters
    import src.setup

    configurations = config.Config()

    # S3 S3Parameters, Service
    s3_parameters: s3p.S3Parameters = src.s3.s3_parameters.S3Parameters().exc()
    service: sr.Service = src.functions.service.Service(region_name=s3_parameters.region_name).exc()

    main()
