from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

AlchemyBaseDeclarative = declarative_base()

class NFlowInterface(AlchemyBaseDeclarative):
    __tablename__ = 'nflows'

    id = Column(Integer, primary_key=True)
    expiration_id = Column(Integer)
    src_ipv4 = Column(String(255), nullable=True)
    src_ipv6 = Column(String(255), nullable=True)
    src_mac = Column(String(255), nullable=True)
    src_oui = Column(String(255), nullable=True)
    src_port = Column(Integer, nullable=True)
    dst_ipv4 = Column(String(255), nullable=True)
    dst_ipv6 = Column(String(255), nullable=True)
    dst_mac = Column(String(255), nullable=True)
    dst_oui = Column(String(255), nullable=True)
    dst_port = Column(Integer, nullable=True)
    protocol = Column(Integer, nullable=True)
    ip_version = Column(Integer, nullable=False)
    vlan_id = Column(Integer, nullable=True)
    tunnel_id = Column(Integer, nullable=True)
    bidirectional_first_seen = Column(Integer, nullable=True)
    bidirectional_last_seen = Column(Integer, nullable=True)
    bidirectional_duration = Column(Integer, nullable=True)
    bidirectional_packets = Column(Integer, nullable=True)
    bidirectional_bytes = Column(Integer, nullable=True)
    src2dst_first_seen = Column(Integer, nullable=True)
    src2dst_last_seen = Column(Integer, nullable=True)
    src2dst_duration = Column(Integer, nullable=True)
    src2dst_packets = Column(Integer, nullable=True)
    src2dst_bytes = Column(Integer, nullable=True)
    dst2src_first_seen = Column(Integer, nullable=True)
    dst2src_last_seen = Column(Integer, nullable=True)
    dst2src_duration = Column(Integer, nullable=True)
    dst2src_packets = Column(Integer, nullable=True)
    dst2src_bytes = Column(Integer, nullable=True)
    application_name = Column(String(255), nullable=True)
    application_category_name = Column(String(255), nullable=True)
    application_is_guessed = Column(Integer, nullable=True)
    application_confidence = Column(Integer, nullable=True)
    requested_server_name = Column(String(255), nullable=True)
    client_fingerprint = Column(String(255), nullable=True)
    server_fingerprint = Column(String(255), nullable=True)
    user_agent = Column(String(255), nullable=True)
    content_type = Column(String(255), nullable=True)
