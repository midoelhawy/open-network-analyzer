import uuid
from nfstream import NFPlugin
import time

from lib.db.DatabaseManager import DatabaseManager
from lib.db.NFlowInstance import FLOW_STATUS
class FlowTracker(NFPlugin):
    """ FlowTracker class: Main entry point to extend NFStream """
    dbManager:DatabaseManager
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
        

    def on_init(self, packet, flow):
        flow.udps.flow_uuid = uuid.uuid4()
        flow.udps.last_db_update = time.time()
        print(f"on_init => Flow ID: {flow.id}")
        self.dbManager.add_flow(flow,FLOW_STATUS.INIT)
        
        

    def on_update(self, packet, flow):
        """
        on_update(self, packet, flow): Method called to update each flow 
                                       with its belonging packet.
        """
        #print(f"on_update => Flow ID: {flow.udps.flow_uuid},lastDbUpdate: {flow.udps.last_db_update}")
        
        # check if last db update is more then 100 seconds ago 
        if time.time() - flow.udps.last_db_update > 10:
            # update database
            print(f"update database")
            flow.udps.last_db_update = time.time()
            self.dbManager.add_flow(flow,FLOW_STATUS.ACTIVE)

    def on_expire(self, flow):
        """
        on_expire(self, flow): Method called at flow expiration.
        """
        print(f"on_expire => Flow UUID: {flow.udps.flow_uuid}")
        self.dbManager.add_flow(flow,FLOW_STATUS.FINISHED)

    def cleanup(self):
        """
        cleanup(self): Method called for plugin cleanup.
        """
        print(f"cleanup")
