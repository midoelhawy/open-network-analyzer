
# Open Network Analyzer 🚀

> **⚠️ This project is under active development and not yet complete!**  

Real-time network traffic analysis with dynamic configurability and flexibility for customization.

## Tasks:

1. [X] **Support saving historical data on SQL, ClickHouse, or other databases.**
2. [ ] **Implement dynamic configurable workspace**
   - Support consumer queues to enable real-time traffic consumption by other applications.
3. [ ] **Add a queue to avoid database stress and other runtime errors**
4. [ ] **Avoid data loss by managing database save operations**
5. [ ] **Add REST API**
6. [ ] **Support Docker**
7. [ ] **Support detecting malicious requests via blacklisted IPs**
8. [ ] **Highlight unencrypted traffic**
9. [ ] **Allow configuration of alerts based on specific rules**
   - Users can define custom alert rules to trigger notifications based on network traffic patterns, specific IPs, protocol types, or anomalies.

## Debug

If you need to debug the project with your live network interface, you need to add the capability `cap_net_raw=eip` to the `python3` binary by running the following command:

```bash
sudo setcap cap_net_raw=eip /usr/bin/python3.10
```

Next, you can run the project with: 

```bash
/usr/bin/python3.10 ./main.py --source wlp3s0
```

**THANKS TO [nfstream Python framework](https://www.nfstream.org/) MAINTAINERS ❤️**
