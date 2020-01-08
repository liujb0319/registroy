#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed 2019-11-15 14:11:10 2019

@author: liujunbang
"""

import abc
from neutron_lib.api import extensions as api_extensions
from neutron_lib.services import base as service_base
import six

from neutron.api.v2 import resource_helper

CLOUD_DC_PEER = "CLOUD_DC_PEER"
ALIAS = "cloud_dc_peer"
RESOURCE_NAME = 'cloud_dc_peer'
COLLECTION_NAME = 'cloud_dc_peers'
# Attribute Map
RESOURCE_ATTRIBUTE_MAP = {
    COLLECTION_NAME: {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_visible': True, 'primary_key': True},
        'tenant_id': {'allow_post': True, 'allow_put': True,
                      'is_visible': True, 'default': False},
        'src_subnets': {'allow_post': True, 'allow_put': True,
                   'is_visible': True, 'default': False},
        'dst_cidr_list': {'allow_post': True, 'allow_put': True,
                   'is_visible': True, 'default': False},
        'iptype': {'allow_post': True, 'allow_put': True,
                      'is_visible': True, 'default': False},
        'vtep_ip': {'allow_post': False, 'allow_put': True,
                   'is_visible': True, 'default': False},
        'result':{ 'allow_post': False, 'allow_put': False,
                   'is_visible': True, 'default': False},
    }
}

class Cloud_dc_peer(api_extensions.ExtensionDescriptor):
    """cloud dc peer API extension."""

    @classmethod
    def get_name(cls):
        return ALIAS

    @classmethod
    def get_alias(cls):
        return ALIAS

    @classmethod
    def get_description(cls):
        return "The cloud dc peer extension."

    @classmethod
    def get_updated(cls):
        return "2019-11-15T10:00:00-00:00"

    @classmethod
    def get_plugin_interface(cls):
        return CloudDcPeerPluginBase
    
    @classmethod
    def get_resources(cls):
        #special_mappings = {'approvers':'approver'}
        plural_mappings = resource_helper.build_plural_mappings(
            {},RESOURCE_ATTRIBUTE_MAP)

        resources = resource_helper.build_resource_info(
                plural_mappings,
                RESOURCE_ATTRIBUTE_MAP,
                RESOURCE_NAME,
                translate_name=True,
                allow_bulk=True)
        return resources
    
    def update_attributes_map(self, attributes, extension_attrs_map=None):
        super(Cloud_dc_peer, self).update_attributes_map(
            attributes,
            extension_attrs_map=RESOURCE_ATTRIBUTE_MAP)

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}

@six.add_metaclass(abc.ABCMeta)
class CloudDcPeerPluginBase(service_base.ServicePluginBase):
    path_prefix = ''
    
    def get_plugin_description(self):
        return "dc peer for openstack or cloudstack"

    @classmethod
    def get_plugin_type(cls):
        return CLOUD_DC_PEER

    @abc.abstractmethod
    def create_cloud_dc_peer(self, context, cloud_dc_peer):
        pass

    @abc.abstractmethod
    def update_cloud_dc_peer(self, context, cloud_dc_peer_id, cloud_dc_peer):
        pass

    @abc.abstractmethod
    def delete_cloud_dc_peer(self, context, cloud_dc_peer_id):
        pass

    @abc.abstractmethod
    def get_cloud_dc_peer(self, context, cloud_dc_peer_id, fields=None):
        pass

