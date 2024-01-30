# Open network analyzer

Thi is a personal project (for now)

## Tasks:

1. [ ] **Implement dynamic configurable workspace**

   - support reading from live network interface or pcap
   - support events action on live python or bash script
     - ON_FLOW_START
     - ON_FLOW_END
     - ON_L7_APP_DETECT
     - ON CLEAN
     - ECC...
2. [ ] **Support live flows analytics**

   - support the access to active flows before saving in historical db
3. [ ] **Support saving historical data on SQL, ClickHouse**

   - save flows in persistent db
4. [ ] **Add REST API**
5. [ ] **Support Docker**

## Debug

if you need to debug the project with your live nwtwork interface you need add the capability `cap_net_raw=eip` to  `python3` binary by running the folwing command :

```bash
sudo setcap cap_net_raw=eip /usr/bin/python3.10
```

Next you can run the project by : `/usr/bin/python3.10 ./main.py --source wlp3s0`



**THANKS TO [nfstream python framework](https://www.nfstream.org/) MAINTAINERS <3**
