#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ConsoleIn.py
 @brief ModuleDescription
 @date $Date$


"""
import OpenRTM_aist
import RTC
import sys
import time
sys.path.append(".")

# Import RTM module


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
consolein_spec = ["implementation_id", "ConsoleIn",
                  "type_name",		 "ConsoleIn",
                  "description",	   "ModuleDescription",
                  "version",		   "1.0.0",
                  "vendor",			"Ruchi",
                  "category",		  "Category",
                  "activity_type",	 "STATIC",
                  "max_instance",	  "1",
                  "language",		  "Python",
                  "lang_type",		 "SCRIPT",
                  ""]
# </rtc-template>

##
# @class ConsoleIn
# @brief ModuleDescription
#
#


class ConsoleIn(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_Out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
		"""
        self._OutOut = OpenRTM_aist.OutPort("Out", self._d_Out)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">

        # </rtc-template>

    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # formaer rtc_init_entry()
    #
    # @return RTC::ReturnCode_t
    #
    #

    def onInitialize(self):
        # Bind variables and configuration variable

        # Set InPort buffers

        # Set OutPort buffers
        self.addOutPort("Out", self._OutOut)

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports

        return RTC.RTC_OK

    ###
    ##
    # The finalize action (on ALIVE->END transition)
    # formaer rtc_exiting_entry()
    ##
    # @return RTC::ReturnCode_t
    #
    ##
    # def onFinalize(self):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The startup action when ExecutionContext startup
    # former rtc_starting_entry()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onStartup(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The shutdown action when ExecutionContext stop
    # former rtc_stopping_entry()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onShutdown(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The activated action (Active state entry action)
    # former rtc_active_entry()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onActivated(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The deactivated action (Active state exit action)
    # former rtc_active_exit()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onDeactivated(self, ec_id):
    #
    # return RTC.RTC_OK

    ##
    #
    # The execution action that is invoked periodically
    # former rtc_active_do()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        print("Please input data: ", end="")
        self._d_Out.data = input()

        OpenRTM_aist.setTimestamp(self._d_Out)
        self._OutOut.write()
        return RTC.RTC_OK

    ###
    ##
    # The aborting action when main logic error occurred.
    # former rtc_aborting_entry()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onAborting(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The error action in ERROR state
    # former rtc_error_do()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onError(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The reset action that is invoked resetting
    # This is same but different the former rtc_init_entry()
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onReset(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The state update action that is invoked after onExecute() action
    # no corresponding operation exists in OpenRTm-aist-0.2.0
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##

    ##
    # def onStateUpdate(self, ec_id):
    #
    # return RTC.RTC_OK

    ###
    ##
    # The action that is invoked when execution context's rate is changed
    # no corresponding operation exists in OpenRTm-aist-0.2.0
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onRateChanged(self, ec_id):
    #
    # return RTC.RTC_OK


def ConsoleInInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=consolein_spec)
    manager.registerFactory(profile,
                            ConsoleIn,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    ConsoleInInit(manager)

    # Create a component
    comp = manager.createComponent("ConsoleIn")


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == "__main__":
    main()
