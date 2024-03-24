# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.04.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.api_status_app_version import APIStatusAppVersion  # noqa: F401,E501


class APIStatus(object):
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
        'current_season': 'int',
        'max_season': 'int',
        'is_datafeed_down': 'bool',
        'down_events': 'list[str]',
        'ios': 'APIStatusAppVersion',
        'android': 'APIStatusAppVersion'
    }

    attribute_map = {
        'current_season': 'current_season',
        'max_season': 'max_season',
        'is_datafeed_down': 'is_datafeed_down',
        'down_events': 'down_events',
        'ios': 'ios',
        'android': 'android'
    }

    def __init__(self, current_season=None, max_season=None, is_datafeed_down=None, down_events=None, ios=None, android=None):  # noqa: E501
        """APIStatus - a model defined in Swagger"""  # noqa: E501

        self._current_season = None
        self._max_season = None
        self._is_datafeed_down = None
        self._down_events = None
        self._ios = None
        self._android = None
        self.discriminator = None

        self.current_season = current_season
        self.max_season = max_season
        self.is_datafeed_down = is_datafeed_down
        self.down_events = down_events
        self.ios = ios
        self.android = android

    @property
    def current_season(self):
        """Gets the current_season of this APIStatus.  # noqa: E501

        Year of the current FRC season.  # noqa: E501

        :return: The current_season of this APIStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_season

    @current_season.setter
    def current_season(self, current_season):
        """Sets the current_season of this APIStatus.

        Year of the current FRC season.  # noqa: E501

        :param current_season: The current_season of this APIStatus.  # noqa: E501
        :type: int
        """
        if current_season is None:
            raise ValueError("Invalid value for `current_season`, must not be `None`")  # noqa: E501

        self._current_season = current_season

    @property
    def max_season(self):
        """Gets the max_season of this APIStatus.  # noqa: E501

        Maximum FRC season year for valid queries.  # noqa: E501

        :return: The max_season of this APIStatus.  # noqa: E501
        :rtype: int
        """
        return self._max_season

    @max_season.setter
    def max_season(self, max_season):
        """Sets the max_season of this APIStatus.

        Maximum FRC season year for valid queries.  # noqa: E501

        :param max_season: The max_season of this APIStatus.  # noqa: E501
        :type: int
        """
        if max_season is None:
            raise ValueError("Invalid value for `max_season`, must not be `None`")  # noqa: E501

        self._max_season = max_season

    @property
    def is_datafeed_down(self):
        """Gets the is_datafeed_down of this APIStatus.  # noqa: E501

        True if the entire FMS API provided by FIRST is down.  # noqa: E501

        :return: The is_datafeed_down of this APIStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_datafeed_down

    @is_datafeed_down.setter
    def is_datafeed_down(self, is_datafeed_down):
        """Sets the is_datafeed_down of this APIStatus.

        True if the entire FMS API provided by FIRST is down.  # noqa: E501

        :param is_datafeed_down: The is_datafeed_down of this APIStatus.  # noqa: E501
        :type: bool
        """
        if is_datafeed_down is None:
            raise ValueError("Invalid value for `is_datafeed_down`, must not be `None`")  # noqa: E501

        self._is_datafeed_down = is_datafeed_down

    @property
    def down_events(self):
        """Gets the down_events of this APIStatus.  # noqa: E501

        An array of strings containing event keys of any active events that are no longer updating.  # noqa: E501

        :return: The down_events of this APIStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._down_events

    @down_events.setter
    def down_events(self, down_events):
        """Sets the down_events of this APIStatus.

        An array of strings containing event keys of any active events that are no longer updating.  # noqa: E501

        :param down_events: The down_events of this APIStatus.  # noqa: E501
        :type: list[str]
        """
        if down_events is None:
            raise ValueError("Invalid value for `down_events`, must not be `None`")  # noqa: E501

        self._down_events = down_events

    @property
    def ios(self):
        """Gets the ios of this APIStatus.  # noqa: E501


        :return: The ios of this APIStatus.  # noqa: E501
        :rtype: APIStatusAppVersion
        """
        return self._ios

    @ios.setter
    def ios(self, ios):
        """Sets the ios of this APIStatus.


        :param ios: The ios of this APIStatus.  # noqa: E501
        :type: APIStatusAppVersion
        """
        if ios is None:
            raise ValueError("Invalid value for `ios`, must not be `None`")  # noqa: E501

        self._ios = ios

    @property
    def android(self):
        """Gets the android of this APIStatus.  # noqa: E501


        :return: The android of this APIStatus.  # noqa: E501
        :rtype: APIStatusAppVersion
        """
        return self._android

    @android.setter
    def android(self, android):
        """Sets the android of this APIStatus.


        :param android: The android of this APIStatus.  # noqa: E501
        :type: APIStatusAppVersion
        """
        if android is None:
            raise ValueError("Invalid value for `android`, must not be `None`")  # noqa: E501

        self._android = android

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
        if issubclass(APIStatus, dict):
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
        if not isinstance(other, APIStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
