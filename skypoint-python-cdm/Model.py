from DataObject import DataObject
from SchemaEntry import SchemaEntry
from Entity import EntityCollection
from LocalEntity import LocalEntity
from Annotation import AnnotationCollection
from Relationship import RelationshipCollection
from SingleKeyRelationship import SingleKeyRelationship
from Reference import ReferenceCollection
from Attribute import Attribute
from Annotation import Annotation
from AttributeReference import AttributeReference
from datetime import datetime
from utils import String
import utils
import json
import pprint
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


class Model(DataObject):
    
    def __init__(self, from_json=False, json=None, 
                        application=config['DEFAULT']['application'], 
                        name=config['DEFAULT']['name'], 
                        description=config['DEFAULT']['description'], 
                        version=config['DEFAULT']['version'],
                        culture=None,
                        modified_time=None):

        if from_json:
            raise NotImplementedError("Not Implemented")
        else:
            self.schema = [
                SchemaEntry("application", String),
                SchemaEntry("name", String),
                SchemaEntry("description", String),
                SchemaEntry("version", String),
                SchemaEntry("culture", String),
                SchemaEntry("modifiedTime", String),
                SchemaEntry("isHidden", bool),
                SchemaEntry("entities", EntityCollection),
                SchemaEntry("annotations", AnnotationCollection),
                SchemaEntry("relationships", RelationshipCollection),
                SchemaEntry("referenceModels", ReferenceCollection)
            ]
            super().__init__(self.schema)

            self.application = application
            self.name = name
            self.description = description
            self.version = version
            self.culture = culture
            self.modifiedTime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')


    def add_entity(self, entity):
        for entity_index in range(len(self.entities)):
            if self.entities[entity_index].name.lower() == entity.name.lower():
                self.entities[entity_index] = entity
                break
        else:
            self.entities.append(entity)

    def add_relationship(self, from_attribute_entity_name, from_attribute_attribute_name,
                               to_attribute_entity_name, to_attribute_attribute_name):
        from_attribute = AttributeReference()
        from_attribute.entityName = from_attribute_entity_name
        from_attribute.attributeName = from_attribute_attribute_name

        to_attribute = AttributeReference()
        to_attribute.entityName = to_attribute_entity_name
        to_attribute.attributeName = to_attribute_attribute_name

        relationship = SingleKeyRelationship()
        relationship.fromAttribute = from_attribute
        relationship.toAttribute = to_attribute
        
        self.relationships.append(relationship)

    @staticmethod
    def generate_entity(dataframe, name, description=None, dtype_converter=None):
        entity = LocalEntity()
        entity.name = name
        entity.description = description

        if dtype_converter is None:
            dtype_converter = utils.dtype_converter

        for column_name, column_datatype in (dataframe.dtypes).items():
            attribute = Attribute()
            attribute.name = column_name
            attribute.dataType = dtype_converter.get(column_datatype, 'string')
            entity.attributes.append(attribute)
        return entity

    @staticmethod
    def add_annotation(name, value, obj):
        """
        Annotations can be added at root level (model.json),
        entity level or attribute level.
        obj is an object in which if "annotations" is present
        then new annotation will be added.
        """
        annotation = Annotation()
        annotation.name = name
        annotation.value = value
        obj.annotations.append(annotation)
        return True


    def print(self):
        pprint.pprint(self.entities)

    def toJson(self):
        result = dict()
        result["application"] = self.application
        result["name"] = self.name
        result["description"] = self.description
        result["version"] = self.version
        result["culture"] = self.culture
        result["modifiedTime"] = self.modifiedTime
        result["isHidden"] = self.isHidden
        result["entities"] = self.entities.toJson()
        result["annotations"] = self.annotations.toJson()
        result["relationships"] = self.relationships.toJson()
        result["referenceModels"] = self.referenceModels.toJson()
        return json.dumps(result)

