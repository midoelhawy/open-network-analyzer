from typing import Optional
import uuid
# add enum with  status # status | init,active,finished

class FLOW_STATUS:
    INIT = 0
    ACTIVE = 1
    FINISHED = 2


class NFlowInstance:
    
    
    __slots__ = (
        'expiration_id', 'src_ip', 'src_mac', 'src_oui', 'src_port', 'dst_ip',
        'dst_mac', 'dst_oui', 'dst_port', 'protocol', 'ip_version', 'vlan_id',
        'tunnel_id', 'bidirectional_first_seen_ms', 'bidirectional_last_seen_ms',
        'bidirectional_duration_ms', 'bidirectional_packets', 'bidirectional_bytes',
        'src2dst_first_seen_ms', 'src2dst_last_seen_ms', 'src2dst_duration_ms',
        'src2dst_packets', 'src2dst_bytes', 'dst2src_first_seen_ms', 'dst2src_last_seen_ms',
        'dst2src_duration_ms', 'dst2src_packets', 'dst2src_bytes', 'application_name',
        'application_category_name', 'application_is_guessed', 'application_confidence',
        'requested_server_name', 'client_fingerprint', 'server_fingerprint', 'user_agent', 'content_type','uuid'
    )

    def __init__(
        self,
        expiration_id: int,
        uuid: str,
        src_ip: str,
        src_mac: str,
        src_oui: str,
        src_port: int,
        dst_ip: str,
        dst_mac: str,
        dst_oui: str,
        dst_port: int,
        protocol: int,
        ip_version: int,
        vlan_id: Optional[int],
        tunnel_id: Optional[int],
        bidirectional_first_seen_ms: int,
        bidirectional_last_seen_ms: int,
        bidirectional_duration_ms: int,
        bidirectional_packets: int,
        bidirectional_bytes: int,
        src2dst_first_seen_ms: int,
        src2dst_last_seen_ms: int,
        src2dst_duration_ms: int,
        src2dst_packets: int,
        src2dst_bytes: int,
        dst2src_first_seen_ms: int,
        dst2src_last_seen_ms: int,
        dst2src_duration_ms: int,
        dst2src_packets: int,
        dst2src_bytes: int,
        application_name: str,
        application_category_name: str,
        application_is_guessed: int,
        application_confidence: int,
        requested_server_name: str,
        client_fingerprint: str,
        server_fingerprint: str,
        user_agent: str,
        content_type: str
    ) -> None:
        self.uuid = uuid
        self.expiration_id = expiration_id
        self.src_ip = src_ip
        self.src_mac = src_mac
        self.src_oui = src_oui
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_mac = dst_mac
        self.dst_oui = dst_oui
        self.dst_port = dst_port
        self.protocol = protocol
        self.ip_version = ip_version
        self.vlan_id = vlan_id
        self.tunnel_id = tunnel_id
        self.bidirectional_first_seen_ms = bidirectional_first_seen_ms
        self.bidirectional_last_seen_ms = bidirectional_last_seen_ms
        self.bidirectional_duration_ms = bidirectional_duration_ms
        self.bidirectional_packets = bidirectional_packets
        self.bidirectional_bytes = bidirectional_bytes
        self.src2dst_first_seen_ms = src2dst_first_seen_ms
        self.src2dst_last_seen_ms = src2dst_last_seen_ms
        self.src2dst_duration_ms = src2dst_duration_ms
        self.src2dst_packets = src2dst_packets
        self.src2dst_bytes = src2dst_bytes
        self.dst2src_first_seen_ms = dst2src_first_seen_ms
        self.dst2src_last_seen_ms = dst2src_last_seen_ms
        self.dst2src_duration_ms = dst2src_duration_ms
        self.dst2src_packets = dst2src_packets
        self.dst2src_bytes = dst2src_bytes
        self.application_name = application_name
        self.application_category_name = application_category_name
        self.application_is_guessed = application_is_guessed
        self.application_confidence = application_confidence
        self.requested_server_name = requested_server_name
        self.client_fingerprint = client_fingerprint
        self.server_fingerprint = server_fingerprint
        self.user_agent = user_agent
        self.content_type = content_type
