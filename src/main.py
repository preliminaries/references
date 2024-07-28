"""Module main.py"""
import os
import sys


def main():
    """
    Entry point
    """

    # Preparing storage areas
    setup = src.setup.Setup(service=service, s3_parameters=s3_parameters)
    setup.exc(bucket_name=s3_parameters.external, prefix=s3_parameters.path_external_references)
    setup.exc(bucket_name=s3_parameters.internal, prefix=configurations.s3_prefix)

    # Transfer ...
    src.data.interface.Interface(service=service, s3_parameters=s3_parameters).exc()

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Setting-up
    root: str = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Modules
    import config
    import src.data.interface
    import src.functions.cache
    import src.functions.service
    import src.s3.s3_parameters
    import src.setup

    configurations = config.Config()

    # S3 S3Parameters, Service
    s3_parameters = src.s3.s3_parameters.S3Parameters().exc()
    service = src.functions.service.Service(region_name=s3_parameters.region_name).exc()

    main()
