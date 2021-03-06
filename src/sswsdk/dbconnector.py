"""
Database connection module for SSW.
"""
from . import _connector_map, logger
from .interface import DBInterface


# FIXME: Convert to metaclasses when Py2 support is removed. Metaclasses have unique interfaces to Python2/Python3.


class SonicV1Connector(DBInterface):
    pass


SonicV1Connector.db_map = _connector_map[SonicV1Connector.__name__]['db_map']

if len(SonicV1Connector.db_map) != len({v['db'] for k, v in SonicV1Connector.db_map.items()}):
    raise RuntimeError("Duplicate DB index detected in configuration.")


class SonicV2Connector(DBInterface):
    pass


SonicV2Connector.db_map = _connector_map[SonicV2Connector.__name__]['db_map']

if len(SonicV2Connector.db_map) != len({v['db'] for k, v in SonicV2Connector.db_map.items()}):
    raise RuntimeError("Duplicate DB index detected in configuration.")


class DBConnector(SonicV1Connector):
    logger.warning("DBConnector is DEPRECATED. 'sswsdk.dbconnector.DBConnector' -> 'sswsdk.SonicV1Connector'")
    pass
