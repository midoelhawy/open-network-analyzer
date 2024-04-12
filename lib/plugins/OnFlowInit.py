class OnFlowInit(object):
    """ OnFlowInit class: Main entry point to extend NFStream """
    def __init__(self, **kwargs):
        """
        NFPlugin Parameters:
        kwargs : user defined named arguments that will be stored as Plugin attributes
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def on_init(self, packet, flow):
        """
        on_init(self, packet, flow): Method called at flow creation.
        You must initiate your udps values if you plan to compute ones.
        Example: -------------------------------------------------------
                 flow.udps.magic_message = "NO"
                 if packet.raw_size == 40:
                    flow.udps.packet_40_count = 1
                 else:
                    flow.udps.packet_40_count = 0
        ----------------------------------------------------------------
        """
        
        print(f"on_init")

    def on_update(self, packet, flow):
        """
        on_update(self, packet, flow): Method called to update each flow 
                                       with its belonging packet.
        Example: -------------------------------------------------------
                 if packet.raw_size == 40:
                    flow.udps.packet_40_count += 1
        ----------------------------------------------------------------
        """
        print(f"on_update")

    def on_expire(self, flow):
        """
        on_expire(self, flow):      Method called at flow expiration.
        Example: -------------------------------------------------------
                 if flow.udps.packet_40_count >= 10:
                    flow.udps.magic_message = "YES"
        ----------------------------------------------------------------
        """
        print(f"on_expire")

    def cleanup(self):
        """
        cleanup(self):               Method called for plugin cleanup.
        Example: -------------------------------------------------------
                 del self.large_dict_passed_as_plugin_attribute
        ----------------------------------------------------------------
        """
        print(f"cleanup")