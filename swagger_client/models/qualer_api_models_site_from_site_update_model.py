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

class QualerApiModelsSiteFromSiteUpdateModel(object):
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
        'site_id': 'int',
        'site_name': 'str',
        'site_code': 'str',
        'shipping_inherited': 'bool',
        'default_account_representative_employee_id': 'int',
        'billing_inherited': 'bool',
        'federal_number': 'str',
        'state_number': 'str',
        'culture_name': 'str',
        'is_science_facility': 'bool',
        'is_service_center': 'bool',
        'is_inventory_storage': 'bool',
        'is_production': 'bool',
        'time_zone_id': 'str',
        'time_zone_offset_minutes': 'int',
        'company_name': 'str',
        'billing_address': 'QualerApiModelsAddressAddressModel',
        'shipping_address': 'QualerApiModelsAddressAddressModel'
    }

    attribute_map = {
        'site_id': 'SiteId',
        'site_name': 'SiteName',
        'site_code': 'SiteCode',
        'shipping_inherited': 'ShippingInherited',
        'default_account_representative_employee_id': 'DefaultAccountRepresentativeEmployeeId',
        'billing_inherited': 'BillingInherited',
        'federal_number': 'FederalNumber',
        'state_number': 'StateNumber',
        'culture_name': 'CultureName',
        'is_science_facility': 'IsScienceFacility',
        'is_service_center': 'IsServiceCenter',
        'is_inventory_storage': 'IsInventoryStorage',
        'is_production': 'IsProduction',
        'time_zone_id': 'TimeZoneId',
        'time_zone_offset_minutes': 'TimeZoneOffsetMinutes',
        'company_name': 'CompanyName',
        'billing_address': 'BillingAddress',
        'shipping_address': 'ShippingAddress'
    }

    def __init__(self, site_id=None, site_name=None, site_code=None, shipping_inherited=None, default_account_representative_employee_id=None, billing_inherited=None, federal_number=None, state_number=None, culture_name=None, is_science_facility=None, is_service_center=None, is_inventory_storage=None, is_production=None, time_zone_id=None, time_zone_offset_minutes=None, company_name=None, billing_address=None, shipping_address=None):  # noqa: E501
        """QualerApiModelsSiteFromSiteUpdateModel - a model defined in Swagger"""  # noqa: E501
        self._site_id = None
        self._site_name = None
        self._site_code = None
        self._shipping_inherited = None
        self._default_account_representative_employee_id = None
        self._billing_inherited = None
        self._federal_number = None
        self._state_number = None
        self._culture_name = None
        self._is_science_facility = None
        self._is_service_center = None
        self._is_inventory_storage = None
        self._is_production = None
        self._time_zone_id = None
        self._time_zone_offset_minutes = None
        self._company_name = None
        self._billing_address = None
        self._shipping_address = None
        self.discriminator = None
        if site_id is not None:
            self.site_id = site_id
        if site_name is not None:
            self.site_name = site_name
        if site_code is not None:
            self.site_code = site_code
        if shipping_inherited is not None:
            self.shipping_inherited = shipping_inherited
        if default_account_representative_employee_id is not None:
            self.default_account_representative_employee_id = default_account_representative_employee_id
        if billing_inherited is not None:
            self.billing_inherited = billing_inherited
        if federal_number is not None:
            self.federal_number = federal_number
        if state_number is not None:
            self.state_number = state_number
        if culture_name is not None:
            self.culture_name = culture_name
        if is_science_facility is not None:
            self.is_science_facility = is_science_facility
        if is_service_center is not None:
            self.is_service_center = is_service_center
        if is_inventory_storage is not None:
            self.is_inventory_storage = is_inventory_storage
        if is_production is not None:
            self.is_production = is_production
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if time_zone_offset_minutes is not None:
            self.time_zone_offset_minutes = time_zone_offset_minutes
        if company_name is not None:
            self.company_name = company_name
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address

    @property
    def site_id(self):
        """Gets the site_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The site_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this QualerApiModelsSiteFromSiteUpdateModel.


        :param site_id: The site_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def site_name(self):
        """Gets the site_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The site_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this QualerApiModelsSiteFromSiteUpdateModel.


        :param site_name: The site_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

    @property
    def site_code(self):
        """Gets the site_code of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The site_code of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        """Sets the site_code of this QualerApiModelsSiteFromSiteUpdateModel.


        :param site_code: The site_code of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._site_code = site_code

    @property
    def shipping_inherited(self):
        """Gets the shipping_inherited of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The shipping_inherited of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: bool
        """
        return self._shipping_inherited

    @shipping_inherited.setter
    def shipping_inherited(self, shipping_inherited):
        """Sets the shipping_inherited of this QualerApiModelsSiteFromSiteUpdateModel.


        :param shipping_inherited: The shipping_inherited of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: bool
        """

        self._shipping_inherited = shipping_inherited

    @property
    def default_account_representative_employee_id(self):
        """Gets the default_account_representative_employee_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The default_account_representative_employee_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: int
        """
        return self._default_account_representative_employee_id

    @default_account_representative_employee_id.setter
    def default_account_representative_employee_id(self, default_account_representative_employee_id):
        """Sets the default_account_representative_employee_id of this QualerApiModelsSiteFromSiteUpdateModel.


        :param default_account_representative_employee_id: The default_account_representative_employee_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: int
        """

        self._default_account_representative_employee_id = default_account_representative_employee_id

    @property
    def billing_inherited(self):
        """Gets the billing_inherited of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The billing_inherited of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: bool
        """
        return self._billing_inherited

    @billing_inherited.setter
    def billing_inherited(self, billing_inherited):
        """Sets the billing_inherited of this QualerApiModelsSiteFromSiteUpdateModel.


        :param billing_inherited: The billing_inherited of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: bool
        """

        self._billing_inherited = billing_inherited

    @property
    def federal_number(self):
        """Gets the federal_number of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The federal_number of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._federal_number

    @federal_number.setter
    def federal_number(self, federal_number):
        """Sets the federal_number of this QualerApiModelsSiteFromSiteUpdateModel.


        :param federal_number: The federal_number of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._federal_number = federal_number

    @property
    def state_number(self):
        """Gets the state_number of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The state_number of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._state_number

    @state_number.setter
    def state_number(self, state_number):
        """Sets the state_number of this QualerApiModelsSiteFromSiteUpdateModel.


        :param state_number: The state_number of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._state_number = state_number

    @property
    def culture_name(self):
        """Gets the culture_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The culture_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._culture_name

    @culture_name.setter
    def culture_name(self, culture_name):
        """Sets the culture_name of this QualerApiModelsSiteFromSiteUpdateModel.


        :param culture_name: The culture_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._culture_name = culture_name

    @property
    def is_science_facility(self):
        """Gets the is_science_facility of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The is_science_facility of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_science_facility

    @is_science_facility.setter
    def is_science_facility(self, is_science_facility):
        """Sets the is_science_facility of this QualerApiModelsSiteFromSiteUpdateModel.


        :param is_science_facility: The is_science_facility of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: bool
        """

        self._is_science_facility = is_science_facility

    @property
    def is_service_center(self):
        """Gets the is_service_center of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The is_service_center of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_service_center

    @is_service_center.setter
    def is_service_center(self, is_service_center):
        """Sets the is_service_center of this QualerApiModelsSiteFromSiteUpdateModel.


        :param is_service_center: The is_service_center of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: bool
        """

        self._is_service_center = is_service_center

    @property
    def is_inventory_storage(self):
        """Gets the is_inventory_storage of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The is_inventory_storage of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_inventory_storage

    @is_inventory_storage.setter
    def is_inventory_storage(self, is_inventory_storage):
        """Sets the is_inventory_storage of this QualerApiModelsSiteFromSiteUpdateModel.


        :param is_inventory_storage: The is_inventory_storage of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: bool
        """

        self._is_inventory_storage = is_inventory_storage

    @property
    def is_production(self):
        """Gets the is_production of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The is_production of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_production

    @is_production.setter
    def is_production(self, is_production):
        """Sets the is_production of this QualerApiModelsSiteFromSiteUpdateModel.


        :param is_production: The is_production of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: bool
        """

        self._is_production = is_production

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The time_zone_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this QualerApiModelsSiteFromSiteUpdateModel.


        :param time_zone_id: The time_zone_id of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._time_zone_id = time_zone_id

    @property
    def time_zone_offset_minutes(self):
        """Gets the time_zone_offset_minutes of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The time_zone_offset_minutes of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: int
        """
        return self._time_zone_offset_minutes

    @time_zone_offset_minutes.setter
    def time_zone_offset_minutes(self, time_zone_offset_minutes):
        """Sets the time_zone_offset_minutes of this QualerApiModelsSiteFromSiteUpdateModel.


        :param time_zone_offset_minutes: The time_zone_offset_minutes of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: int
        """

        self._time_zone_offset_minutes = time_zone_offset_minutes

    @property
    def company_name(self):
        """Gets the company_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The company_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this QualerApiModelsSiteFromSiteUpdateModel.


        :param company_name: The company_name of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def billing_address(self):
        """Gets the billing_address of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The billing_address of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: QualerApiModelsAddressAddressModel
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this QualerApiModelsSiteFromSiteUpdateModel.


        :param billing_address: The billing_address of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: QualerApiModelsAddressAddressModel
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501


        :return: The shipping_address of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :rtype: QualerApiModelsAddressAddressModel
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this QualerApiModelsSiteFromSiteUpdateModel.


        :param shipping_address: The shipping_address of this QualerApiModelsSiteFromSiteUpdateModel.  # noqa: E501
        :type: QualerApiModelsAddressAddressModel
        """

        self._shipping_address = shipping_address

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
        if issubclass(QualerApiModelsSiteFromSiteUpdateModel, dict):
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
        if not isinstance(other, QualerApiModelsSiteFromSiteUpdateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
