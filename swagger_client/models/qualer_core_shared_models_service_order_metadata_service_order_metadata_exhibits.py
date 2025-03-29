# coding: utf-8

"""
    Qualer.Web.Mvc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'subtitle': 'str',
        'exhibits': 'list[QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue]'
    }

    attribute_map = {
        'title': 'Title',
        'subtitle': 'Subtitle',
        'exhibits': 'Exhibits'
    }

    def __init__(self, title=None, subtitle=None, exhibits=None):  # noqa: E501
        """QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._subtitle = None
        self._exhibits = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if subtitle is not None:
            self.subtitle = subtitle
        if exhibits is not None:
            self.exhibits = exhibits

    @property
    def title(self):
        """Gets the title of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501


        :return: The title of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.


        :param title: The title of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subtitle(self):
        """Gets the subtitle of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501


        :return: The subtitle of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.


        :param subtitle: The subtitle of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def exhibits(self):
        """Gets the exhibits of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501


        :return: The exhibits of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501
        :rtype: list[QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue]
        """
        return self._exhibits

    @exhibits.setter
    def exhibits(self, exhibits):
        """Sets the exhibits of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.


        :param exhibits: The exhibits of this QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits.  # noqa: E501
        :type: list[QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibitsKeyValue]
        """

        self._exhibits = exhibits

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QualerCoreSharedModelsServiceOrderMetadataServiceOrderMetadataExhibits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
