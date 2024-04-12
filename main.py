import argparse
from nfstream import NFStreamer


from lib.lib import DatabaseManager


def main():
    parser = argparse.ArgumentParser(description="NFStreamer attributes")

    parser.add_argument(
        "--source",
        default="",
        help="Packet capture source. Pcap file path, List of pcap files path (considered as a single file) or network interface name.",
    )
    parser.add_argument(
        "--decode_tunnels",
        default=True,
        help="Enable/Disable GTP/CAPWAP/TZSP tunnels decoding.",
    )
    parser.add_argument(
        "--bpf_filter",
        default=None,
        help="Specify a BPF filter filter for filtering selected traffic.",
    )
    parser.add_argument(
        "--promiscuous_mode",
        default=True,
        help="Enable/Disable promiscuous capture mode.",
    )
    parser.add_argument(
        "--snapshot_length",
        default=1536,
        type=int,
        help="Control packet slicing size (truncation) in bytes.",
    )
    parser.add_argument(
        "--idle_timeout",
        default=120,
        type=int,
        help="Flows that are idle (no packets received) for more than this value in seconds are expired.",
    )
    parser.add_argument(
        "--active_timeout",
        default=1800,
        type=int,
        help="Flows that are active for more than this value in seconds are expired.",
    )
    parser.add_argument(
        "--accounting_mode",
        default=0,
        type=int,
        help="Specify the accounting mode that will be used to report bytes related features (0: Link layer, 1: IP layer, 2: Transport layer, 3: Payload).",
    )
    parser.add_argument(
        "--udps",
        default=None,
        help="Specify user defined NFPlugins used to extend NFStreamer.",
    )
    parser.add_argument(
        "--n_dissections",
        default=20,
        type=int,
        help="Number of per flow packets to dissect for L7 visibility feature. When set to 0, L7 visibility feature is disabled.",
    )
    parser.add_argument(
        "--statistical_analysis",
        default=False,
        help="Enable/Disable post-mortem flow statistical analysis.",
    )
    parser.add_argument(
        "--splt_analysis",
        default=0,
        type=int,
        help="Specify the sequence of first packets length for early statistical analysis. When set to 0, splt_analysis is disabled.",
    )
    parser.add_argument(
        "--max_nflows",
        default=0,
        type=int,
        help="Specify the number of maximum flows to capture before returning. Unset when equal to 0.",
    )
    parser.add_argument(
        "--n_meters",
        default=0,
        type=int,
        help="Specify the number of parallel metering processes. When set to 0, NFStreamer will automatically scale metering according to available physical cores on the running host.",
    )
    parser.add_argument(
        "--performance_report",
        default=0,
        type=int,
        help="Performance report interval in seconds. Disabled when set to 0. Ignored for offline capture.",
    )
    parser.add_argument(
        "--system_visibility_mode",
        default=0,
        type=int,
        help="Enable system process mapping by probing the host machine.",
    )
    parser.add_argument(
        "--system_visibility_poll_ms",
        default=100,
        type=int,
        help="Set the polling interval in milliseconds for system process mapping feature (0 is the maximum achievable rate).",
    )

    args = parser.parse_args()



    online_streamer = NFStreamer(
        source=args.source
    )

    db = DatabaseManager()
    print(f"Start parsing ....")
    for flow in online_streamer:
        print("new flow")
        db.create_nflow_record(flow)
        print(flow)

    # print(args)


if __name__ == "__main__":
    main()
