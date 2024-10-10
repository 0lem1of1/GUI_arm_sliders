from tkinter import *
import rospy
from sensors_msgs.msg import JointState


class JointSlidersGUI(object):
	"""docstring for JointSlidersGUI"""
	def __init__(self, root):
		self.root = root
		self.root.title("Joint Control GUI")

		#ROS publisher
		rospy.init_node('joint_slider_gui',anonymous=True)
		self.pub = rospy.Publisher('/joint_states',JointState,queue_size=10)
	



		#creting sliders
		self.joint_values = [DoubleVar() for _ in range(6)]
		self.sliders = []

		for i in range(6):
			slider = Scale(root, from_=-3.14, to=3.14, resolution=0.01,
				orient=HORIZONTAL, variable=self.joint_values[i],
				label=f'Joint {i+1}', length=400)

			slider.pack()
			self.sliders.append(slider)


		# Button to publish the joint values
		publish_button = Button(root, text="Publish Joint States",command=self.print_joint_values)
		publish_button.pack()

	def publish_joint_states(self):
		joint_state= JointState()

		joint_state.name = [f'joint_{i+1}' for i in range(6)]

		joint_state.positions = [value.get() for value in joint_values]

		joint_state.stamp = rospy.Time.now()

		self.pub.publish(joint_state)
		rospy.loginfo("Published Joint States: %s", joint_state.position)



if __name__ == "__main__":
	
	try:
		root = Tk()
		gui = JointSlidersGUI(root)
		root.mainloop()
	except rospy.ROSInterruptException:
		pass
