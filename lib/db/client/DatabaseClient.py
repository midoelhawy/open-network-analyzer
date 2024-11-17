import uuid
from venv import logger

from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from lib.db import NFlowInstance
from lib.db.NFlowInterface import AlchemyBaseDeclarative, NFlowInterface


class DatabaseClient:
    db_url:str
    def __init__(self, db_url) -> None:
        self.db_url = db_url
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.init_db()

    def init_db(self) -> None:
        logger.info("Initializing database")
        if not database_exists(self.db_url):
            create_database(self.db_url)
        AlchemyBaseDeclarative.metadata.create_all(self.engine)

    def add_flow(self, nflow_instance: 'NFlowInstance') -> None:
        session = self.Session()

        if nflow_instance.ip_version == 4:
            src_ip_col = NFlowInterface.src_ipv4
            dst_ip_col = NFlowInterface.dst_ipv4
        elif nflow_instance.ip_version == 6:
            src_ip_col = NFlowInterface.src_ipv6
            dst_ip_col = NFlowInterface.dst_ipv6
        else:
            raise ValueError("Invalid IP version")

        existing_flow = session.query(exists().where(src_ip_col == nflow_instance.src_ip)
                                      .where(dst_ip_col == nflow_instance.dst_ip)
                                      .where(NFlowInterface.src2dst_first_seen == int(nflow_instance.src2dst_first_seen_ms / 1000))).scalar()

        if not existing_flow:
            new_flow = NFlowInterface(
                uuid=nflow_instance.udps.flow_uuid,
                expiration_id=nflow_instance.expiration_id,
                src_ipv4=nflow_instance.src_ip if nflow_instance.ip_version == 4 else None,
                src_ipv6=nflow_instance.src_ip if nflow_instance.ip_version == 6 else None,
                src_mac=nflow_instance.src_mac,
                src_oui=nflow_instance.src_oui,
                src_port=nflow_instance.src_port,
                dst_ipv4=nflow_instance.dst_ip if nflow_instance.ip_version == 4 else None,
                dst_ipv6=nflow_instance.dst_ip if nflow_instance.ip_version == 6 else None,
                dst_mac=nflow_instance.dst_mac,
                dst_oui=nflow_instance.dst_oui,
                dst_port=nflow_instance.dst_port,
                protocol=nflow_instance.protocol,
                ip_version=nflow_instance.ip_version,
                vlan_id=nflow_instance.vlan_id,
                tunnel_id=nflow_instance.tunnel_id,
                bidirectional_first_seen=int(nflow_instance.bidirectional_first_seen_ms / 1000),
                bidirectional_last_seen=int(nflow_instance.bidirectional_last_seen_ms / 1000),
                bidirectional_duration=int(nflow_instance.bidirectional_duration_ms / 1000),
                bidirectional_packets=nflow_instance.bidirectional_packets,
                bidirectional_bytes=nflow_instance.bidirectional_bytes,
                src2dst_first_seen=int(nflow_instance.src2dst_first_seen_ms / 1000),
                src2dst_last_seen=int(nflow_instance.src2dst_last_seen_ms / 1000),
                src2dst_duration=int(nflow_instance.src2dst_duration_ms / 1000),
                src2dst_packets=nflow_instance.src2dst_packets,
                src2dst_bytes=nflow_instance.src2dst_bytes,
                dst2src_first_seen=int(nflow_instance.dst2src_first_seen_ms / 1000),
                dst2src_last_seen=int(nflow_instance.dst2src_last_seen_ms / 1000),
                dst2src_duration=int(nflow_instance.dst2src_duration_ms / 1000),
                dst2src_packets=nflow_instance.dst2src_packets,
                dst2src_bytes=nflow_instance.dst2src_bytes,
                application_name=nflow_instance.application_name,
                application_category_name=nflow_instance.application_category_name,
                application_is_guessed=nflow_instance.application_is_guessed,
                application_confidence=nflow_instance.application_confidence,
                requested_server_name=nflow_instance.requested_server_name,
                client_fingerprint=nflow_instance.client_fingerprint,
                server_fingerprint=nflow_instance.server_fingerprint,
                user_agent=nflow_instance.user_agent,
                content_type=nflow_instance.content_type
            )
            session.add(new_flow)

        session.commit()
        session.close()