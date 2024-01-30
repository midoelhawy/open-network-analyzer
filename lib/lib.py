from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NFlowTable(Base):
    __tablename__ = 'nflows'

    id = Column(Integer, primary_key=True)
    expiration_id = Column(Integer)
    src_ip = Column(String)
    src_mac = Column(String)
    src_oui = Column(String)
    src_port = Column(Integer)
    dst_ip = Column(String)
    dst_mac = Column(String)
    dst_oui = Column(String)
    dst_port = Column(Integer)
    protocol = Column(Integer)
    ip_version = Column(Integer)
    vlan_id = Column(Integer)
    tunnel_id = Column(Integer)
    bidirectional_first_seen= Column(Integer)
    bidirectional_last_seen= Column(Integer)
    bidirectional_duration = Column(Integer)
    bidirectional_packets = Column(Integer)
    bidirectional_bytes = Column(Integer)
    src2dst_first_seen = Column(Integer)
    src2dst_last_seen = Column(Integer)
    src2dst_duration = Column(Integer)
    src2dst_packets = Column(Integer)
    src2dst_bytes = Column(Integer)
    dst2src_first_seen = Column(Integer)
    dst2src_last_seen = Column(Integer)
    dst2src_duration = Column(Integer)
    dst2src_packets = Column(Integer)
    dst2src_bytes = Column(Integer)
    application_name = Column(String)
    application_category_name = Column(String)
    application_is_guessed = Column(Integer)
    application_confidence = Column(Integer)
    requested_server_name = Column(String)
    client_fingerprint = Column(String)
    server_fingerprint = Column(String)
    user_agent = Column(String)
    content_type = Column(String)

def create_nflow_record(nflow_instance):

    engine = create_engine('mysql+pymysql://dev:mido@localhost:3306/flows', echo=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    nflow_record = NFlowTable(
        expiration_id=nflow_instance.expiration_id,
        src_ip=nflow_instance.src_ip,
        src_mac=nflow_instance.src_mac,
        src_oui=nflow_instance.src_oui,
        src_port=nflow_instance.src_port,
        dst_ip=nflow_instance.dst_ip,
        dst_mac=nflow_instance.dst_mac,
        dst_oui=nflow_instance.dst_oui,
        dst_port=nflow_instance.dst_port,
        protocol=nflow_instance.protocol,
        ip_version=nflow_instance.ip_version,
        vlan_id=nflow_instance.vlan_id,
        tunnel_id=nflow_instance.tunnel_id,
        bidirectional_first_seen=int(nflow_instance.bidirectional_first_seen_ms / 1000),
        bidirectional_last_seen=int(nflow_instance.bidirectional_last_seen_ms  / 1000),
        bidirectional_duration=int(nflow_instance.bidirectional_duration_ms  / 1000),
        bidirectional_packets=nflow_instance.bidirectional_packets,
        bidirectional_bytes=nflow_instance.bidirectional_bytes,
        src2dst_first_seen=int(nflow_instance.src2dst_first_seen_ms  / 1000),
        src2dst_last_seen=int(nflow_instance.src2dst_last_seen_ms  / 1000),
        src2dst_duration=int(nflow_instance.src2dst_duration_ms  / 1000),
        src2dst_packets=nflow_instance.src2dst_packets,
        src2dst_bytes=nflow_instance.src2dst_bytes,
        dst2src_first_seen=int(nflow_instance.dst2src_first_seen_ms  / 1000),
        dst2src_last_seen=int(nflow_instance.dst2src_last_seen_ms  / 1000),
        dst2src_duration=int(nflow_instance.dst2src_duration_ms  / 1000),
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

    session.add(nflow_record)
    session.commit()


