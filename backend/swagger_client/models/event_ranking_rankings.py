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

from swagger_client.models.wlt_record import WLTRecord  # noqa: F401,E501


class EventRankingRankings(object):
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
        'dq': 'int',
        'matches_played': 'int',
        'qual_average': 'int',
        'rank': 'int',
        'record': 'WLTRecord',
        'extra_stats': 'list[float]',
        'sort_orders': 'list[float]',
        'team_key': 'str'
    }

    attribute_map = {
        'dq': 'dq',
        'matches_played': 'matches_played',
        'qual_average': 'qual_average',
        'rank': 'rank',
        'record': 'record',
        'extra_stats': 'extra_stats',
        'sort_orders': 'sort_orders',
        'team_key': 'team_key'
    }

    def __init__(self, dq=None, matches_played=None, qual_average=None, rank=None, record=None, extra_stats=None, sort_orders=None, team_key=None):  # noqa: E501
        """EventRankingRankings - a model defined in Swagger"""  # noqa: E501

        self._dq = None
        self._matches_played = None
        self._qual_average = None
        self._rank = None
        self._record = None
        self._extra_stats = None
        self._sort_orders = None
        self._team_key = None
        self.discriminator = None

        self.dq = dq
        self.matches_played = matches_played
        if qual_average is not None:
            self.qual_average = qual_average
        self.rank = rank
        self.record = record
        if extra_stats is not None:
            self.extra_stats = extra_stats
        if sort_orders is not None:
            self.sort_orders = sort_orders
        self.team_key = team_key

    @property
    def dq(self):
        """Gets the dq of this EventRankingRankings.  # noqa: E501

        Number of times disqualified.  # noqa: E501

        :return: The dq of this EventRankingRankings.  # noqa: E501
        :rtype: int
        """
        return self._dq

    @dq.setter
    def dq(self, dq):
        """Sets the dq of this EventRankingRankings.

        Number of times disqualified.  # noqa: E501

        :param dq: The dq of this EventRankingRankings.  # noqa: E501
        :type: int
        """
        if dq is None:
            raise ValueError("Invalid value for `dq`, must not be `None`")  # noqa: E501

        self._dq = dq

    @property
    def matches_played(self):
        """Gets the matches_played of this EventRankingRankings.  # noqa: E501

        Number of matches played by this team.  # noqa: E501

        :return: The matches_played of this EventRankingRankings.  # noqa: E501
        :rtype: int
        """
        return self._matches_played

    @matches_played.setter
    def matches_played(self, matches_played):
        """Sets the matches_played of this EventRankingRankings.

        Number of matches played by this team.  # noqa: E501

        :param matches_played: The matches_played of this EventRankingRankings.  # noqa: E501
        :type: int
        """
        if matches_played is None:
            raise ValueError("Invalid value for `matches_played`, must not be `None`")  # noqa: E501

        self._matches_played = matches_played

    @property
    def qual_average(self):
        """Gets the qual_average of this EventRankingRankings.  # noqa: E501

        The average match score during qualifications. Year specific. May be null if not relevant for a given year.  # noqa: E501

        :return: The qual_average of this EventRankingRankings.  # noqa: E501
        :rtype: int
        """
        return self._qual_average

    @qual_average.setter
    def qual_average(self, qual_average):
        """Sets the qual_average of this EventRankingRankings.

        The average match score during qualifications. Year specific. May be null if not relevant for a given year.  # noqa: E501

        :param qual_average: The qual_average of this EventRankingRankings.  # noqa: E501
        :type: int
        """

        self._qual_average = qual_average

    @property
    def rank(self):
        """Gets the rank of this EventRankingRankings.  # noqa: E501

        The team's rank at the event as provided by FIRST.  # noqa: E501

        :return: The rank of this EventRankingRankings.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this EventRankingRankings.

        The team's rank at the event as provided by FIRST.  # noqa: E501

        :param rank: The rank of this EventRankingRankings.  # noqa: E501
        :type: int
        """
        if rank is None:
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def record(self):
        """Gets the record of this EventRankingRankings.  # noqa: E501


        :return: The record of this EventRankingRankings.  # noqa: E501
        :rtype: WLTRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this EventRankingRankings.


        :param record: The record of this EventRankingRankings.  # noqa: E501
        :type: WLTRecord
        """
        if record is None:
            raise ValueError("Invalid value for `record`, must not be `None`")  # noqa: E501

        self._record = record

    @property
    def extra_stats(self):
        """Gets the extra_stats of this EventRankingRankings.  # noqa: E501

        Additional special data on the team's performance calculated by TBA.  # noqa: E501

        :return: The extra_stats of this EventRankingRankings.  # noqa: E501
        :rtype: list[float]
        """
        return self._extra_stats

    @extra_stats.setter
    def extra_stats(self, extra_stats):
        """Sets the extra_stats of this EventRankingRankings.

        Additional special data on the team's performance calculated by TBA.  # noqa: E501

        :param extra_stats: The extra_stats of this EventRankingRankings.  # noqa: E501
        :type: list[float]
        """

        self._extra_stats = extra_stats

    @property
    def sort_orders(self):
        """Gets the sort_orders of this EventRankingRankings.  # noqa: E501

        Additional year-specific information, may be null. See parent `sort_order_info` for details.  # noqa: E501

        :return: The sort_orders of this EventRankingRankings.  # noqa: E501
        :rtype: list[float]
        """
        return self._sort_orders

    @sort_orders.setter
    def sort_orders(self, sort_orders):
        """Sets the sort_orders of this EventRankingRankings.

        Additional year-specific information, may be null. See parent `sort_order_info` for details.  # noqa: E501

        :param sort_orders: The sort_orders of this EventRankingRankings.  # noqa: E501
        :type: list[float]
        """

        self._sort_orders = sort_orders

    @property
    def team_key(self):
        """Gets the team_key of this EventRankingRankings.  # noqa: E501

        The team with this rank.  # noqa: E501

        :return: The team_key of this EventRankingRankings.  # noqa: E501
        :rtype: str
        """
        return self._team_key

    @team_key.setter
    def team_key(self, team_key):
        """Sets the team_key of this EventRankingRankings.

        The team with this rank.  # noqa: E501

        :param team_key: The team_key of this EventRankingRankings.  # noqa: E501
        :type: str
        """
        if team_key is None:
            raise ValueError("Invalid value for `team_key`, must not be `None`")  # noqa: E501

        self._team_key = team_key

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
        if issubclass(EventRankingRankings, dict):
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
        if not isinstance(other, EventRankingRankings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
