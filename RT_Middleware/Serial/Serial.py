﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file Serial.py
 @brief Serial communication
 @date $Date$


"""
import OpenRTM_aist
import RTC
import sys
import time
import serial
from serial.tools import list_ports
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
serial_spec = ["implementation_id", "Serial",
               "type_name",		 "Serial",
               "description",	   "Serial communication",
               "version",		   "1.0.0",
               "vendor",			"Ruchi",
               "category",		  "Category",
               "activity_type",	 "STATIC",
               "max_instance",	  "1",
               "language",		  "Python",
               "lang_type",		 "SCRIPT",
               "conf.default.Port", "COM3",
               "conf.default.Baudrate", "9600",

               "conf.__widget__.Port", "text",
               "conf.__widget__.Baudrate", "text",
               "conf.__constraints__.Baudrate", "x>0",

               "conf.__type__.Port", "string",
               "conf.__type__.Baudrate", "int",

               ""]
# </rtc-template>

##
# @class Serial
# @brief Serial communication
#
#


class Serial(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_wData = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
		"""
        self._WriteIn = OpenRTM_aist.InPort("Write", self._d_wData)
        self._d_rData = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
		"""
        self._ReadOut = OpenRTM_aist.OutPort("Read", self._d_rData)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """

		 - Name:  Port
		 - DefaultValue: COM3
		"""
        self._Port = ['COM3']
        """

		 - Name:  Baudrate
		 - DefaultValue: 9600
		"""
        self._Baudrate = [9600]

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
        self.bindParameter("Port", self._Port, "COM3")
        self.bindParameter("Baudrate", self._Baudrate, "9600")

        # Set InPort buffers
        self.addInPort("Write", self._WriteIn)

        # Set OutPort buffers
        self.addOutPort("Read", self._ReadOut)

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

    ##
    #
    # The activated action (Active state entry action)
    # former rtc_active_entry()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        devices = [info.device for info in list_ports.comports()]
        # port is not found
        if ((self._Port[0] in devices) == False):
            print("port is not found :" + self._Port[0])
            print("please connect usb, or select a port below")
            for i in range(len(devices)):
                print("> " + devices[i])
            return RTC.RTC_OK

        self.ser = [serial.Serial()]
        self.ser[0].baudrate = self._Baudrate[0]
        self.ser[0].port = self._Port[0]
        self.ser[0].timeout = 1

        try:
            self.ser[0].open()
            print("port is opened : " + self._Port[0])
            return RTC.RTC_OK
        except:
            print("Can't open port : " + self._Port[0])

        return RTC.RTC_OK

    ##
    #
    # The deactivated action (Active state exit action)
    # former rtc_active_exit()
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):

        return RTC.RTC_OK

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
        if (self._WriteIn.isNew()):
            self.ser[0].write(str.encode(self._WriteIn.read().data))

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


def SerialInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=serial_spec)
    manager.registerFactory(profile,
                            Serial,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    SerialInit(manager)

    # Create a component
    comp = manager.createComponent("Serial")


def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == "__main__":
    main()
