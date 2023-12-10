import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    df = df.pivot(index= 'id_1', columns = 'id_2', values='car').fillna(0)
    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df['car_type'] = ['low' if car <= 15 else 'medium' if car > 15 and car <= 25 else 'high' for car in df['car']]
    df = df.groupby('car_type')['car_type'].count().reset_index(name='car_type_count')
    df = df.sort_values(by='car_type')
    d = df.set_index('car_type').to_dict()
    return d


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    condition = df['bus'] > df['bus'].mean() * 2
    indices_list = df.index[condition].tolist()
    return indices_list


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    df = df.groupby('route')['truck'].mean().reset_index(name = 'average_truck')
    df = df[df['average_truck'] > 7]
    l = df['route'].tolist()
    return l

df = pd.read_csv('datasets\dataset-1.csv')
l = filter_routes(df)
print(l) 
    


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
     condition= df1>20
     new_df1=df1.where(~condition, df1*0.75, df1*1.25)
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    

    return pd.Series()
