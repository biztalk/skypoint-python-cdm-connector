from DataObject import DataObject
from MetadataObject import MetadataObjectCollection
import re

class Entity(DataObject):
    
    def __init__(self, schema=[]):
        super().__init__(schema)

    invalidEntityNameRegex = re.compile("\\.|\"")

    def validate(self):
        super().validate()
        if self.invalidEntityNameRegex.search(self.name):
            raise ValueError("%s.name cannot contain dot or quotation mark." % (self.__class__.__name__, ))


class EntityCollection(MetadataObjectCollection):
    itemType = Entity
