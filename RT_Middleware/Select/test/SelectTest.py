#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file SelectTest.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

import Select

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
selecttest_spec = ["implementation_id", "SelectTest", 
         "type_name",         "SelectTest", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "Ruchi", 
         "category",          "GUI", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.Width", "800",
         "conf.default.Height", "450",

         "conf.__widget__.Width", "text",
         "conf.__widget__.Height", "text",
         "conf.__constraints__.Width", "400<=x<=1600",
         "conf.__constraints__.Height", "225<=x<=900",

         "conf.__type__.Width", "int",
         "conf.__type__.Height", "int",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class SelectTest
# @brief ModuleDescription
# 
# 
# </rtc-template>
class SelectTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_StartPoint = OpenRTM_aist.instantiateDataType(RTC.TimedPoint2D)
        """
         - Semantics: Percentage from top left
         - Unit: ratio
        """
        self._StartPointIn = OpenRTM_aist.InPort("StartPoint", self._d_StartPoint)
        self._d_EndPoint = OpenRTM_aist.instantiateDataType(RTC.TimedPoint2D)
        """
         - Semantics: Percentage from top left
         - Unit: ratio
        """
        self._EndPointIn = OpenRTM_aist.InPort("EndPoint", self._d_EndPoint)
        self._d_ShowImage = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
        """
        Select target image
        """
        self._ShowImageOut = OpenRTM_aist.OutPort("ShowImage", self._d_ShowImage)
        self._d_CompeteMotion = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._CompeteMotionOut = OpenRTM_aist.OutPort("CompeteMotion", self._d_CompeteMotion)
        self._d_StatusCode = OpenRTM_aist.instantiateDataType(RTC.TimedUShort)
        """
        """
        self._StatusCodeOut = OpenRTM_aist.OutPort("StatusCode", self._d_StatusCode)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  Width
         - DefaultValue: 800
        """
        self._Width = [800]
        """
        
         - Name:  Height
         - DefaultValue: 450
        """
        self._Height = [450]
        
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
        self.bindParameter("Width", self._Width, "800")
        self.bindParameter("Height", self._Height, "450")
        
        # Set InPort buffers
        self.addInPort("StartPoint",self._StartPointIn)
        self.addInPort("EndPoint",self._EndPointIn)
        
        # Set OutPort buffers
        self.addOutPort("ShowImage",self._ShowImageOut)
        self.addOutPort("CompeteMotion",self._CompeteMotionOut)
        self.addOutPort("StatusCode",self._StatusCodeOut)
        
        # Set service provider to Ports
        
        # Set service consumers to Ports
        
        # Set CORBA Service Ports
        
        return RTC.RTC_OK
    
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #
    #    return RTC.RTC_OK
    
    #    ##
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
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
    
        return RTC.RTC_OK
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("SelectTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def SelectTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=selecttest_spec)
    manager.registerFactory(profile,
                            SelectTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SelectTestInit(manager)
    Select.SelectInit(manager)

    # Create a component
    comp = manager.createComponent("SelectTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

