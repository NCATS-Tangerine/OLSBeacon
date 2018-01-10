# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.concept_detail import ConceptDetail  # noqa: F401,E501
from swagger_server import util


class ConceptWithDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, semantic_group: str=None, synonyms: List[str]=None, definition: str=None, details: List[ConceptDetail]=None):  # noqa: E501
        """ConceptWithDetails - a model defined in Swagger

        :param id: The id of this ConceptWithDetails.  # noqa: E501
        :type id: str
        :param name: The name of this ConceptWithDetails.  # noqa: E501
        :type name: str
        :param semantic_group: The semantic_group of this ConceptWithDetails.  # noqa: E501
        :type semantic_group: str
        :param synonyms: The synonyms of this ConceptWithDetails.  # noqa: E501
        :type synonyms: List[str]
        :param definition: The definition of this ConceptWithDetails.  # noqa: E501
        :type definition: str
        :param details: The details of this ConceptWithDetails.  # noqa: E501
        :type details: List[ConceptDetail]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'semantic_group': str,
            'synonyms': List[str],
            'definition': str,
            'details': List[ConceptDetail]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'semantic_group': 'semanticGroup',
            'synonyms': 'synonyms',
            'definition': 'definition',
            'details': 'details'
        }

        self._id = id
        self._name = name
        self._semantic_group = semantic_group
        self._synonyms = synonyms
        self._definition = definition
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'ConceptWithDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConceptWithDetails of this ConceptWithDetails.  # noqa: E501
        :rtype: ConceptWithDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ConceptWithDetails.

        local object identifier for the concept in the specified knowledge source database   # noqa: E501

        :return: The id of this ConceptWithDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ConceptWithDetails.

        local object identifier for the concept in the specified knowledge source database   # noqa: E501

        :param id: The id of this ConceptWithDetails.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this ConceptWithDetails.

        canonical human readable name of the concept   # noqa: E501

        :return: The name of this ConceptWithDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ConceptWithDetails.

        canonical human readable name of the concept   # noqa: E501

        :param name: The name of this ConceptWithDetails.
        :type name: str
        """

        self._name = name

    @property
    def semantic_group(self) -> str:
        """Gets the semantic_group of this ConceptWithDetails.

        concept semantic type   # noqa: E501

        :return: The semantic_group of this ConceptWithDetails.
        :rtype: str
        """
        return self._semantic_group

    @semantic_group.setter
    def semantic_group(self, semantic_group: str):
        """Sets the semantic_group of this ConceptWithDetails.

        concept semantic type   # noqa: E501

        :param semantic_group: The semantic_group of this ConceptWithDetails.
        :type semantic_group: str
        """

        self._semantic_group = semantic_group

    @property
    def synonyms(self) -> List[str]:
        """Gets the synonyms of this ConceptWithDetails.

        list of synonyms for concept   # noqa: E501

        :return: The synonyms of this ConceptWithDetails.
        :rtype: List[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms: List[str]):
        """Sets the synonyms of this ConceptWithDetails.

        list of synonyms for concept   # noqa: E501

        :param synonyms: The synonyms of this ConceptWithDetails.
        :type synonyms: List[str]
        """

        self._synonyms = synonyms

    @property
    def definition(self) -> str:
        """Gets the definition of this ConceptWithDetails.

        concept definition   # noqa: E501

        :return: The definition of this ConceptWithDetails.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition: str):
        """Sets the definition of this ConceptWithDetails.

        concept definition   # noqa: E501

        :param definition: The definition of this ConceptWithDetails.
        :type definition: str
        """

        self._definition = definition

    @property
    def details(self) -> List[ConceptDetail]:
        """Gets the details of this ConceptWithDetails.


        :return: The details of this ConceptWithDetails.
        :rtype: List[ConceptDetail]
        """
        return self._details

    @details.setter
    def details(self, details: List[ConceptDetail]):
        """Sets the details of this ConceptWithDetails.


        :param details: The details of this ConceptWithDetails.
        :type details: List[ConceptDetail]
        """

        self._details = details