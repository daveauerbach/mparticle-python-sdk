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


class CommerceEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_action=None, timestamp_unixtime_ms=None, event_id=None, source_message_id=None, session_id=None, session_uuid=None, custom_attributes=None, location=None, device_current_state=None, promotion_action=None, product_impressions=None, shopping_cart=None, currency_code=None, screen_name=None, is_non_interactive=None):
        """
        CommerceEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timestamp_unixtime_ms': 'int',
            'event_id': 'int',
            'source_message_id': 'str',
            'session_id': 'int',
            'session_uuid': 'str',
            'custom_attributes': 'dict(str, str)',
            'location': 'GeoLocation',
            'device_current_state': 'DeviceCurrentState',
            'product_action': 'ProductAction',
            'promotion_action': 'PromotionAction',
            'product_impressions': 'list[ProductImpression]',
            'shopping_cart': 'ShoppingCart',
            'currency_code': 'str',
            'screen_name': 'str',
            'is_non_interactive': 'bool'
        }

        self.attribute_map = {
            'timestamp_unixtime_ms': 'timestamp_unixtime_ms',
            'event_id': 'event_id',
            'source_message_id': 'source_message_id',
            'session_id': 'session_id',
            'session_uuid': 'session_uuid',
            'custom_attributes': 'custom_attributes',
            'location': 'location',
            'device_current_state': 'device_current_state',
            'product_action': 'product_action',
            'promotion_action': 'promotion_action',
            'product_impressions': 'product_impressions',
            'shopping_cart': 'shopping_cart',
            'currency_code': 'currency_code',
            'screen_name': 'screen_name',
            'is_non_interactive': 'is_non_interactive'
        }

        self._timestamp_unixtime_ms = timestamp_unixtime_ms
        self._event_id = event_id
        self._source_message_id = source_message_id
        self._session_id = session_id
        self._session_uuid = session_uuid
        self._custom_attributes = custom_attributes
        self._location = location
        self._device_current_state = device_current_state
        self._product_action = product_action
        self._promotion_action = promotion_action
        self._product_impressions = product_impressions
        self._shopping_cart = shopping_cart
        self._currency_code = currency_code
        self._screen_name = screen_name
        self._is_non_interactive = is_non_interactive

        if (product_action is None and
            product_impressions is None and
            promotion_action is None):
            raise ValueError(
                "At least one of: product_action, product_impressions, or promotion_action is required."
            )

    @property
    def timestamp_unixtime_ms(self):
        """
        Gets the timestamp_unixtime_ms of this CommerceEvent.


        :return: The timestamp_unixtime_ms of this CommerceEvent.
        :rtype: int
        """
        return self._timestamp_unixtime_ms

    @timestamp_unixtime_ms.setter
    def timestamp_unixtime_ms(self, timestamp_unixtime_ms):
        """
        Sets the timestamp_unixtime_ms of this CommerceEvent.


        :param timestamp_unixtime_ms: The timestamp_unixtime_ms of this CommerceEvent.
        :type: int
        """

        self._timestamp_unixtime_ms = timestamp_unixtime_ms

    @property
    def event_id(self):
        """
        Gets the event_id of this CommerceEvent.


        :return: The event_id of this CommerceEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this CommerceEvent.


        :param event_id: The event_id of this CommerceEvent.
        :type: int
        """

        self._event_id = event_id

    @property
    def source_message_id(self):
        """
        Gets the source_message_id of this CommerceEvent.


        :return: The source_message_id of this CommerceEvent.
        :rtype: str
        """
        return self._source_message_id

    @source_message_id.setter
    def source_message_id(self, source_message_id):
        """
        Sets the source_message_id of this CommerceEvent.


        :param source_message_id: The source_message_id of this CommerceEvent.
        :type: str
        """

        self._source_message_id = source_message_id

    @property
    def session_id(self):
        """
        Gets the session_id of this CommerceEvent.


        :return: The session_id of this CommerceEvent.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this CommerceEvent.


        :param session_id: The session_id of this CommerceEvent.
        :type: int
        """

        self._session_id = session_id

    @property
    def session_uuid(self):
        """
        Gets the session_uuid of this CommerceEvent.


        :return: The session_uuid of this CommerceEvent.
        :rtype: str
        """
        return self._session_uuid

    @session_uuid.setter
    def session_uuid(self, session_uuid):
        """
        Sets the session_uuid of this CommerceEvent.


        :param session_uuid: The session_uuid of this CommerceEvent.
        :type: str
        """

        self._session_uuid = session_uuid

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this CommerceEvent.


        :return: The custom_attributes of this CommerceEvent.
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this CommerceEvent.


        :param custom_attributes: The custom_attributes of this CommerceEvent.
        :type: dict(str, str)
        """

        self._custom_attributes = custom_attributes

    @property
    def location(self):
        """
        Gets the location of this CommerceEvent.


        :return: The location of this CommerceEvent.
        :rtype: GeoLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this CommerceEvent.


        :param location: The location of this CommerceEvent.
        :type: GeoLocation
        """

        self._location = location

    @property
    def device_current_state(self):
        """
        Gets the device_current_state of this CommerceEvent.


        :return: The device_current_state of this CommerceEvent.
        :rtype: DeviceCurrentState
        """
        return self._device_current_state

    @device_current_state.setter
    def device_current_state(self, device_current_state):
        """
        Sets the device_current_state of this CommerceEvent.


        :param device_current_state: The device_current_state of this CommerceEvent.
        :type: DeviceCurrentState
        """

        self._device_current_state = device_current_state

    @property
    def product_action(self):
        """
        Gets the product_action of this CommerceEvent.


        :return: The product_action of this CommerceEvent.
        :rtype: ProductAction
        """
        return self._product_action

    @product_action.setter
    def product_action(self, product_action):
        """
        Sets the product_action of this CommerceEvent.


        :param product_action: The product_action of this CommerceEvent.
        :type: ProductAction
        """

        self._product_action = product_action

    @property
    def promotion_action(self):
        """
        Gets the promotion_action of this CommerceEvent.


        :return: The promotion_action of this CommerceEvent.
        :rtype: PromotionAction
        """
        return self._promotion_action

    @promotion_action.setter
    def promotion_action(self, promotion_action):
        """
        Sets the promotion_action of this CommerceEvent.


        :param promotion_action: The promotion_action of this CommerceEvent.
        :type: PromotionAction
        """

        self._promotion_action = promotion_action

    @property
    def product_impressions(self):
        """
        Gets the product_impressions of this CommerceEvent.


        :return: The product_impressions of this CommerceEvent.
        :rtype: list[ProductImpression]
        """
        return self._product_impressions

    @product_impressions.setter
    def product_impressions(self, product_impressions):
        """
        Sets the product_impressions of this CommerceEvent.


        :param product_impressions: The product_impressions of this CommerceEvent.
        :type: list[ProductImpression]
        """

        self._product_impressions = product_impressions

    @property
    def shopping_cart(self):
        """
        Gets the shopping_cart of this CommerceEvent.


        :return: The shopping_cart of this CommerceEvent.
        :rtype: ShoppingCart
        """
        return self._shopping_cart

    @shopping_cart.setter
    def shopping_cart(self, shopping_cart):
        """
        Sets the shopping_cart of this CommerceEvent.


        :param shopping_cart: The shopping_cart of this CommerceEvent.
        :type: ShoppingCart
        """

        self._shopping_cart = shopping_cart

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CommerceEvent.


        :return: The currency_code of this CommerceEvent.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CommerceEvent.


        :param currency_code: The currency_code of this CommerceEvent.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def screen_name(self):
        """
        Gets the screen_name of this CommerceEvent.


        :return: The screen_name of this CommerceEvent.
        :rtype: str
        """
        return self._screen_name

    @screen_name.setter
    def screen_name(self, screen_name):
        """
        Sets the screen_name of this CommerceEvent.


        :param screen_name: The screen_name of this CommerceEvent.
        :type: str
        """

        self._screen_name = screen_name

    @property
    def is_non_interactive(self):
        """
        Gets the is_non_interactive of this CommerceEvent.


        :return: The is_non_interactive of this CommerceEvent.
        :rtype: bool
        """
        return self._is_non_interactive

    @is_non_interactive.setter
    def is_non_interactive(self, is_non_interactive):
        """
        Sets the is_non_interactive of this CommerceEvent.


        :param is_non_interactive: The is_non_interactive of this CommerceEvent.
        :type: bool
        """

        self._is_non_interactive = is_non_interactive

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
