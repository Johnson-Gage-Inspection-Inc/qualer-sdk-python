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

class QualerApiModelsMaintenancePlansToMaintenanceTaskResponse(object):
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
        'segment_name': 'str',
        'service_level_id': 'int',
        'display_order': 'int',
        'service_notes': 'str',
        'interval_cycle': 'str',
        'interval_length': 'int',
        'on_day': 'str',
        'on_month': 'str',
        'on_week_days': 'str',
        'weekday_of_month': 'str',
        'color_code': 'int',
        'service_interval': 'str',
        'on_segment_id': 'int',
        'document_number': 'str',
        'document_section': 'str',
        'as_found_standard_group_id': 'int',
        'as_left_standard_group_id': 'int',
        'task_notes': 'str',
        'advance_recall_period': 'str',
        'days_before_due': 'int',
        'past_due_grace_period': 'str',
        'days_after_due': 'int',
        'use_period_in_reports': 'str',
        'generate_order_automatically': 'bool',
        'approve_upon_generation': 'bool',
        'generate_separate': 'bool'
    }

    attribute_map = {
        'segment_name': 'SegmentName',
        'service_level_id': 'ServiceLevelId',
        'display_order': 'DisplayOrder',
        'service_notes': 'ServiceNotes',
        'interval_cycle': 'IntervalCycle',
        'interval_length': 'IntervalLength',
        'on_day': 'OnDay',
        'on_month': 'OnMonth',
        'on_week_days': 'OnWeekDays',
        'weekday_of_month': 'WeekdayOfMonth',
        'color_code': 'ColorCode',
        'service_interval': 'ServiceInterval',
        'on_segment_id': 'OnSegmentId',
        'document_number': 'DocumentNumber',
        'document_section': 'DocumentSection',
        'as_found_standard_group_id': 'AsFoundStandardGroupId',
        'as_left_standard_group_id': 'AsLeftStandardGroupId',
        'task_notes': 'TaskNotes',
        'advance_recall_period': 'AdvanceRecallPeriod',
        'days_before_due': 'DaysBeforeDue',
        'past_due_grace_period': 'PastDueGracePeriod',
        'days_after_due': 'DaysAfterDue',
        'use_period_in_reports': 'UsePeriodInReports',
        'generate_order_automatically': 'GenerateOrderAutomatically',
        'approve_upon_generation': 'ApproveUponGeneration',
        'generate_separate': 'GenerateSeparate'
    }

    def __init__(self, segment_name=None, service_level_id=None, display_order=None, service_notes=None, interval_cycle=None, interval_length=None, on_day=None, on_month=None, on_week_days=None, weekday_of_month=None, color_code=None, service_interval=None, on_segment_id=None, document_number=None, document_section=None, as_found_standard_group_id=None, as_left_standard_group_id=None, task_notes=None, advance_recall_period=None, days_before_due=None, past_due_grace_period=None, days_after_due=None, use_period_in_reports=None, generate_order_automatically=None, approve_upon_generation=None, generate_separate=None):  # noqa: E501
        """QualerApiModelsMaintenancePlansToMaintenanceTaskResponse - a model defined in Swagger"""  # noqa: E501
        self._segment_name = None
        self._service_level_id = None
        self._display_order = None
        self._service_notes = None
        self._interval_cycle = None
        self._interval_length = None
        self._on_day = None
        self._on_month = None
        self._on_week_days = None
        self._weekday_of_month = None
        self._color_code = None
        self._service_interval = None
        self._on_segment_id = None
        self._document_number = None
        self._document_section = None
        self._as_found_standard_group_id = None
        self._as_left_standard_group_id = None
        self._task_notes = None
        self._advance_recall_period = None
        self._days_before_due = None
        self._past_due_grace_period = None
        self._days_after_due = None
        self._use_period_in_reports = None
        self._generate_order_automatically = None
        self._approve_upon_generation = None
        self._generate_separate = None
        self.discriminator = None
        if segment_name is not None:
            self.segment_name = segment_name
        if service_level_id is not None:
            self.service_level_id = service_level_id
        if display_order is not None:
            self.display_order = display_order
        if service_notes is not None:
            self.service_notes = service_notes
        if interval_cycle is not None:
            self.interval_cycle = interval_cycle
        if interval_length is not None:
            self.interval_length = interval_length
        if on_day is not None:
            self.on_day = on_day
        if on_month is not None:
            self.on_month = on_month
        if on_week_days is not None:
            self.on_week_days = on_week_days
        if weekday_of_month is not None:
            self.weekday_of_month = weekday_of_month
        if color_code is not None:
            self.color_code = color_code
        if service_interval is not None:
            self.service_interval = service_interval
        if on_segment_id is not None:
            self.on_segment_id = on_segment_id
        if document_number is not None:
            self.document_number = document_number
        if document_section is not None:
            self.document_section = document_section
        if as_found_standard_group_id is not None:
            self.as_found_standard_group_id = as_found_standard_group_id
        if as_left_standard_group_id is not None:
            self.as_left_standard_group_id = as_left_standard_group_id
        if task_notes is not None:
            self.task_notes = task_notes
        if advance_recall_period is not None:
            self.advance_recall_period = advance_recall_period
        if days_before_due is not None:
            self.days_before_due = days_before_due
        if past_due_grace_period is not None:
            self.past_due_grace_period = past_due_grace_period
        if days_after_due is not None:
            self.days_after_due = days_after_due
        if use_period_in_reports is not None:
            self.use_period_in_reports = use_period_in_reports
        if generate_order_automatically is not None:
            self.generate_order_automatically = generate_order_automatically
        if approve_upon_generation is not None:
            self.approve_upon_generation = approve_upon_generation
        if generate_separate is not None:
            self.generate_separate = generate_separate

    @property
    def segment_name(self):
        """Gets the segment_name of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The segment_name of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._segment_name

    @segment_name.setter
    def segment_name(self, segment_name):
        """Sets the segment_name of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param segment_name: The segment_name of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._segment_name = segment_name

    @property
    def service_level_id(self):
        """Gets the service_level_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The service_level_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._service_level_id

    @service_level_id.setter
    def service_level_id(self, service_level_id):
        """Sets the service_level_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param service_level_id: The service_level_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._service_level_id = service_level_id

    @property
    def display_order(self):
        """Gets the display_order of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The display_order of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param display_order: The display_order of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def service_notes(self):
        """Gets the service_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The service_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._service_notes

    @service_notes.setter
    def service_notes(self, service_notes):
        """Sets the service_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param service_notes: The service_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._service_notes = service_notes

    @property
    def interval_cycle(self):
        """Gets the interval_cycle of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The interval_cycle of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._interval_cycle

    @interval_cycle.setter
    def interval_cycle(self, interval_cycle):
        """Sets the interval_cycle of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param interval_cycle: The interval_cycle of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._interval_cycle = interval_cycle

    @property
    def interval_length(self):
        """Gets the interval_length of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The interval_length of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._interval_length

    @interval_length.setter
    def interval_length(self, interval_length):
        """Sets the interval_length of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param interval_length: The interval_length of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._interval_length = interval_length

    @property
    def on_day(self):
        """Gets the on_day of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The on_day of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._on_day

    @on_day.setter
    def on_day(self, on_day):
        """Sets the on_day of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param on_day: The on_day of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._on_day = on_day

    @property
    def on_month(self):
        """Gets the on_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The on_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._on_month

    @on_month.setter
    def on_month(self, on_month):
        """Sets the on_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param on_month: The on_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._on_month = on_month

    @property
    def on_week_days(self):
        """Gets the on_week_days of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The on_week_days of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._on_week_days

    @on_week_days.setter
    def on_week_days(self, on_week_days):
        """Sets the on_week_days of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param on_week_days: The on_week_days of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._on_week_days = on_week_days

    @property
    def weekday_of_month(self):
        """Gets the weekday_of_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The weekday_of_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._weekday_of_month

    @weekday_of_month.setter
    def weekday_of_month(self, weekday_of_month):
        """Sets the weekday_of_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param weekday_of_month: The weekday_of_month of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._weekday_of_month = weekday_of_month

    @property
    def color_code(self):
        """Gets the color_code of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The color_code of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._color_code

    @color_code.setter
    def color_code(self, color_code):
        """Sets the color_code of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param color_code: The color_code of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._color_code = color_code

    @property
    def service_interval(self):
        """Gets the service_interval of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The service_interval of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._service_interval

    @service_interval.setter
    def service_interval(self, service_interval):
        """Sets the service_interval of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param service_interval: The service_interval of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._service_interval = service_interval

    @property
    def on_segment_id(self):
        """Gets the on_segment_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The on_segment_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._on_segment_id

    @on_segment_id.setter
    def on_segment_id(self, on_segment_id):
        """Sets the on_segment_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param on_segment_id: The on_segment_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._on_segment_id = on_segment_id

    @property
    def document_number(self):
        """Gets the document_number of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The document_number of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param document_number: The document_number of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._document_number = document_number

    @property
    def document_section(self):
        """Gets the document_section of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The document_section of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._document_section

    @document_section.setter
    def document_section(self, document_section):
        """Sets the document_section of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param document_section: The document_section of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._document_section = document_section

    @property
    def as_found_standard_group_id(self):
        """Gets the as_found_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The as_found_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._as_found_standard_group_id

    @as_found_standard_group_id.setter
    def as_found_standard_group_id(self, as_found_standard_group_id):
        """Sets the as_found_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param as_found_standard_group_id: The as_found_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._as_found_standard_group_id = as_found_standard_group_id

    @property
    def as_left_standard_group_id(self):
        """Gets the as_left_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The as_left_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._as_left_standard_group_id

    @as_left_standard_group_id.setter
    def as_left_standard_group_id(self, as_left_standard_group_id):
        """Sets the as_left_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param as_left_standard_group_id: The as_left_standard_group_id of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._as_left_standard_group_id = as_left_standard_group_id

    @property
    def task_notes(self):
        """Gets the task_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The task_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._task_notes

    @task_notes.setter
    def task_notes(self, task_notes):
        """Sets the task_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param task_notes: The task_notes of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._task_notes = task_notes

    @property
    def advance_recall_period(self):
        """Gets the advance_recall_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The advance_recall_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._advance_recall_period

    @advance_recall_period.setter
    def advance_recall_period(self, advance_recall_period):
        """Sets the advance_recall_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param advance_recall_period: The advance_recall_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._advance_recall_period = advance_recall_period

    @property
    def days_before_due(self):
        """Gets the days_before_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The days_before_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._days_before_due

    @days_before_due.setter
    def days_before_due(self, days_before_due):
        """Sets the days_before_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param days_before_due: The days_before_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._days_before_due = days_before_due

    @property
    def past_due_grace_period(self):
        """Gets the past_due_grace_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The past_due_grace_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._past_due_grace_period

    @past_due_grace_period.setter
    def past_due_grace_period(self, past_due_grace_period):
        """Sets the past_due_grace_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param past_due_grace_period: The past_due_grace_period of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._past_due_grace_period = past_due_grace_period

    @property
    def days_after_due(self):
        """Gets the days_after_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The days_after_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: int
        """
        return self._days_after_due

    @days_after_due.setter
    def days_after_due(self, days_after_due):
        """Sets the days_after_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param days_after_due: The days_after_due of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: int
        """

        self._days_after_due = days_after_due

    @property
    def use_period_in_reports(self):
        """Gets the use_period_in_reports of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The use_period_in_reports of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._use_period_in_reports

    @use_period_in_reports.setter
    def use_period_in_reports(self, use_period_in_reports):
        """Sets the use_period_in_reports of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param use_period_in_reports: The use_period_in_reports of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: str
        """

        self._use_period_in_reports = use_period_in_reports

    @property
    def generate_order_automatically(self):
        """Gets the generate_order_automatically of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The generate_order_automatically of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: bool
        """
        return self._generate_order_automatically

    @generate_order_automatically.setter
    def generate_order_automatically(self, generate_order_automatically):
        """Sets the generate_order_automatically of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param generate_order_automatically: The generate_order_automatically of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: bool
        """

        self._generate_order_automatically = generate_order_automatically

    @property
    def approve_upon_generation(self):
        """Gets the approve_upon_generation of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The approve_upon_generation of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: bool
        """
        return self._approve_upon_generation

    @approve_upon_generation.setter
    def approve_upon_generation(self, approve_upon_generation):
        """Sets the approve_upon_generation of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param approve_upon_generation: The approve_upon_generation of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: bool
        """

        self._approve_upon_generation = approve_upon_generation

    @property
    def generate_separate(self):
        """Gets the generate_separate of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501


        :return: The generate_separate of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :rtype: bool
        """
        return self._generate_separate

    @generate_separate.setter
    def generate_separate(self, generate_separate):
        """Sets the generate_separate of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.


        :param generate_separate: The generate_separate of this QualerApiModelsMaintenancePlansToMaintenanceTaskResponse.  # noqa: E501
        :type: bool
        """

        self._generate_separate = generate_separate

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
        if issubclass(QualerApiModelsMaintenancePlansToMaintenanceTaskResponse, dict):
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
        if not isinstance(other, QualerApiModelsMaintenancePlansToMaintenanceTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
