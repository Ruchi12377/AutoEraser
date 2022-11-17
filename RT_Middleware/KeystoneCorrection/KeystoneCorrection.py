#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file KeystoneCorrection.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
from PIL import Image, ImageTk
import cv2
import numpy
import numpy as np
import statistics
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
keystonecorrection_spec = ["implementation_id", "KeystoneCorrection", 
         "type_name",         "KeystoneCorrection", 
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
# @class KeystoneCorrection
# @brief ModuleDescription
# 
# 
# </rtc-template>
class KeystoneCorrection(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_ImageIn = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
        """
        """
        self._ImageInIn = OpenRTM_aist.InPort("ImageIn", self._d_ImageIn)
        self._d_ImageOut = OpenRTM_aist.instantiateDataType(RTC.CameraImage)
        """
        """
        self._ImageOutOut = OpenRTM_aist.OutPort("ImageOut", self._d_ImageOut)


		


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
        self.addInPort("ImageIn",self._ImageInIn)
		
        # Set OutPort buffers
        self.addOutPort("ImageOut",self._ImageOutOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    def mousePoints(self,event, x, y, flags, params):
        print("mouspoints!!!!!!")
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x,y)
            self.circles[self.counter] = x,y
            self.counter = self.counter + 1
            print(self.circles)
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
	
    ###
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
        self.Acceptanceimg = []
        self.counter = 0
        self.circles = np.zeros((4,2), np.int)
        self.point1 = []
        self.point2 = []
        self.point3 = []
        self.point4 = []
        self.pointx = []
        self.pointy = []
        self.pointul = []
        self.pointbl = []
        self.pointur = []
        self.pointbr = []
        self.pointleft = []
        self.pointright = []
        self.point_synthesis = []
        self.point_synthesis_numpy = []
        self.img_correction = None
        self.img_jugge = 0

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
        if self._ImageInIn.isNew(): #新しいデータが来たか確認
            print("imagein!!!")
            # バッファを読み込み、CV2に変換
            rawImage = self._ImageInIn.read()
            self.Acceptanceimg.append(numpy.frombuffer(rawImage.pixels, numpy.uint8).reshape(
                (rawImage.height, rawImage.width, 3)))
            self.Acceptanceimg[0] = cv2.cvtColor(self.Acceptanceimg[0], cv2.COLOR_BGRA2BGR)    
            self.img = self.Acceptanceimg[0]


            if self.counter ==4 :
                #4点が順不同の場合に整列する処理
                self.point1 = self.circles[0].tolist()
                self.point2 = self.circles[1].tolist()
                self.point3 = self.circles[2].tolist()
                self.point4 = self.circles[3].tolist()
                self.pointx.append(self.point1[0])
                self.pointx.append(self.point2[0])
                self.pointx.append(self.point3[0])
                self.pointx.append(self.point4[0])
                self.pointy.append(self.point1[1])
                self.pointy.append(self.point2[1])
                self.pointy.append(self.point3[1])
                self.pointy.append(self.point4[1])

                #x軸、y軸を比較して、4隅を特定
                for num,point in enumerate(self.pointx):
                    if point <= statistics.mean(self.pointx) and self.pointy[num] <= statistics.mean(self.pointy):
                        self.pointul.append(self.pointx[num])
                        self.pointul.append(self.pointy[num])
                    elif point >= statistics.mean(self.pointx) and self.pointy[num] <= statistics.mean(self.pointy):
                        self.pointur.append(self.pointx[num])
                        self.pointur.append(self.pointy[num])
                    elif point <= statistics.mean(self.pointx) and self.pointy[num] >= statistics.mean(self.pointy):
                        self.pointbl.append(self.pointx[num])
                        self.pointbl.append(self.pointy[num])
                    elif point >= statistics.mean(self.pointx) and self.pointy[num] >= statistics.mean(self.pointy):
                        self.pointbr.append(self.pointx[num])
                        self.pointbr.append(self.pointy[num])
                        
                self.point_synthesis.append(self.pointul)
                self.point_synthesis.append(self.pointur)
                self.point_synthesis.append(self.pointbl)
                self.point_synthesis.append(self.pointbr)
                
                #台形補正
                for num,dl in enumerate(self.point_synthesis):
                    self.point_synthesis[num] = [dl[0],dl[1]]
                    self.point_synthesis_numpy = np.array(self.point_synthesis)

                #画像のサイズを設定
                width , height = 1500, 500 #本システムの場合はホワイトボードの縦横比に合わせる
                pts1 = np.float32([self.point_synthesis_numpy[0],self.point_synthesis_numpy[1],self.point_synthesis_numpy[2],self.point_synthesis_numpy[3]])
                pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
                matrix = cv2.getPerspectiveTransform(pts1,pts2)
                imgoutput = cv2.warpPerspective(self.img, matrix,(width, height))
                #cv2.imshow('Output image', imgoutput)
                self.img_jugge = 1

                for x in range(0, 4):
                    cv2.circle(self.img, (self.circles[x][0], self.circles[x][1]), 3, (0, 255, 0), cv2.FILLED)

                if self.img_jugge == 1:

                    self._d_ImageOut.width = imgoutput.shape[1]
                    self._d_ImageOut.height = imgoutput.shape[0]
                    self._d_ImageOut.format = 'jpg'
                    self._d_ImageOut.pixels = imgoutput.tobytes()

                    self._ImageOutOut.write()
                    

            cv2.imshow('Original image', self.img)
            cv2.setMouseCallback('Original image', self.mousePoints)

            cv2.waitKey(1)
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
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
	



def KeystoneCorrectionInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=keystonecorrection_spec)
    manager.registerFactory(profile,
                            KeystoneCorrection,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    KeystoneCorrectionInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("KeystoneCorrection" + args)

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

