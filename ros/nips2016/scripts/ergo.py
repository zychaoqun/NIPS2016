#!/usr/bin/env python

import rospy
from nips2016.ergo import Ergo

rospy.init_node('ergo')
Ergo().run()
