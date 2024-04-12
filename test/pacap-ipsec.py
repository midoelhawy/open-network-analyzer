import datetime
from nfstream import NFStreamer
import json

online_streamer = NFStreamer(
    source="/home/ahmedhekal/Downloads/pcap/merged.pcap",
    decode_tunnels=True,
    bpf_filter=None,
    promiscuous_mode=True,
    snapshot_length=1536,
    idle_timeout=120,
    active_timeout=1800,
    accounting_mode=0,
    udps=None,
    n_dissections=20,
    statistical_analysis=True,
)

flows_to_be_analyzed = []

def convertNflowToDct(obj:NFStreamer):
    newdict = {}
    
    for key in dir(obj):
        if not key.startswith('__') and key != "_C":
            try:
                prop = getattr(obj, key)
                if type(prop) is str or type(prop) is int or type(prop) is float:
                    newdict[key] = prop
                #newdict[key] = prop
            except:
                print(f"Ignored {key}")
            
    
    newdict["FIRST_SEEN_SRC"] =  datetime.datetime.fromtimestamp(obj.src2dst_first_seen_ms/1000.0).isoformat()
    newdict["FIRST_SEEN_DST"] = datetime.datetime.fromtimestamp(obj.dst2src_first_seen_ms/1000.0).isoformat()
    newdict["LAST_SEEN_SRC"] = datetime.datetime.fromtimestamp(obj.src2dst_last_seen_ms/1000.0).isoformat()
    newdict["LAST_SEEN_DST"] = datetime.datetime.fromtimestamp(obj.dst2src_last_seen_ms/1000.0).isoformat()
    newdict["SRC_DURATION"] = int(obj.src2dst_duration_ms  / 1000)
    newdict["DST_DURATION"] = int(obj.dst2src_duration_ms  / 1000)
    
    
    return newdict


for flow in online_streamer:
    # if flow.ip_version == 6:
    flows_to_be_analyzed.append(convertNflowToDct(flow))
        
        # flows_to_be_analyzed.append({
        #     "SRC_IP": flow.src_ip,
        #     "DST_IP": flow.dst_ip,
        #     "APPLICATION": flow.application_name,
        #     "CATEGORY": flow.application_category_name,
        #     "DST_PORT": flow.dst_port,
        #     "SRC_PORT": flow.src_port,
        #     "SRC_DURATION": int(flow.src2dst_duration_ms  / 1000),
        #     "DST_DURATION": int(flow.dst2src_duration_ms  / 1000),
        #     "PROTOCOL": flow.protocol,
        #     "FIRST_SEEN_SRC":  datetime.datetime.fromtimestamp(flow.src2dst_first_seen_ms/1000.0).isoformat() ,
        #     "FIRST_SEEN_DST": datetime.datetime.fromtimestamp(flow.dst2src_first_seen_ms/1000.0).isoformat(),
        #     "LAST_SEEN_SRC": datetime.datetime.fromtimestamp(flow.src2dst_last_seen_ms/1000.0).isoformat(),
        #     "LAST_SEEN_DST": datetime.datetime.fromtimestamp(flow.dst2src_last_seen_ms/1000.0).isoformat(),
            
        # })
        #print(f"SRC_IP:{flow.src_ip}; DST_IP: {flow.dst_ip} ;APPLICATION : {flow.application_name}; CATEGORY: {flow.application_category_name} ; DST_PORT: {flow.dst_port}; SRC_PORT: {flow.src_port} ; SRC_DURATION: {int(flow.src2dst_duration_ms  / 1000)}; DST_DURATION: {int(flow.dst2src_duration_ms  / 1000)}")
    #print(flow)
    
    
print(flows_to_be_analyzed)


with open('/tmp/result.json', 'w') as fp:
    json.dump(flows_to_be_analyzed, fp)