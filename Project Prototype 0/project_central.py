from DublinBusAPIs import bus_location_finder

information_from_bus_finder = bus_location_finder.main('2042', '46A')
#print(information_from_bus_finder)
counter_bus = 1
for i in information_from_bus_finder:
    print('Bus number', counter_bus)
    for j in i:
        print(j)
    counter_bus += 1
