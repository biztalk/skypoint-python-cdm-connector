from Base import Base
from ObjectCollection import ObjectCollection


class Relationship(Base):
    def __init__(self, schema=[]):
        super().__init__(schema)



class RelationshipCollection(ObjectCollection):
    itemType = Relationship
