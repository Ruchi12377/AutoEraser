﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file Select.py
 @brief ModuleDescription
 @date $Date$


"""
from ast import While
import sys
import time
import cv2
import numpy
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
select_spec = ["implementation_id", "Select",
		 "type_name",         "Select",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "Ruchi",
		 "category",          "GUI",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class Select
# @brief ModuleDescription
#
#
class Select(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_ShowImage = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
		"""
		Select target image
		"""
		self._ShowImageIn = OpenRTM_aist.InPort("ShowImage", self._d_ShowImage)
		self._d_CompeteMotion = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._CompeteMotionIn = OpenRTM_aist.InPort("CompeteMotion", self._d_CompeteMotion)
		self._d_StatusCode = OpenRTM_aist.instantiateDataType(RTC.TimedUShort)
		"""
		"""
		self._StatusCodeIn = OpenRTM_aist.InPort("StatusCode", self._d_StatusCode)
		self._d_StartPoint = OpenRTM_aist.instantiateDataType(RTC.Point2D)
		"""
		 - Semantics: Percentage from top left
		 - Unit: ratio
		"""
		self._StartPointOut = OpenRTM_aist.OutPort("StartPoint", self._d_StartPoint)
		self._d_EndPoint = OpenRTM_aist.instantiateDataType(RTC.Point2D)
		"""
		 - Semantics: Percentage from top left
		 - Unit: ratio
		"""
		self._EndPointOut = OpenRTM_aist.OutPort("EndPoint", self._d_EndPoint)





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
		self.addInPort("ShowImage",self._ShowImageIn)
		self.addInPort("CompeteMotion",self._CompeteMotionIn)
		self.addInPort("StatusCode",self._StatusCodeIn)

		# Set OutPort buffers
		self.addOutPort("StartPoint",self._StartPointOut)
		self.addOutPort("EndPoint",self._EndPointOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

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
		self.img = [None]
	
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
		#this method is only check and set img then show img
		#check in port
		if(self._ShowImageIn.isNew()):
			#in port has new buffer
			#read buffer and reshape as cv2 img
			rawImage = self._ShowImageIn.read()
			self.img[0] = numpy.frombuffer(rawImage.pixels, numpy.uint8).reshape((rawImage.height, rawImage.width, 3))
			self.img[0] = cv2.cvtColor(self.img[0], cv2.COLOR_BGRA2BGR)

		cv2.imshow('WhiteBoard', self.img[0])
		cv2.waitKey(1)
		
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def SelectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=select_spec)
    manager.registerFactory(profile,
                            Select,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SelectInit(manager)

    # Create a component
    comp = manager.createComponent("Select")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

