﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Pump.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

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
pump_spec = ["implementation_id", "Pump",
             "type_name",         "Pump",
             "description",       "ModuleDescription",
             "version",           "1.0.0",
             "vendor",            "VenderName",
             "category",          "Category",
             "activity_type",     "STATIC",
             "max_instance",      "1",
             "language",          "Python",
             "lang_type",         "SCRIPT",
             ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class Pump
# @brief ModuleDescription
#
#
# </rtc-template>


class Pump(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_WaterAmount = OpenRTM_aist.instantiateDataType(RTC.TimedUShort)
        """
        """
        self._WaterAmountIn = OpenRTM_aist.InPort(
            "WaterAmount", self._d_WaterAmount)
        self._d_PumpWaterAmount = OpenRTM_aist.instantiateDataType(
            RTC.TimedString)
        """
        """
        self._PumpWaterAmountOut = OpenRTM_aist.OutPort(
            "PumpWaterAmount", self._d_PumpWaterAmount)

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">

        # </rtc-template>

    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    #
    # @return RTC::ReturnCode_t
    #
    #

    def onInitialize(self):
        # Bind variables and configuration variable

        # Set InPort buffers
        self.addInPort("WaterAmount", self._WaterAmountIn)

        # Set OutPort buffers
        self.addOutPort("PumpWaterAmount", self._PumpWaterAmountOut)

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports

        return RTC.RTC_OK

    ###
    ##
    # The finalize action (on ALIVE->END transition)
    ##
    # @return RTC::ReturnCode_t
    #
    ##
    # def onFinalize(self):
    #

    #    return RTC.RTC_OK

    ###
    ##
    # The startup action when ExecutionContext startup
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The shutdown action when ExecutionContext stop
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK

    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):

        return RTC.RTC_OK

    ##
    #
    # The deactivated action (Active state exit action)
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
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if (self._WaterAmountIn.isNew()):  # 新しいデータが来たか確認
            self._d_WaterAmount = self._WaterAmountIn.read()  # 値を読み込む
            self._d_PumpWaterAmount.data = "Pump " + self._d_WaterAmount.data
            self._PumpWaterAmountOut.write()
        return RTC.RTC_OK

    ###
    ##
    # The aborting action when main logic error occurred.
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The error action in ERROR state
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onError(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The reset action that is invoked resetting
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The state update action that is invoked after onExecute() action
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##

    ##
    # def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK

    ###
    ##
    # The action that is invoked when execution context's rate is changed
    ##
    # @param ec_id target ExecutionContext Id
    ##
    # @return RTC::ReturnCode_t
    ##
    ##
    # def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK


def PumpInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=pump_spec)
    manager.registerFactory(profile,
                            Pump,
                            OpenRTM_aist.Delete)


def MyModuleInit(manager):
    PumpInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""

    # Create a component
    comp = manager.createComponent("Pump" + args)


def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()


if __name__ == "__main__":
    main()
