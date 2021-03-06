# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class MediaInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, action=None, channel=None, metadata=None, timed_metadata=None, playback_position=None, format=None, quality=None, playback_rate=None):
        """
        MediaInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'channel': 'str',
            'metadata': 'str',
            'timed_metadata': 'str',
            'playback_position': 'float',
            'format': 'str',
            'quality': 'str',
            'playback_rate': 'float'
        }

        self.attribute_map = {
            'action': 'action',
            'channel': 'channel',
            'metadata': 'metadata',
            'timed_metadata': 'timed_metadata',
            'playback_position': 'playback_position',
            'format': 'format',
            'quality': 'quality',
            'playback_rate': 'playback_rate'
        }

        self._action = action
        self._channel = channel
        self._metadata = metadata
        self._timed_metadata = timed_metadata
        self._playback_position = playback_position
        self._format = format
        self._quality = quality
        self._playback_rate = playback_rate

    @property
    def action(self):
        """
        Gets the action of this MediaInfo.


        :return: The action of this MediaInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this MediaInfo.


        :param action: The action of this MediaInfo.
        :type: str
        """
        allowed_values = ["unknown", "play", "stop", "update_playback_position", "skip", "rate"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def channel(self):
        """
        Gets the channel of this MediaInfo.


        :return: The channel of this MediaInfo.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this MediaInfo.


        :param channel: The channel of this MediaInfo.
        :type: str
        """

        self._channel = channel

    @property
    def metadata(self):
        """
        Gets the metadata of this MediaInfo.


        :return: The metadata of this MediaInfo.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MediaInfo.


        :param metadata: The metadata of this MediaInfo.
        :type: str
        """

        self._metadata = metadata

    @property
    def timed_metadata(self):
        """
        Gets the timed_metadata of this MediaInfo.


        :return: The timed_metadata of this MediaInfo.
        :rtype: str
        """
        return self._timed_metadata

    @timed_metadata.setter
    def timed_metadata(self, timed_metadata):
        """
        Sets the timed_metadata of this MediaInfo.


        :param timed_metadata: The timed_metadata of this MediaInfo.
        :type: str
        """

        self._timed_metadata = timed_metadata

    @property
    def playback_position(self):
        """
        Gets the playback_position of this MediaInfo.


        :return: The playback_position of this MediaInfo.
        :rtype: float
        """
        return self._playback_position

    @playback_position.setter
    def playback_position(self, playback_position):
        """
        Sets the playback_position of this MediaInfo.


        :param playback_position: The playback_position of this MediaInfo.
        :type: float
        """

        self._playback_position = playback_position

    @property
    def format(self):
        """
        Gets the format of this MediaInfo.


        :return: The format of this MediaInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this MediaInfo.


        :param format: The format of this MediaInfo.
        :type: str
        """
        allowed_values = ["unknown", "audio", "video"]
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def quality(self):
        """
        Gets the quality of this MediaInfo.


        :return: The quality of this MediaInfo.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this MediaInfo.


        :param quality: The quality of this MediaInfo.
        :type: str
        """
        allowed_values = ["unknown", "low", "sd", "medium", "hd", "ultra_hd"]
        if quality not in allowed_values:
            raise ValueError(
                "Invalid value for `quality` ({0}), must be one of {1}"
                .format(quality, allowed_values)
            )

        self._quality = quality

    @property
    def playback_rate(self):
        """
        Gets the playback_rate of this MediaInfo.


        :return: The playback_rate of this MediaInfo.
        :rtype: float
        """
        return self._playback_rate

    @playback_rate.setter
    def playback_rate(self, playback_rate):
        """
        Sets the playback_rate of this MediaInfo.


        :param playback_rate: The playback_rate of this MediaInfo.
        :type: float
        """

        self._playback_rate = playback_rate

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
