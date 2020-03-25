from Model import Model
import pandas as pd
from datetime import datetime


if __name__ == "__main__":
    m = Model()
    m.print()

    df = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98],
       "currentTime": [datetime.now(), datetime.now(), datetime.now(), datetime.now(), datetime.now()] }
    df = pd.DataFrame(df)


    df2 = {"countryAA": ["AAA", "NNN", "UUU", "BBB", "HHH AAA"],
       "populationBB": [200.4, 143.5, 1252, 1357, 52.98],
       "currentTimeCC": [datetime.now(), datetime.now(), datetime.now(), datetime.now(), datetime.now()] }
    df2 = pd.DataFrame(df2)    

    entity = Model.generate_entity(df, "customEntity")
    m.add_entity(entity)
    entity3 = Model.generate_entity(df2, "customEntity3")
    m.add_entity(entity3)

    Model.add_annotation("modelJsonAnnotation", "modelJsonAnnotationValue", m)
    Model.add_annotation("annotationName", "annotationValue", entity3)
    Model.add_annotation("annotationName2", "annotationValue2", entity3.attributes[1])

    m.add_relationship("PeopleFromCalifornia", "skypointId", "Profile", "skypointId")

    x = m.toJson()
    with open("foo.json", "w") as f:
        f.write(x)

    print(entity.name)
