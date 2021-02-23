#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import math

class pub:
	def __init__(self):
		rospy.init_node('publisher',anonymous=True)
		self.pub=rospy.Publisher('publish_topic',PoseStamped,queue_size=10)
		self.rate=rospy.Rate(15)

	def run(self):
		points=PoseStamped()
		print(points)
		points.pose.position.x=0
		points.pose.position.y=0
		rate=rospy.Rate(15)
		points.header.frame_id="map"
		pointx=0
		pointy=0
		while not rospy.is_shutdown():
			if (points.pose.position.x==0&points.pose.position.y==0):
				while (points.pose.position.y!=8):
					points.pose.position.y=pointy
					pointy=pointy+1
					self.pub.publish(points)
					self.rate.sleep()
				while (points.pose.position.x!=8):
					points.pose.positon.x=pointx
					pointx=pointx+1
					self.pub.publish(points)
					self.rate.sleep()	
		
			elif (points.pose.position.x==8&points.pose.position.y==8):
				while (points.pose.position.y!=8):
					points.pose.position.y=pointy
					pointy=pointy+1
					self.pub.publish(points)
					self.rate.sleep()
				while (points.pose.position.x!=8):
					points.pose.positon.x=pointx
					pointx=pointx+1
					self.pub.publish(points)
					self.rate.sleep()	
if __name__ == '__main__':
	try:
		node=pub()
		node.run()
	except rospy.ROSInterruptException:
		pass
