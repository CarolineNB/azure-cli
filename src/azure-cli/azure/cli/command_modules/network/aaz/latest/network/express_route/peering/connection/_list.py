# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route peering connection list",
)
class List(AAZCommand):
    """List all global reach connections associated with a private peering in an express route circuit.

    :example: List ExpressRouteCircuit Connection
        az network express-route peering connection list --circuit-name MyCircuit --peering-name MyPeering --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressroutecircuits/{}/peerings/{}/connections", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.circuit_name = AAZStrArg(
            options=["--circuit-name"],
            help="ExpressRoute circuit name.",
            required=True,
        )
        _args_schema.peering_name = AAZStrArg(
            options=["--peering-name"],
            help="Name of BGP peering (i.e. AzurePrivatePeering).",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ExpressRouteCircuitConnectionsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ExpressRouteCircuitConnectionsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "circuitName", self.ctx.args.circuit_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "peeringName", self.ctx.args.peering_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )
            properties.express_route_circuit_peering = AAZObjectType(
                serialized_name="expressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.express_route_circuit_peering)
            properties.ipv6_circuit_connection_config = AAZObjectType(
                serialized_name="ipv6CircuitConnectionConfig",
            )
            properties.peer_express_route_circuit_peering = AAZObjectType(
                serialized_name="peerExpressRouteCircuitPeering",
            )
            _build_schema_sub_resource_read(properties.peer_express_route_circuit_peering)
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            ipv6_circuit_connection_config = cls._schema_on_200.value.Element.properties.ipv6_circuit_connection_config
            ipv6_circuit_connection_config.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            ipv6_circuit_connection_config.circuit_connection_status = AAZStrType(
                serialized_name="circuitConnectionStatus",
                flags={"read_only": True},
            )

            return cls._schema_on_200


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType()

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType()

    _schema.id = _schema_sub_resource_read.id


__all__ = ["List"]
