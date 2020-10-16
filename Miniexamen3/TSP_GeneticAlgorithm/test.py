from pandas import read_csv
from modules import GenAlg, distanceCalc, plotMapPoints

df_lat_long = read_csv("locationsMX.csv",index_col=0)
latLongDict = df_lat_long.to_dict()
print(df_lat_long)
distanceMatrix = distanceCalc.get_distance_matrix("locationsMX.csv")

ordered_cities_dict = GenAlg.solve_TSP(distanceMatrix, latLongDict)
# ordered_cities_dict = {'1 => Durango': [24.578335, -107.086384], '2 => Culicán': [24.804901, -107.493355], '3 => La Paz': [24.116421, -110.372768], '4 => Hermosillo': [29.1026, -110.97732], '5 => Mexicali': [32.62781, -115.45446], '6 => Chihuahua': [28.63528, -106.08889], '7 => Saltillo': [25.42321, -101.0053], '8 => San Luis': [22.14982, -100.97916], '9 => Pachuca': [20.082506, -98.826819], '10 => Xalapa': [19.542036, -96.954949], '11 => Campeche': [19.830558, -90.614858], '12 => Mérida': [20.97537, -89.61696], '13 => Chetumal': [18.522157, -88.339799], '14 => Villahermosa': [17.992517, -93.023162], '15 => Tuxtla Gutiérrez': [16.745986, -93.199611], '16 => Oaxaca': [17.081286, -96.805773], '17 => Chilpancingo': [17.547698, -99.567457], '18 => Cuernavaca': [18.931869, -99.310606], '19 => Toluca': [19.294099, -99.701255], '20 => Querétaro': [20.612123, -100.480258], '21 => Aguascalientes': [21.88572, -102.361341], '22 => Zacatecas': [23.067688, -104.792973], '23 => Tepic': [21.500971, -104.946946], '24 => Colima': [19.240044, -103.763627], '25 => Guadalajara': [20.66682, -103.39182], '26 => Guanajuato': [21.025104, -101.2929], '27 => Morelia': [19.70078, -101.18443], '28 => Ciudad de México': [19.42847, -99.12766], '29 => Tlaxcala': [19.416135, -98.727453], '30 => Puebla': [19.03793, -98.20346], '31 => Ciudad Victoria': [23.740981, -99.213379], '32 => Monterrey': [25.67507, -100.31847]}
plotMapPoints.set_locations_mex(ordered_cities_dict,"index.html")
