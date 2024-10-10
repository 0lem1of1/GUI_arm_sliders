from tkinter import *


class JointSlidersGUI(object):
	"""docstring for JointSlidersGUI"""
	def __init__(self, root):
		self.root = root
		self.root.title("Joint Control GUI")

		#ROS publisher

	



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

	def print_joint_values(self):
		joint_positions = [value.get() for value in self.joint_values]
		print("Joint Positions:", joint_positions)

if __name__ == "__main__":
	
	root = Tk()
	gui = JointSlidersGUI(root)
	root.mainloop()
