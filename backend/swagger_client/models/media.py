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


class Media(object):
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
        'key': 'str',
        'type': 'str',
        'foreign_key': 'str',
        'details': 'object',
        'preferred': 'bool',
        'direct_url': 'str',
        'view_url': 'str'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'foreign_key': 'foreign_key',
        'details': 'details',
        'preferred': 'preferred',
        'direct_url': 'direct_url',
        'view_url': 'view_url'
    }

    def __init__(self, key=None, type=None, foreign_key=None, details=None, preferred=None, direct_url=None, view_url=None):  # noqa: E501
        """Media - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._type = None
        self._foreign_key = None
        self._details = None
        self._preferred = None
        self._direct_url = None
        self._view_url = None
        self.discriminator = None

        self.key = key
        self.type = type
        if foreign_key is not None:
            self.foreign_key = foreign_key
        if details is not None:
            self.details = details
        if preferred is not None:
            self.preferred = preferred
        if direct_url is not None:
            self.direct_url = direct_url
        if view_url is not None:
            self.view_url = view_url

    @property
    def key(self):
        """Gets the key of this Media.  # noqa: E501

        TBA identifier for this media.  # noqa: E501

        :return: The key of this Media.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Media.

        TBA identifier for this media.  # noqa: E501

        :param key: The key of this Media.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def type(self):
        """Gets the type of this Media.  # noqa: E501

        String type of the media element.  # noqa: E501

        :return: The type of this Media.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Media.

        String type of the media element.  # noqa: E501

        :param type: The type of this Media.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["youtube", "cdphotothread", "imgur", "facebook-profile", "youtube-channel", "twitter-profile", "github-profile", "instagram-profile", "periscope-profile", "grabcad", "instagram-image", "external-link", "avatar", "direct_link"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def foreign_key(self):
        """Gets the foreign_key of this Media.  # noqa: E501

        The key used to identify this media on the media site.  # noqa: E501

        :return: The foreign_key of this Media.  # noqa: E501
        :rtype: str
        """
        return self._foreign_key

    @foreign_key.setter
    def foreign_key(self, foreign_key):
        """Sets the foreign_key of this Media.

        The key used to identify this media on the media site.  # noqa: E501

        :param foreign_key: The foreign_key of this Media.  # noqa: E501
        :type: str
        """

        self._foreign_key = foreign_key

    @property
    def details(self):
        """Gets the details of this Media.  # noqa: E501

        If required, a JSON dict of additional media information.  # noqa: E501

        :return: The details of this Media.  # noqa: E501
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Media.

        If required, a JSON dict of additional media information.  # noqa: E501

        :param details: The details of this Media.  # noqa: E501
        :type: object
        """

        self._details = details

    @property
    def preferred(self):
        """Gets the preferred of this Media.  # noqa: E501

        True if the media is of high quality.  # noqa: E501

        :return: The preferred of this Media.  # noqa: E501
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this Media.

        True if the media is of high quality.  # noqa: E501

        :param preferred: The preferred of this Media.  # noqa: E501
        :type: bool
        """

        self._preferred = preferred

    @property
    def direct_url(self):
        """Gets the direct_url of this Media.  # noqa: E501

        Direct URL to the media.  # noqa: E501

        :return: The direct_url of this Media.  # noqa: E501
        :rtype: str
        """
        return self._direct_url

    @direct_url.setter
    def direct_url(self, direct_url):
        """Sets the direct_url of this Media.

        Direct URL to the media.  # noqa: E501

        :param direct_url: The direct_url of this Media.  # noqa: E501
        :type: str
        """

        self._direct_url = direct_url

    @property
    def view_url(self):
        """Gets the view_url of this Media.  # noqa: E501

        The URL that leads to the full web page for the media, if one exists.  # noqa: E501

        :return: The view_url of this Media.  # noqa: E501
        :rtype: str
        """
        return self._view_url

    @view_url.setter
    def view_url(self, view_url):
        """Sets the view_url of this Media.

        The URL that leads to the full web page for the media, if one exists.  # noqa: E501

        :param view_url: The view_url of this Media.  # noqa: E501
        :type: str
        """

        self._view_url = view_url

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
        if issubclass(Media, dict):
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
        if not isinstance(other, Media):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
