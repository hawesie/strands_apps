#!/usr/bin/env python

from __future__ import with_statement 
import rospy

class TearDownAtNodes(object):
	""" 
	"""
	def __init__(self, tear_down_nodes = []):
		super(TearDownAtNodes, self).__init__()
		
		self.tear_down_nodes = set(tear_down_nodes)
		self.launch_files_up = False		
        
        rospy.Subscriber('current_node', String, self._update_topological_location, queue = 1)

    def _update_topological_location(self, node):
    	if node.data in self.tear_down_nodes:
    		if self.launch_files_up:
    			rospy.loginfo('Tearing down launch files ')
    	elif not self.launch_files_up:
    		rospy.loginfo('Bringing launch files up')

if __name__ == '__main__':

	tear_down_nodes = ['ChargingPoint', 'WayPoint1']

    executor = TearDownAtNodes(tear_down_nodes = tear_down_nodes)        
    rospy.spin()
