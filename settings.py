class Settings(object):
	"""存储游戏《外星人入侵》所有设置的类"""

	def __init__(self):
		super(Settings, self).__init__()
		# 屏幕设置
		self.screen_width = 1000
		self.screen_height = 595
		self.bg_color = (230, 230, 230)

		# 飞船设置
		self.ship_speed = 1.5
		# self.ship_speed = 1.5

		# 子弹设置
		self.bullet_speed = 1
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (100, 100, 100)
		self.bullet_allowed = 5

		# 外星人设置
		self.alien_speed = 1.0
		self.fleet_drop_speed = 5
		# 1表示右移，-1表示左移
		self.fleet_direction = 1
