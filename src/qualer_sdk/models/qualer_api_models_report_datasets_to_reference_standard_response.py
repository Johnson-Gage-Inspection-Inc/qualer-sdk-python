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


class QualerApiModelsReportDatasetsToReferenceStandardResponse(object):
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
        "is_auxiliary": "bool",
        "last_service_date": "datetime",
        "next_service_date": "datetime",
        "certificate_number": "str",
        "calibrated_by": "str",
        "tool_name": "str",
        "tool_site": "str",
        "tool_room": "str",
        "tool_station": "str",
        "tool_location": "str",
        "asset_tag": "str",
        "lot_number": "str",
        "asset_user": "str",
        "tool_type_name": "str",
        "tool_description": "str",
        "tool_id": "int",
        "manufacturer": "str",
        "serial_number": "str",
        "area": "str",
        "service_order_item_id": "int",
        "manufacturer_part_number": "str",
        "equipment_id": "str",
    }

    attribute_map = {
        "is_auxiliary": "IsAuxiliary",
        "last_service_date": "LastServiceDate",
        "next_service_date": "NextServiceDate",
        "certificate_number": "CertificateNumber",
        "calibrated_by": "CalibratedBy",
        "tool_name": "ToolName",
        "tool_site": "ToolSite",
        "tool_room": "ToolRoom",
        "tool_station": "ToolStation",
        "tool_location": "ToolLocation",
        "asset_tag": "AssetTag",
        "lot_number": "LotNumber",
        "asset_user": "AssetUser",
        "tool_type_name": "ToolTypeName",
        "tool_description": "ToolDescription",
        "tool_id": "ToolId",
        "manufacturer": "Manufacturer",
        "serial_number": "SerialNumber",
        "area": "Area",
        "service_order_item_id": "ServiceOrderItemId",
        "manufacturer_part_number": "ManufacturerPartNumber",
        "equipment_id": "EquipmentId",
    }

    def __init__(
        self,
        is_auxiliary=None,
        last_service_date=None,
        next_service_date=None,
        certificate_number=None,
        calibrated_by=None,
        tool_name=None,
        tool_site=None,
        tool_room=None,
        tool_station=None,
        tool_location=None,
        asset_tag=None,
        lot_number=None,
        asset_user=None,
        tool_type_name=None,
        tool_description=None,
        tool_id=None,
        manufacturer=None,
        serial_number=None,
        area=None,
        service_order_item_id=None,
        manufacturer_part_number=None,
        equipment_id=None,
        _configuration=None,
    ):  # noqa: E501
        """QualerApiModelsReportDatasetsToReferenceStandardResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_auxiliary = None
        self._last_service_date = None
        self._next_service_date = None
        self._certificate_number = None
        self._calibrated_by = None
        self._tool_name = None
        self._tool_site = None
        self._tool_room = None
        self._tool_station = None
        self._tool_location = None
        self._asset_tag = None
        self._lot_number = None
        self._asset_user = None
        self._tool_type_name = None
        self._tool_description = None
        self._tool_id = None
        self._manufacturer = None
        self._serial_number = None
        self._area = None
        self._service_order_item_id = None
        self._manufacturer_part_number = None
        self._equipment_id = None
        self.discriminator = None

        if is_auxiliary is not None:
            self.is_auxiliary = is_auxiliary
        if last_service_date is not None:
            self.last_service_date = last_service_date
        if next_service_date is not None:
            self.next_service_date = next_service_date
        if certificate_number is not None:
            self.certificate_number = certificate_number
        if calibrated_by is not None:
            self.calibrated_by = calibrated_by
        if tool_name is not None:
            self.tool_name = tool_name
        if tool_site is not None:
            self.tool_site = tool_site
        if tool_room is not None:
            self.tool_room = tool_room
        if tool_station is not None:
            self.tool_station = tool_station
        if tool_location is not None:
            self.tool_location = tool_location
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if lot_number is not None:
            self.lot_number = lot_number
        if asset_user is not None:
            self.asset_user = asset_user
        if tool_type_name is not None:
            self.tool_type_name = tool_type_name
        if tool_description is not None:
            self.tool_description = tool_description
        if tool_id is not None:
            self.tool_id = tool_id
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if serial_number is not None:
            self.serial_number = serial_number
        if area is not None:
            self.area = area
        if service_order_item_id is not None:
            self.service_order_item_id = service_order_item_id
        if manufacturer_part_number is not None:
            self.manufacturer_part_number = manufacturer_part_number
        if equipment_id is not None:
            self.equipment_id = equipment_id

    @property
    def is_auxiliary(self):
        """Gets the is_auxiliary of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The is_auxiliary of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_auxiliary

    @is_auxiliary.setter
    def is_auxiliary(self, is_auxiliary):
        """Sets the is_auxiliary of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param is_auxiliary: The is_auxiliary of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: bool
        """

        self._is_auxiliary = is_auxiliary

    @property
    def last_service_date(self):
        """Gets the last_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The last_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_service_date

    @last_service_date.setter
    def last_service_date(self, last_service_date):
        """Sets the last_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param last_service_date: The last_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: datetime
        """

        self._last_service_date = last_service_date

    @property
    def next_service_date(self):
        """Gets the next_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The next_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._next_service_date

    @next_service_date.setter
    def next_service_date(self, next_service_date):
        """Sets the next_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param next_service_date: The next_service_date of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: datetime
        """

        self._next_service_date = next_service_date

    @property
    def certificate_number(self):
        """Gets the certificate_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The certificate_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param certificate_number: The certificate_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._certificate_number = certificate_number

    @property
    def calibrated_by(self):
        """Gets the calibrated_by of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The calibrated_by of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._calibrated_by

    @calibrated_by.setter
    def calibrated_by(self, calibrated_by):
        """Sets the calibrated_by of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param calibrated_by: The calibrated_by of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._calibrated_by = calibrated_by

    @property
    def tool_name(self):
        """Gets the tool_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        """Sets the tool_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_name: The tool_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_name = tool_name

    @property
    def tool_site(self):
        """Gets the tool_site of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_site of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_site

    @tool_site.setter
    def tool_site(self, tool_site):
        """Sets the tool_site of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_site: The tool_site of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_site = tool_site

    @property
    def tool_room(self):
        """Gets the tool_room of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_room of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_room

    @tool_room.setter
    def tool_room(self, tool_room):
        """Sets the tool_room of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_room: The tool_room of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_room = tool_room

    @property
    def tool_station(self):
        """Gets the tool_station of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_station of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_station

    @tool_station.setter
    def tool_station(self, tool_station):
        """Sets the tool_station of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_station: The tool_station of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_station = tool_station

    @property
    def tool_location(self):
        """Gets the tool_location of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_location of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_location

    @tool_location.setter
    def tool_location(self, tool_location):
        """Sets the tool_location of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_location: The tool_location of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_location = tool_location

    @property
    def asset_tag(self):
        """Gets the asset_tag of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The asset_tag of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param asset_tag: The asset_tag of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def lot_number(self):
        """Gets the lot_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The lot_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._lot_number

    @lot_number.setter
    def lot_number(self, lot_number):
        """Sets the lot_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param lot_number: The lot_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._lot_number = lot_number

    @property
    def asset_user(self):
        """Gets the asset_user of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The asset_user of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._asset_user

    @asset_user.setter
    def asset_user(self, asset_user):
        """Sets the asset_user of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param asset_user: The asset_user of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._asset_user = asset_user

    @property
    def tool_type_name(self):
        """Gets the tool_type_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_type_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_type_name

    @tool_type_name.setter
    def tool_type_name(self, tool_type_name):
        """Sets the tool_type_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_type_name: The tool_type_name of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_type_name = tool_type_name

    @property
    def tool_description(self):
        """Gets the tool_description of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_description of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._tool_description

    @tool_description.setter
    def tool_description(self, tool_description):
        """Sets the tool_description of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_description: The tool_description of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._tool_description = tool_description

    @property
    def tool_id(self):
        """Gets the tool_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The tool_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: int
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """Sets the tool_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param tool_id: The tool_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: int
        """

        self._tool_id = tool_id

    @property
    def manufacturer(self):
        """Gets the manufacturer of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The manufacturer of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param manufacturer: The manufacturer of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def serial_number(self):
        """Gets the serial_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The serial_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param serial_number: The serial_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def area(self):
        """Gets the area of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The area of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param area: The area of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def service_order_item_id(self):
        """Gets the service_order_item_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The service_order_item_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: int
        """
        return self._service_order_item_id

    @service_order_item_id.setter
    def service_order_item_id(self, service_order_item_id):
        """Sets the service_order_item_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param service_order_item_id: The service_order_item_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: int
        """

        self._service_order_item_id = service_order_item_id

    @property
    def manufacturer_part_number(self):
        """Gets the manufacturer_part_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The manufacturer_part_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_part_number

    @manufacturer_part_number.setter
    def manufacturer_part_number(self, manufacturer_part_number):
        """Sets the manufacturer_part_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param manufacturer_part_number: The manufacturer_part_number of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._manufacturer_part_number = manufacturer_part_number

    @property
    def equipment_id(self):
        """Gets the equipment_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501


        :return: The equipment_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :rtype: str
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        """Sets the equipment_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.


        :param equipment_id: The equipment_id of this QualerApiModelsReportDatasetsToReferenceStandardResponse.  # noqa: E501
        :type: str
        """

        self._equipment_id = equipment_id

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
        if issubclass(QualerApiModelsReportDatasetsToReferenceStandardResponse, dict):
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
        if not isinstance(
            other, QualerApiModelsReportDatasetsToReferenceStandardResponse
        ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(
            other, QualerApiModelsReportDatasetsToReferenceStandardResponse
        ):
            return True

        return self.to_dict() != other.to_dict()
