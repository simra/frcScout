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

from swagger_client.models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup  # noqa: F401,E501


class TeamEventStatusAlliance(object):
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
        'name': 'str',
        'number': 'int',
        'backup': 'TeamEventStatusAllianceBackup',
        'pick': 'int'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'backup': 'backup',
        'pick': 'pick'
    }

    def __init__(self, name=None, number=None, backup=None, pick=None):  # noqa: E501
        """TeamEventStatusAlliance - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._number = None
        self._backup = None
        self._pick = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.number = number
        if backup is not None:
            self.backup = backup
        self.pick = pick

    @property
    def name(self):
        """Gets the name of this TeamEventStatusAlliance.  # noqa: E501

        Alliance name, may be null.  # noqa: E501

        :return: The name of this TeamEventStatusAlliance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamEventStatusAlliance.

        Alliance name, may be null.  # noqa: E501

        :param name: The name of this TeamEventStatusAlliance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this TeamEventStatusAlliance.  # noqa: E501

        Alliance number.  # noqa: E501

        :return: The number of this TeamEventStatusAlliance.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TeamEventStatusAlliance.

        Alliance number.  # noqa: E501

        :param number: The number of this TeamEventStatusAlliance.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def backup(self):
        """Gets the backup of this TeamEventStatusAlliance.  # noqa: E501


        :return: The backup of this TeamEventStatusAlliance.  # noqa: E501
        :rtype: TeamEventStatusAllianceBackup
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """Sets the backup of this TeamEventStatusAlliance.


        :param backup: The backup of this TeamEventStatusAlliance.  # noqa: E501
        :type: TeamEventStatusAllianceBackup
        """

        self._backup = backup

    @property
    def pick(self):
        """Gets the pick of this TeamEventStatusAlliance.  # noqa: E501

        Order the team was picked in the alliance from 0-2, with 0 being alliance captain.  # noqa: E501

        :return: The pick of this TeamEventStatusAlliance.  # noqa: E501
        :rtype: int
        """
        return self._pick

    @pick.setter
    def pick(self, pick):
        """Sets the pick of this TeamEventStatusAlliance.

        Order the team was picked in the alliance from 0-2, with 0 being alliance captain.  # noqa: E501

        :param pick: The pick of this TeamEventStatusAlliance.  # noqa: E501
        :type: int
        """
        if pick is None:
            raise ValueError("Invalid value for `pick`, must not be `None`")  # noqa: E501

        self._pick = pick

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
        if issubclass(TeamEventStatusAlliance, dict):
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
        if not isinstance(other, TeamEventStatusAlliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
