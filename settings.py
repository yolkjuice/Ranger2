class Settings(object):
	"""存储游戏《外星人入侵》所有设置的类"""

	def __init__(self):
		super(Settings, self).__init__()
		"""初始化游戏的静态设置"""
		# 屏幕设置
		self.screen_width = 1250
		self.screen_height = 750
		self.bg_color = (230, 230, 230)

		# 飞船设置
		# self.ship_speed = 1.5
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (100, 100, 100)
		self.bullet_allowed = 3

		# 外星人设置
		self.fleet_drop_speed = 20

		# 初始化游戏动态设置
		# 加快游戏节奏的倍数
		self.speedup_scale = 1.1
		# 外星人分数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.ship_speed = 0.5
		self.bullet_speed = 1.5
		self.alien_speed = 0.3

		# 1表示右移，-1表示左移
		self.fleet_direction = 1

		# 记分
		self.alien_points = 50
		pass


	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		# print(self.alien_points)
		pass
