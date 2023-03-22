"""
Analysis package initialization
"""
import logging
import pandas as pd
from analysis.analysis import analyze_dataframe, find_missing_values
from analysis.visualization import plot_count, plot_distribution, \
    boxplot_dist, plot_scatter, plot_heatmap

logger: logging.Logger = logging.getLogger(__name__)


def numerical_eda(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    EDA based on numerical values for dataset
    :param dataframe: Dataframe to analyze
    :type dataframe: pd.DataFrame
    :return: The dataframe without missing values
    :rtype: pd.DataFrame
    """
    logger.info("Running Exploratory Data Analysis")
    analyze_dataframe(dataframe)
    dataframe = find_missing_values(dataframe)
    return dataframe


def visualize_data(dataframe: pd.DataFrame) -> None:
    """
    Basic visualization of the dataframe
    :param dataframe: Dataframe to visualize
    :type dataframe: pd.DataFrame
    :return: None
    :rtype: NoneType
    """
    logger.info("Running visualization")
    plot_heatmap(dataframe)
    plot_scatter(dataframe, 'bill_length_mm', 'bill_depth_mm', 'species')
    plot_scatter(dataframe, 'bill_length_mm', 'bill_depth_mm', 'sex')
    plot_scatter(dataframe, 'flipper_length_mm', 'body_mass_g', 'species')
    plot_count(dataframe, ['species'], 'island')
    plot_count(dataframe, ['species'], 'year')
    plot_distribution(dataframe['bill_length_mm'], 'lightskyblue')
    plot_distribution(dataframe['bill_length_mm'], 'coral')
    plot_distribution(dataframe['bill_length_mm'], 'palegreen')
    plot_distribution(dataframe['bill_length_mm'], 'lightskyblue')
    boxplot_dist(dataframe, 'bill_length_mm', 'bill_depth_mm', 'species')
    boxplot_dist(dataframe, 'bill_length_mm', 'bill_depth_mm', 'sex')
