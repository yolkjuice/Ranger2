class Settings(object):
	"""存储游戏《外星人入侵》所有设置的类"""

	def __init__(self):
		super(Settings, self).__init__()
		# 屏幕设置
		self.screen_width = 1000
		self.screen_height = 595
		self.bg_color = (230, 230, 230)

		# 飞船设置
		self.ship_speed = 0.5
		# self.ship_speed = 1.5
