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

class QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel(object):
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
        'measurement_tool_id': 'int',
        'last_service_date': 'datetime',
        'next_service_date': 'datetime',
        'calibrated_by': 'str',
        'certificate_number': 'str',
        'tool_name': 'str',
        'tool_description': 'str',
        'manufacturer': 'str',
        'manufacturer_part_number': 'str',
        'serial_number': 'str',
        'asset_tag': 'str',
        'asset_user': 'str',
        'equipment_id': 'str'
    }

    attribute_map = {
        'measurement_tool_id': 'MeasurementToolId',
        'last_service_date': 'LastServiceDate',
        'next_service_date': 'NextServiceDate',
        'calibrated_by': 'CalibratedBy',
        'certificate_number': 'CertificateNumber',
        'tool_name': 'ToolName',
        'tool_description': 'ToolDescription',
        'manufacturer': 'Manufacturer',
        'manufacturer_part_number': 'ManufacturerPartNumber',
        'serial_number': 'SerialNumber',
        'asset_tag': 'AssetTag',
        'asset_user': 'AssetUser',
        'equipment_id': 'EquipmentId'
    }

    def __init__(self, measurement_tool_id=None, last_service_date=None, next_service_date=None, calibrated_by=None, certificate_number=None, tool_name=None, tool_description=None, manufacturer=None, manufacturer_part_number=None, serial_number=None, asset_tag=None, asset_user=None, equipment_id=None):  # noqa: E501
        """QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel - a model defined in Swagger"""  # noqa: E501
        self._measurement_tool_id = None
        self._last_service_date = None
        self._next_service_date = None
        self._calibrated_by = None
        self._certificate_number = None
        self._tool_name = None
        self._tool_description = None
        self._manufacturer = None
        self._manufacturer_part_number = None
        self._serial_number = None
        self._asset_tag = None
        self._asset_user = None
        self._equipment_id = None
        self.discriminator = None
        if measurement_tool_id is not None:
            self.measurement_tool_id = measurement_tool_id
        if last_service_date is not None:
            self.last_service_date = last_service_date
        if next_service_date is not None:
            self.next_service_date = next_service_date
        if calibrated_by is not None:
            self.calibrated_by = calibrated_by
        if certificate_number is not None:
            self.certificate_number = certificate_number
        if tool_name is not None:
            self.tool_name = tool_name
        if tool_description is not None:
            self.tool_description = tool_description
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if manufacturer_part_number is not None:
            self.manufacturer_part_number = manufacturer_part_number
        if serial_number is not None:
            self.serial_number = serial_number
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if asset_user is not None:
            self.asset_user = asset_user
        if equipment_id is not None:
            self.equipment_id = equipment_id

    @property
    def measurement_tool_id(self):
        """Gets the measurement_tool_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The measurement_tool_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._measurement_tool_id

    @measurement_tool_id.setter
    def measurement_tool_id(self, measurement_tool_id):
        """Sets the measurement_tool_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param measurement_tool_id: The measurement_tool_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: int
        """

        self._measurement_tool_id = measurement_tool_id

    @property
    def last_service_date(self):
        """Gets the last_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The last_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_service_date

    @last_service_date.setter
    def last_service_date(self, last_service_date):
        """Sets the last_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param last_service_date: The last_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: datetime
        """

        self._last_service_date = last_service_date

    @property
    def next_service_date(self):
        """Gets the next_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The next_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._next_service_date

    @next_service_date.setter
    def next_service_date(self, next_service_date):
        """Sets the next_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param next_service_date: The next_service_date of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: datetime
        """

        self._next_service_date = next_service_date

    @property
    def calibrated_by(self):
        """Gets the calibrated_by of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The calibrated_by of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._calibrated_by

    @calibrated_by.setter
    def calibrated_by(self, calibrated_by):
        """Sets the calibrated_by of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param calibrated_by: The calibrated_by of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._calibrated_by = calibrated_by

    @property
    def certificate_number(self):
        """Gets the certificate_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The certificate_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param certificate_number: The certificate_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._certificate_number = certificate_number

    @property
    def tool_name(self):
        """Gets the tool_name of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The tool_name of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name):
        """Sets the tool_name of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param tool_name: The tool_name of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._tool_name = tool_name

    @property
    def tool_description(self):
        """Gets the tool_description of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The tool_description of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._tool_description

    @tool_description.setter
    def tool_description(self, tool_description):
        """Sets the tool_description of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param tool_description: The tool_description of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._tool_description = tool_description

    @property
    def manufacturer(self):
        """Gets the manufacturer of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The manufacturer of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param manufacturer: The manufacturer of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def manufacturer_part_number(self):
        """Gets the manufacturer_part_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The manufacturer_part_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_part_number

    @manufacturer_part_number.setter
    def manufacturer_part_number(self, manufacturer_part_number):
        """Sets the manufacturer_part_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param manufacturer_part_number: The manufacturer_part_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._manufacturer_part_number = manufacturer_part_number

    @property
    def serial_number(self):
        """Gets the serial_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The serial_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param serial_number: The serial_number of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def asset_tag(self):
        """Gets the asset_tag of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The asset_tag of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param asset_tag: The asset_tag of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def asset_user(self):
        """Gets the asset_user of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The asset_user of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_user

    @asset_user.setter
    def asset_user(self, asset_user):
        """Sets the asset_user of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param asset_user: The asset_user of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_user = asset_user

    @property
    def equipment_id(self):
        """Gets the equipment_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501


        :return: The equipment_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        """Sets the equipment_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.


        :param equipment_id: The equipment_id of this QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel.  # noqa: E501
        :type: str
        """

        self._equipment_id = equipment_id

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
        if issubclass(QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel, dict):
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
        if not isinstance(other, QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
