import pygame

class Ship(object):
	"""管理飞船的类"""

	def __init__(self, ai_game):
		"""初始化飞船并设置其位置"""
		super(Ship, self).__init__()
		# 用主屏幕做参考
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/space-158234_1280.bmp')
		self.rect = self.image.get_rect()

		# 对于每艘新飞船，一开始都放在屏幕低端之间
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
		# self.screen.fill(230, 0, 0)

# self.image 对应飞船的图像
# self.rect 对应飞船占据的空间
# 	占据空间又有大小、形状、位置
# 		形状和图像有关
# 		位置和主屏幕有关
# 		大小和主屏幕有关
# screen为对象
