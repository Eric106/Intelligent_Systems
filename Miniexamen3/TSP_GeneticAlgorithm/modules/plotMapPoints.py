from folium import Map, Marker, Icon, PolyLine

def get_mex_map():
    m = Map(
        location=[23.0676883,-104.7929726],
        zoom_start=5
    )
    return m

def set_locations_mex(locationsDict,htmlFileName):
    mexMap = get_mex_map()
    for key in locationsDict.keys():
        if list(locationsDict.keys())[0] == key:
            Marker(locationsDict[key],popup='<b>'+key.split('=> ')[1]+'</b>',
            tooltip=key, icon=Icon(color='green')).add_to(mexMap)
        elif list(locationsDict.keys())[-1] == key:
            Marker(locationsDict[key],popup='<b>'+key.split('=> ')[1]+'</b>',
            tooltip=key, icon=Icon(color='red')).add_to(mexMap)
        else:
            Marker(locationsDict[key], popup='<b>'+key.split('=> ')[1]+'</b>',
                   tooltip=key).add_to(mexMap)
    PolyLine(list(locationsDict.values()),color="red", weight=2.5, opacity=1).add_to(mexMap)
    mexMap.save(htmlFileName)
