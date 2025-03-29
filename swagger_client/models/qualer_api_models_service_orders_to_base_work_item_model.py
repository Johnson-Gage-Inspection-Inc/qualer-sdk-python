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

class QualerApiModelsServiceOrdersToBaseWorkItemModel(object):
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
        'tasks': 'list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel]',
        'parts': 'list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel]',
        'repairs': 'list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel]',
        'work_item_id': 'int',
        'vendor_tag': 'str'
    }

    attribute_map = {
        'tasks': 'Tasks',
        'parts': 'Parts',
        'repairs': 'Repairs',
        'work_item_id': 'WorkItemId',
        'vendor_tag': 'VendorTag'
    }

    def __init__(self, tasks=None, parts=None, repairs=None, work_item_id=None, vendor_tag=None):  # noqa: E501
        """QualerApiModelsServiceOrdersToBaseWorkItemModel - a model defined in Swagger"""  # noqa: E501
        self._tasks = None
        self._parts = None
        self._repairs = None
        self._work_item_id = None
        self._vendor_tag = None
        self.discriminator = None
        if tasks is not None:
            self.tasks = tasks
        if parts is not None:
            self.parts = parts
        if repairs is not None:
            self.repairs = repairs
        if work_item_id is not None:
            self.work_item_id = work_item_id
        if vendor_tag is not None:
            self.vendor_tag = vendor_tag

    @property
    def tasks(self):
        """Gets the tasks of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501


        :return: The tasks of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :rtype: list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this QualerApiModelsServiceOrdersToBaseWorkItemModel.


        :param tasks: The tasks of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :type: list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderItemTaskPriceModel]
        """

        self._tasks = tasks

    @property
    def parts(self):
        """Gets the parts of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501


        :return: The parts of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :rtype: list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this QualerApiModelsServiceOrdersToBaseWorkItemModel.


        :param parts: The parts of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :type: list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel]
        """

        self._parts = parts

    @property
    def repairs(self):
        """Gets the repairs of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501


        :return: The repairs of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :rtype: list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel]
        """
        return self._repairs

    @repairs.setter
    def repairs(self, repairs):
        """Sets the repairs of this QualerApiModelsServiceOrdersToBaseWorkItemModel.


        :param repairs: The repairs of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :type: list[QualerApiModelsServiceOrdersToBaseWorkItemModelOrderPartRepairPriceModel]
        """

        self._repairs = repairs

    @property
    def work_item_id(self):
        """Gets the work_item_id of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501


        :return: The work_item_id of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :rtype: int
        """
        return self._work_item_id

    @work_item_id.setter
    def work_item_id(self, work_item_id):
        """Sets the work_item_id of this QualerApiModelsServiceOrdersToBaseWorkItemModel.


        :param work_item_id: The work_item_id of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :type: int
        """

        self._work_item_id = work_item_id

    @property
    def vendor_tag(self):
        """Gets the vendor_tag of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501


        :return: The vendor_tag of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :rtype: str
        """
        return self._vendor_tag

    @vendor_tag.setter
    def vendor_tag(self, vendor_tag):
        """Sets the vendor_tag of this QualerApiModelsServiceOrdersToBaseWorkItemModel.


        :param vendor_tag: The vendor_tag of this QualerApiModelsServiceOrdersToBaseWorkItemModel.  # noqa: E501
        :type: str
        """

        self._vendor_tag = vendor_tag

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
        if issubclass(QualerApiModelsServiceOrdersToBaseWorkItemModel, dict):
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
        if not isinstance(other, QualerApiModelsServiceOrdersToBaseWorkItemModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
