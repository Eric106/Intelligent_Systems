from geopy.distance import geodesic
from pandas import read_csv

def get_distance_matrix(fileNameCSV):
    df_lat_long = read_csv(fileNameCSV,index_col=0)
    df_distance_matrix = df_lat_long
    df_distance_matrix = df_distance_matrix.drop(columns=df_lat_long.columns.tolist())
    dictLatLong = df_lat_long.to_dict()
    for cityX in df_lat_long.index.tolist():
        tempColInfo = []
        ct1 = (round(dictLatLong['Latitud'][cityX],6),round(dictLatLong['Longitud'][cityX],6))
        for cityY in df_lat_long.index.tolist():
            ct2 = (round(dictLatLong['Latitud'][cityY],6),round(dictLatLong['Longitud'][cityY],6))
            tempColInfo.append(int(geodesic(ct1,ct2).km))
        df_distance_matrix[cityX] = tempColInfo
    return df_distance_matrix