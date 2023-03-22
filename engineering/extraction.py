"""
Extraction script
"""
from typing import Optional
import pandas as pd
from numpy import uint16, float32
from engineering.persistence_manager import PersistenceManager, DataType


def extract_raw_data(
        filename: str = 'penguins.csv',
        data_type: DataType = DataType.RAW, d_types: Optional[dict] = None
) -> pd.DataFrame:
    """
    Engineering method to extract raw data from csv file
    :param filename: Filename to extract data from. The default is
     'drugs_train.csv'
    :type filename: str
    :param data_type: Path where data will be saved: RAW or
     PROCESSED. The default is RAW
    :type data_type: DataType
    :param d_types: Optional dictionary to handle data types of columns.
     The default is None
    :type d_types: dict
    :return: Dataframe with raw data
    :rtype: pd.DataFrame
    """
    if not d_types:
        d_types = {
            'species': 'category', 'island': 'category',
            'bill_length_mm': float32, 'bill_depth_mm': float32,
            'flipper_length_mm': float32, 'body_mass_g': float32,
            'sex': 'category', 'year': uint16}
    dataframe: pd.DataFrame = PersistenceManager.load_from_csv(
        filename=filename, data_type=data_type, dtypes=d_types)
    return dataframe
