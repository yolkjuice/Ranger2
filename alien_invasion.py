import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvsion(object):
	"""管理游戏资源和行为的类"""

	def __init__(self):
		"""初始化游戏并创建游戏资源"""
		super(AlienInvsion, self).__init__()
		pygame.init()
		self.settings = Settings()

		# 初始化屏幕
		self.screen = pygame.display.set_mode((
			self.settings.screen_width, self.settings.screen_height))

		# 窗口标题
		pygame.display.set_caption("Aline Invasion")

		# 初始化飞船
		self.ship = Ship(self)


	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			# 监视键盘和鼠标事件。
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# 填充屏幕
			self.screen.fill(self.settings.bg_color)

			# 绘制飞船
			self.ship.blitme()

			# 让最近绘制的屏幕可见
			pygame.display.flip()

if __name__ == '__main__':
	# 创建游戏实例并运行游戏
	ai = AlienInvsion()
	ai.run_game()
