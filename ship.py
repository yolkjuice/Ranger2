import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""管理飞船的类"""

	def __init__(self, ai_game):
		"""初始化飞船并设置其位置"""
		super(Ship, self).__init__()
		# 用主屏幕做参考
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# 对于每艘新飞船，一开始都放在屏幕低端之间
		self.rect.midbottom = self.screen_rect.midbottom

		# 移动标志
		self.move_right = False
		self.move_left = False
		self.move_top = False
		self.move_bottom = False

		# 飞船移动位置
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
		# self.screen.fill(230, 0, 0)


	def update(self):
		"""根据移动标志调整飞船位置"""
		# 先更新飞船移动位置
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed

		if self.move_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		if self.move_top and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.ship_speed

		if self.move_bottom and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# 再更新对象rect.x
		self.rect.x = self.x
		self.rect.y = self.y


	def center_ship(self):
		"""让飞船在屏幕底端居中"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		pass

# self.image 对应飞船的图像
# self.rect 对应飞船占据的空间
# 	占据空间又有大小、形状、位置
# 		形状和图像有关
# 		位置和主屏幕有关
# 		大小和主屏幕有关
# screen为对象
