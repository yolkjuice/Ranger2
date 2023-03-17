import pygame.font

class ScoreBoard(object):
	"""显示得分信息的类"""

	def __init__(self, ai_game):
		"""初始化显示的属性"""
		super(ScoreBoard, self).__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# 显示得分信息的文字的设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# 准备初始得分图像
		self.prep_score()

		# 准备最高分图像
		self.prep_high_score()

		# 准备游戏等级图像
		self.prep_level()


	def prep_score(self):
		"""将得分信息渲染成一幅图像"""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
		self.text_color, self.settings.bg_color)

		# 在屏幕右上角显示得分
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		pass


	def prep_high_score(self):
		"""将最高分信息渲染成一幅图像"""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
		self.text_color, self.settings.bg_color)

		# 在屏幕右上角显示得分
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
		pass


	def check_high_score(self):
		"""检查是否产生最高分"""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()
		pass


	def prep_level(self):
		"""将游戏等级渲染成图像"""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
			self.text_color, self.settings.bg_color)

		# 将游戏等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		pass


	def show_score(self):
		"""在屏幕上绘制得分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		pass
