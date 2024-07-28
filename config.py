"""Module config.py"""
import os


class Config:
    """
    Configuration
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        # A S3 (Simple Storage Service) parameters template
        self.s3_parameters_template = 'https://raw.githubusercontent.com/preliminaries/.github/master/profile/s3_parameters.yaml'

        # A S3 prefix
        self.s3_prefix = 'mileage/'
