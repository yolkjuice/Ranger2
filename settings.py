class Settings(object):
	"""存储游戏《外星人入侵》所有设置的类"""

	def __init__(self):
		super(Settings, self).__init__()
		# 屏幕设置
		self.screen_width = 1250
		self.screen_height = 750
		self.bg_color = (230, 230, 230)

		# 飞船设置
		self.ship_speed = 0.5
		# self.ship_speed = 1.5
		self.ship_limit = 3

		# 子弹设置
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (100, 100, 100)
		self.bullet_allowed = 3

		# 外星人设置
		self.alien_speed = 0.5
		self.fleet_drop_speed = 8
		# 1表示右移，-1表示左移
		self.fleet_direction = 1
