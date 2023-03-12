import pygame.font

class Button(object):
	"""管理按钮的类"""
	def __init__(self, ai_game, msg):
		"""初始化按钮的属性"""
		super(Button, self).__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# 设置按钮的尺寸和其他属性
		self.width, self.height = 150, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# 创建按钮的矩形，并居中放置
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# 按钮的标签只添加一次
		self._prep_msg(msg)


	def _prep_msg(self, msg):
		"""将msg渲染成图像，并在按钮中居中放置"""
		self.msg_image = self.font.render(msg, True, self.button_color,
		 self.text_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		"""绘制按钮和文本"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		pass
