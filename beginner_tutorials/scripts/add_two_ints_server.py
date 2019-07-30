#!/usr/bin/env python
<<<<<<< HEAD
=======

>>>>>>> 71e5b7f0fff7d726bb565b76372467c921f67281
from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
<<<<<<< HEAD
	print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
	return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
        rospy.init_node('add_two_ints_server')
        s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
        print "Ready to add two ints."
        rospy.spin()

if __name__ == "__main__":
        add_two_ints_server()
=======
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
>>>>>>> 71e5b7f0fff7d726bb565b76372467c921f67281
