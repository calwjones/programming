class RunTravelAgent:
    h1 =  Holiday("Bermuda", 2, 800)
    h2 =  Holiday("Hull", 14, 8)
    h3 =  Holiday("Los Angeles", 12, 2100)

    t1 = TravelAgent("CheapAsChips", "MA99 1CU")

    t1.addHoliday(h1)
    t1.addHoliday(h2)
    t1.addHoliday(h3)

    t2 = TravelAgent("Shoe String Tours", "CO33 2DX")

    print(t1)

    print("h3 Duration= "+str(h3.getDuration())+" days & Cost= "+str(h3.getCost()))
    print("t2 "+str(t2.getName())+" "+ str(t2.getPostcode()))