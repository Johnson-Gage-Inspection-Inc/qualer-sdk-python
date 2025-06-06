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

from qualer_sdk.configuration import Configuration


class QualerApiModelsEmployeesFromUpdateEmployeeModel(object):
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
        "first_name": "str",
        "last_name": "str",
        "subscription_email": "str",
        "mobile_phone": "str",
        "office_phone": "str",
        "alias": "str",
        "title": "str",
        "culture_name": "str",
        "culture_ui_name": "str",
        "image_url": "str",
    }

    attribute_map = {
        "first_name": "FirstName",
        "last_name": "LastName",
        "subscription_email": "SubscriptionEmail",
        "mobile_phone": "MobilePhone",
        "office_phone": "OfficePhone",
        "alias": "Alias",
        "title": "Title",
        "culture_name": "CultureName",
        "culture_ui_name": "CultureUiName",
        "image_url": "ImageUrl",
    }

    def __init__(
        self,
        first_name=None,
        last_name=None,
        subscription_email=None,
        mobile_phone=None,
        office_phone=None,
        alias=None,
        title=None,
        culture_name=None,
        culture_ui_name=None,
        image_url=None,
        _configuration=None,
    ):  # noqa: E501
        """QualerApiModelsEmployeesFromUpdateEmployeeModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._subscription_email = None
        self._mobile_phone = None
        self._office_phone = None
        self._alias = None
        self._title = None
        self._culture_name = None
        self._culture_ui_name = None
        self._image_url = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if subscription_email is not None:
            self.subscription_email = subscription_email
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if office_phone is not None:
            self.office_phone = office_phone
        if alias is not None:
            self.alias = alias
        if title is not None:
            self.title = title
        if culture_name is not None:
            self.culture_name = culture_name
        if culture_ui_name is not None:
            self.culture_ui_name = culture_ui_name
        if image_url is not None:
            self.image_url = image_url

    @property
    def first_name(self):
        """Gets the first_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The first_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param first_name: The first_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The last_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param last_name: The last_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def subscription_email(self):
        """Gets the subscription_email of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The subscription_email of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._subscription_email

    @subscription_email.setter
    def subscription_email(self, subscription_email):
        """Sets the subscription_email of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param subscription_email: The subscription_email of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._subscription_email = subscription_email

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The mobile_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param mobile_phone: The mobile_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def office_phone(self):
        """Gets the office_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The office_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._office_phone

    @office_phone.setter
    def office_phone(self, office_phone):
        """Sets the office_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param office_phone: The office_phone of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._office_phone = office_phone

    @property
    def alias(self):
        """Gets the alias of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The alias of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param alias: The alias of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def title(self):
        """Gets the title of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The title of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param title: The title of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def culture_name(self):
        """Gets the culture_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The culture_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._culture_name

    @culture_name.setter
    def culture_name(self, culture_name):
        """Sets the culture_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param culture_name: The culture_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._culture_name = culture_name

    @property
    def culture_ui_name(self):
        """Gets the culture_ui_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The culture_ui_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._culture_ui_name

    @culture_ui_name.setter
    def culture_ui_name(self, culture_ui_name):
        """Sets the culture_ui_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param culture_ui_name: The culture_ui_name of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._culture_ui_name = culture_ui_name

    @property
    def image_url(self):
        """Gets the image_url of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501


        :return: The image_url of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this QualerApiModelsEmployeesFromUpdateEmployeeModel.


        :param image_url: The image_url of this QualerApiModelsEmployeesFromUpdateEmployeeModel.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(QualerApiModelsEmployeesFromUpdateEmployeeModel, dict):
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
        if not isinstance(other, QualerApiModelsEmployeesFromUpdateEmployeeModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualerApiModelsEmployeesFromUpdateEmployeeModel):
            return True

        return self.to_dict() != other.to_dict()
