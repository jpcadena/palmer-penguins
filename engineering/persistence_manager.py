"""
Persistence script
"""
import logging
from enum import Enum
from typing import Union, Optional
import pandas as pd
from core.config import ENCODING

logger: logging.Logger = logging.getLogger(__name__)


class DataType(Enum):
    """
    Data Type class based on Enum
    """
    RAW: str = 'data/raw/'
    PROCESSED: str = 'data/processed/'
    FIGURES: str = 'reports/figures/'


class PersistenceManager:
    """
    Persistence Manager class
    """

    @staticmethod
    def save_to_csv(
            data: Union[list[dict], pd.DataFrame],
            data_type: DataType = DataType.PROCESSED, filename: str = 'data'
    ) -> bool:
        """
        Save list of dictionaries as csv file
        :param data: list of tweets as dictionaries
        :type data: list[dict]
        :param data_type: folder where data will be saved
        :type data_type: DataType
        :param filename: name of the file
        :type filename: str
        :return: confirmation for csv file created
        :rtype: bool
        """
        dataframe: pd.DataFrame
        if isinstance(data, pd.DataFrame):
            dataframe = data
        else:
            if not data:
                return False
            dataframe = pd.DataFrame(data)
        dataframe.to_csv(f'{str(data_type)}{filename}.csv', index=False,
                         encoding=ENCODING)
        return True

    @staticmethod
    def load_from_csv(
            filename: str, data_type: DataType, dtypes: Optional[dict]
    ) -> pd.DataFrame:
        """
        Load dataframe from CSV using chunk scheme
        :param filename: name of the file
        :type filename: str
        :param data_type: Path where data will be saved
        :type data_type: DataType
        :param dtypes: Dictionary of columns and datatypes
        :type dtypes: dict
        :return: dataframe retrieved from CSV after optimization with chunks
        :rtype: pd.DataFrame
        """
        filepath: str = f'{data_type.value}{filename}'
        dataframe: pd.DataFrame = pd.read_csv(
            filepath, header=0, dtype=dtypes, encoding=ENCODING)
        return dataframe

    @staticmethod
    def save_to_pickle(
            dataframe: pd.DataFrame, filename: str = 'optimized_df.pkl'
    ) -> None:
        """
        Save dataframe to pickle file
        :param dataframe: dataframe
        :type dataframe: pd.DataFrame
        :param filename: name of the file
        :type filename: str
        :return: None
        :rtype: NoneType
        """
        dataframe.to_pickle(f'data/processed/{filename}')

    @staticmethod
    def load_from_pickle(filename: str = 'optimized_df.pkl') -> pd.DataFrame:
        """
        Load dataframe from Pickle file
        :param filename: name of the file to search and load
        :type filename: str
        :return: dataframe read from pickle
        :rtype: pd.DataFrame
        """
        dataframe: pd.DataFrame = pd.read_pickle(f'data/processed/{filename}')
        return dataframe
