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

class QualerApiModelsMeasurementsToMeasurementRecordResponseModel(object):
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
        'service_order_id': 'int',
        'service_order_number': 'int',
        'custom_order_number': 'str',
        'order_item_number': 'int',
        'certificate_number': 'str',
        'result_status': 'str',
        'as_found_result': 'str',
        'as_left_result': 'str',
        'service_date': 'datetime',
        'serial_number': 'str',
        'asset_tag': 'str',
        'asset_user': 'str',
        'asset_tag_change': 'str',
        'asset_user_change': 'str',
        'service_notes': 'str',
        'serial_number_change': 'str',
        'due_date': 'datetime',
        'next_service_date': 'datetime',
        'service_level': 'str',
        'service_level_code': 'str',
        'next_service_level': 'str',
        'next_service_level_code': 'str',
        'asset_name': 'str',
        'asset_description': 'str',
        'parts_charge': 'float',
        'parts_charge_before_discount': 'float',
        'service_charge': 'float',
        'repairs_charge': 'float',
        'segment_name': 'str',
        'schedule_name': 'str',
        'service_schedule_segment_id': 'int',
        'forward_next_service': 'bool',
        'forward_segment_id': 'int',
        'measurement_batches': 'list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModel]'
    }

    attribute_map = {
        'service_order_id': 'ServiceOrderId',
        'service_order_number': 'ServiceOrderNumber',
        'custom_order_number': 'CustomOrderNumber',
        'order_item_number': 'OrderItemNumber',
        'certificate_number': 'CertificateNumber',
        'result_status': 'ResultStatus',
        'as_found_result': 'AsFoundResult',
        'as_left_result': 'AsLeftResult',
        'service_date': 'ServiceDate',
        'serial_number': 'SerialNumber',
        'asset_tag': 'AssetTag',
        'asset_user': 'AssetUser',
        'asset_tag_change': 'AssetTagChange',
        'asset_user_change': 'AssetUserChange',
        'service_notes': 'ServiceNotes',
        'serial_number_change': 'SerialNumberChange',
        'due_date': 'DueDate',
        'next_service_date': 'NextServiceDate',
        'service_level': 'ServiceLevel',
        'service_level_code': 'ServiceLevelCode',
        'next_service_level': 'NextServiceLevel',
        'next_service_level_code': 'NextServiceLevelCode',
        'asset_name': 'AssetName',
        'asset_description': 'AssetDescription',
        'parts_charge': 'PartsCharge',
        'parts_charge_before_discount': 'PartsChargeBeforeDiscount',
        'service_charge': 'ServiceCharge',
        'repairs_charge': 'RepairsCharge',
        'segment_name': 'SegmentName',
        'schedule_name': 'ScheduleName',
        'service_schedule_segment_id': 'ServiceScheduleSegmentId',
        'forward_next_service': 'ForwardNextService',
        'forward_segment_id': 'ForwardSegmentId',
        'measurement_batches': 'MeasurementBatches'
    }

    def __init__(self, service_order_id=None, service_order_number=None, custom_order_number=None, order_item_number=None, certificate_number=None, result_status=None, as_found_result=None, as_left_result=None, service_date=None, serial_number=None, asset_tag=None, asset_user=None, asset_tag_change=None, asset_user_change=None, service_notes=None, serial_number_change=None, due_date=None, next_service_date=None, service_level=None, service_level_code=None, next_service_level=None, next_service_level_code=None, asset_name=None, asset_description=None, parts_charge=None, parts_charge_before_discount=None, service_charge=None, repairs_charge=None, segment_name=None, schedule_name=None, service_schedule_segment_id=None, forward_next_service=None, forward_segment_id=None, measurement_batches=None):  # noqa: E501
        """QualerApiModelsMeasurementsToMeasurementRecordResponseModel - a model defined in Swagger"""  # noqa: E501
        self._service_order_id = None
        self._service_order_number = None
        self._custom_order_number = None
        self._order_item_number = None
        self._certificate_number = None
        self._result_status = None
        self._as_found_result = None
        self._as_left_result = None
        self._service_date = None
        self._serial_number = None
        self._asset_tag = None
        self._asset_user = None
        self._asset_tag_change = None
        self._asset_user_change = None
        self._service_notes = None
        self._serial_number_change = None
        self._due_date = None
        self._next_service_date = None
        self._service_level = None
        self._service_level_code = None
        self._next_service_level = None
        self._next_service_level_code = None
        self._asset_name = None
        self._asset_description = None
        self._parts_charge = None
        self._parts_charge_before_discount = None
        self._service_charge = None
        self._repairs_charge = None
        self._segment_name = None
        self._schedule_name = None
        self._service_schedule_segment_id = None
        self._forward_next_service = None
        self._forward_segment_id = None
        self._measurement_batches = None
        self.discriminator = None
        if service_order_id is not None:
            self.service_order_id = service_order_id
        if service_order_number is not None:
            self.service_order_number = service_order_number
        if custom_order_number is not None:
            self.custom_order_number = custom_order_number
        if order_item_number is not None:
            self.order_item_number = order_item_number
        if certificate_number is not None:
            self.certificate_number = certificate_number
        if result_status is not None:
            self.result_status = result_status
        if as_found_result is not None:
            self.as_found_result = as_found_result
        if as_left_result is not None:
            self.as_left_result = as_left_result
        if service_date is not None:
            self.service_date = service_date
        if serial_number is not None:
            self.serial_number = serial_number
        if asset_tag is not None:
            self.asset_tag = asset_tag
        if asset_user is not None:
            self.asset_user = asset_user
        if asset_tag_change is not None:
            self.asset_tag_change = asset_tag_change
        if asset_user_change is not None:
            self.asset_user_change = asset_user_change
        if service_notes is not None:
            self.service_notes = service_notes
        if serial_number_change is not None:
            self.serial_number_change = serial_number_change
        if due_date is not None:
            self.due_date = due_date
        if next_service_date is not None:
            self.next_service_date = next_service_date
        if service_level is not None:
            self.service_level = service_level
        if service_level_code is not None:
            self.service_level_code = service_level_code
        if next_service_level is not None:
            self.next_service_level = next_service_level
        if next_service_level_code is not None:
            self.next_service_level_code = next_service_level_code
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_description is not None:
            self.asset_description = asset_description
        if parts_charge is not None:
            self.parts_charge = parts_charge
        if parts_charge_before_discount is not None:
            self.parts_charge_before_discount = parts_charge_before_discount
        if service_charge is not None:
            self.service_charge = service_charge
        if repairs_charge is not None:
            self.repairs_charge = repairs_charge
        if segment_name is not None:
            self.segment_name = segment_name
        if schedule_name is not None:
            self.schedule_name = schedule_name
        if service_schedule_segment_id is not None:
            self.service_schedule_segment_id = service_schedule_segment_id
        if forward_next_service is not None:
            self.forward_next_service = forward_next_service
        if forward_segment_id is not None:
            self.forward_segment_id = forward_segment_id
        if measurement_batches is not None:
            self.measurement_batches = measurement_batches

    @property
    def service_order_id(self):
        """Gets the service_order_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_order_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_order_id

    @service_order_id.setter
    def service_order_id(self, service_order_id):
        """Sets the service_order_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_order_id: The service_order_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: int
        """

        self._service_order_id = service_order_id

    @property
    def service_order_number(self):
        """Gets the service_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_order_number

    @service_order_number.setter
    def service_order_number(self, service_order_number):
        """Sets the service_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_order_number: The service_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: int
        """

        self._service_order_number = service_order_number

    @property
    def custom_order_number(self):
        """Gets the custom_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The custom_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._custom_order_number

    @custom_order_number.setter
    def custom_order_number(self, custom_order_number):
        """Sets the custom_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param custom_order_number: The custom_order_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._custom_order_number = custom_order_number

    @property
    def order_item_number(self):
        """Gets the order_item_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The order_item_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._order_item_number

    @order_item_number.setter
    def order_item_number(self, order_item_number):
        """Sets the order_item_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param order_item_number: The order_item_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: int
        """

        self._order_item_number = order_item_number

    @property
    def certificate_number(self):
        """Gets the certificate_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The certificate_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param certificate_number: The certificate_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._certificate_number = certificate_number

    @property
    def result_status(self):
        """Gets the result_status of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The result_status of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._result_status

    @result_status.setter
    def result_status(self, result_status):
        """Sets the result_status of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param result_status: The result_status of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._result_status = result_status

    @property
    def as_found_result(self):
        """Gets the as_found_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The as_found_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._as_found_result

    @as_found_result.setter
    def as_found_result(self, as_found_result):
        """Sets the as_found_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param as_found_result: The as_found_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._as_found_result = as_found_result

    @property
    def as_left_result(self):
        """Gets the as_left_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The as_left_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._as_left_result

    @as_left_result.setter
    def as_left_result(self, as_left_result):
        """Sets the as_left_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param as_left_result: The as_left_result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._as_left_result = as_left_result

    @property
    def service_date(self):
        """Gets the service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._service_date

    @service_date.setter
    def service_date(self, service_date):
        """Sets the service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_date: The service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: datetime
        """

        self._service_date = service_date

    @property
    def serial_number(self):
        """Gets the serial_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The serial_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param serial_number: The serial_number of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def asset_tag(self):
        """Gets the asset_tag of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The asset_tag of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param asset_tag: The asset_tag of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_tag = asset_tag

    @property
    def asset_user(self):
        """Gets the asset_user of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The asset_user of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_user

    @asset_user.setter
    def asset_user(self, asset_user):
        """Sets the asset_user of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param asset_user: The asset_user of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_user = asset_user

    @property
    def asset_tag_change(self):
        """Gets the asset_tag_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The asset_tag_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag_change

    @asset_tag_change.setter
    def asset_tag_change(self, asset_tag_change):
        """Sets the asset_tag_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param asset_tag_change: The asset_tag_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_tag_change = asset_tag_change

    @property
    def asset_user_change(self):
        """Gets the asset_user_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The asset_user_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_user_change

    @asset_user_change.setter
    def asset_user_change(self, asset_user_change):
        """Sets the asset_user_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param asset_user_change: The asset_user_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_user_change = asset_user_change

    @property
    def service_notes(self):
        """Gets the service_notes of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_notes of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._service_notes

    @service_notes.setter
    def service_notes(self, service_notes):
        """Sets the service_notes of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_notes: The service_notes of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._service_notes = service_notes

    @property
    def serial_number_change(self):
        """Gets the serial_number_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The serial_number_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._serial_number_change

    @serial_number_change.setter
    def serial_number_change(self, serial_number_change):
        """Sets the serial_number_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param serial_number_change: The serial_number_change of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._serial_number_change = serial_number_change

    @property
    def due_date(self):
        """Gets the due_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The due_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param due_date: The due_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def next_service_date(self):
        """Gets the next_service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The next_service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._next_service_date

    @next_service_date.setter
    def next_service_date(self, next_service_date):
        """Sets the next_service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param next_service_date: The next_service_date of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: datetime
        """

        self._next_service_date = next_service_date

    @property
    def service_level(self):
        """Gets the service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level):
        """Sets the service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_level: The service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._service_level = service_level

    @property
    def service_level_code(self):
        """Gets the service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._service_level_code

    @service_level_code.setter
    def service_level_code(self, service_level_code):
        """Sets the service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_level_code: The service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._service_level_code = service_level_code

    @property
    def next_service_level(self):
        """Gets the next_service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The next_service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._next_service_level

    @next_service_level.setter
    def next_service_level(self, next_service_level):
        """Sets the next_service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param next_service_level: The next_service_level of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._next_service_level = next_service_level

    @property
    def next_service_level_code(self):
        """Gets the next_service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The next_service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._next_service_level_code

    @next_service_level_code.setter
    def next_service_level_code(self, next_service_level_code):
        """Sets the next_service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param next_service_level_code: The next_service_level_code of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._next_service_level_code = next_service_level_code

    @property
    def asset_name(self):
        """Gets the asset_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The asset_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        """Sets the asset_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param asset_name: The asset_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_name = asset_name

    @property
    def asset_description(self):
        """Gets the asset_description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The asset_description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        """Sets the asset_description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param asset_description: The asset_description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._asset_description = asset_description

    @property
    def parts_charge(self):
        """Gets the parts_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The parts_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._parts_charge

    @parts_charge.setter
    def parts_charge(self, parts_charge):
        """Sets the parts_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param parts_charge: The parts_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: float
        """

        self._parts_charge = parts_charge

    @property
    def parts_charge_before_discount(self):
        """Gets the parts_charge_before_discount of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The parts_charge_before_discount of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._parts_charge_before_discount

    @parts_charge_before_discount.setter
    def parts_charge_before_discount(self, parts_charge_before_discount):
        """Sets the parts_charge_before_discount of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param parts_charge_before_discount: The parts_charge_before_discount of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: float
        """

        self._parts_charge_before_discount = parts_charge_before_discount

    @property
    def service_charge(self):
        """Gets the service_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._service_charge

    @service_charge.setter
    def service_charge(self, service_charge):
        """Sets the service_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_charge: The service_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: float
        """

        self._service_charge = service_charge

    @property
    def repairs_charge(self):
        """Gets the repairs_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The repairs_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._repairs_charge

    @repairs_charge.setter
    def repairs_charge(self, repairs_charge):
        """Sets the repairs_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param repairs_charge: The repairs_charge of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: float
        """

        self._repairs_charge = repairs_charge

    @property
    def segment_name(self):
        """Gets the segment_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The segment_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._segment_name

    @segment_name.setter
    def segment_name(self, segment_name):
        """Sets the segment_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param segment_name: The segment_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._segment_name = segment_name

    @property
    def schedule_name(self):
        """Gets the schedule_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The schedule_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._schedule_name

    @schedule_name.setter
    def schedule_name(self, schedule_name):
        """Sets the schedule_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param schedule_name: The schedule_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: str
        """

        self._schedule_name = schedule_name

    @property
    def service_schedule_segment_id(self):
        """Gets the service_schedule_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The service_schedule_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_schedule_segment_id

    @service_schedule_segment_id.setter
    def service_schedule_segment_id(self, service_schedule_segment_id):
        """Sets the service_schedule_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param service_schedule_segment_id: The service_schedule_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: int
        """

        self._service_schedule_segment_id = service_schedule_segment_id

    @property
    def forward_next_service(self):
        """Gets the forward_next_service of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The forward_next_service of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._forward_next_service

    @forward_next_service.setter
    def forward_next_service(self, forward_next_service):
        """Sets the forward_next_service of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param forward_next_service: The forward_next_service of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: bool
        """

        self._forward_next_service = forward_next_service

    @property
    def forward_segment_id(self):
        """Gets the forward_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The forward_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._forward_segment_id

    @forward_segment_id.setter
    def forward_segment_id(self, forward_segment_id):
        """Sets the forward_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param forward_segment_id: The forward_segment_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: int
        """

        self._forward_segment_id = forward_segment_id

    @property
    def measurement_batches(self):
        """Gets the measurement_batches of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501


        :return: The measurement_batches of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :rtype: list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModel]
        """
        return self._measurement_batches

    @measurement_batches.setter
    def measurement_batches(self, measurement_batches):
        """Sets the measurement_batches of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.


        :param measurement_batches: The measurement_batches of this QualerApiModelsMeasurementsToMeasurementRecordResponseModel.  # noqa: E501
        :type: list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModel]
        """

        self._measurement_batches = measurement_batches

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
        if issubclass(QualerApiModelsMeasurementsToMeasurementRecordResponseModel, dict):
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
        if not isinstance(other, QualerApiModelsMeasurementsToMeasurementRecordResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
