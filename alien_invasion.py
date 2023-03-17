import sys
from time import sleep
import pygame

from settings import Settings
from gamestats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import ScoreBoard

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
		# 全屏
		# self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		# self.settings.width = self.screen.get_rect().width
		# self.settings.width = self.screen.get_rect().height

		# 窗口标题
		pygame.display.set_caption("Aline Invasion")

		# 创建一个存储游戏统计信息的实例
		self.stats = GameStats(self)

		# 初始化飞船
		self.ship = Ship(self)

		# 初始化子弹编组
		self.bullets = pygame.sprite.Group()

		# 初始化外星人编组
		self.aliens = pygame.sprite.Group()
		self._create_fleet()

		# 创建一个Play按钮
		self.play_button = Button(self, 'Play')

		# 创建一个记分牌
		self.sb = ScoreBoard(self)


	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			# run_game重构为多个辅助方法，以'_'开头
			self._check_event()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()


	def _update_aliens(self):
		"""检测是否有外星人位于屏幕边缘
			更新所有外星人的位置"""
		self._check_fleet_eages()
		self.aliens.update()

		# 检测外星人和飞船碰撞
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# 检查是否有外星人到达底部
		self._check_aliens_bottom()
		pass


	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# 像飞船被撞一样处理
				self._ship_hit()
		pass


	def _ship_hit(self):
		"""响应外星人和飞船碰撞"""

		if self.stats.ships_left > 0:
			# 飞船剩余数量-1
			self.stats.ships_left -= 1

			# 清空子弹和外星人
			self.bullets.empty()
			self.aliens.empty()

			# 创建新的外星人并将飞船放在屏幕底端
			self._create_fleet()
			self.ship.center_ship()

			# 暂停
			sleep(0.5)
		else:
			self.stats.game_active = False
			# 让鼠标可见
			pygame.mouse.set_visible(True)


	def _check_fleet_eages(self):
		"""有外星人到达屏幕边缘时采取措施"""
		for alien in self.aliens.sprites():
			if alien.check_eages():
				self._change_fleet_direction()
				break
		pass


	def _change_fleet_direction(self):
		"""将外星人群下移并改变左右方向"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1
		pass


	def _check_event(self):
			# 监视键盘和鼠标事件。
			for event in pygame.event.get():
				# 退出
				if event.type == pygame.QUIT:
					sys.exit()

				# 移动飞船
				# 按下
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				# 松开
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
				# 鼠标点击
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					self._check_play_button(mouse_pos)


	def _check_play_button(self, mouse_pos):
		"""在点击Play按钮时开始新游戏"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		# 非活动状态才允许按Play按钮
		if button_clicked and not self.stats.game_active:
			# 重置游戏设置
			self.settings.initialize_dynamic_settings()
			# 重置游戏统计信息
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()


			# 清空外星人和子弹
			self.aliens.empty()
			self.bullets.empty()

			# 绘制新外星人群并居中放置飞船
			self._create_fleet()
			self.ship.center_ship()

			# 隐藏鼠标
			pygame.mouse.set_visible(False)


	def _update_bullets(self):
		"""更新子弹的位置并删除消失的子弹"""
		# 更新子弹的位置
		self.bullets.update()

		# 删除消失的子弹
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		# print(len(self.bullets))

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		# 检查是否有子弹和外星人碰撞
		# 	如果有，删除相应子弹和外星人
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score()

		if not self.aliens:
			# 删除所有子弹并生成新的外星人群
			self.bullets.empty()
			self._create_fleet()
			# 提高游戏等级
			self.settings.increase_speed()
			self.stats.level += 1
			self.sb.prep_level()
		pass


	def _create_fleet(self):
		"""创建外星人群"""
		# 创建一个外星人并计算一行可以容纳多少外星人
		# 外星人的间距为外星人的宽度
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# 计算屏幕容纳多少行外星人
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
			(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# 创建外星人群
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
		pass


	def _create_alien(self, alien_number, row_number):
		# 创建一个外星人并加入当前行
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)
		pass


	def _update_screen(self):
			# 填充屏幕
			self.screen.fill(self.settings.bg_color)
			# 绘制飞船
			self.ship.blitme()
			# 绘制所有子弹
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			# 绘制外星人群
			self.aliens.draw(self.screen)
			# 绘制记分牌
			self.sb.show_score()

			# 非活动状态绘制Play按钮
			if not self.stats.game_active:
				self.play_button.draw_button()

			# 让最近绘制的屏幕可见
			pygame.display.flip()


	def _check_keydown_events(self, event):
		# 右移
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = True
		# 左移
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = True
		# 上移
		elif event.key == pygame.K_UP:
			self.ship.move_top = True
		# 下移
		elif event.key == pygame.K_DOWN:
			self.ship.move_bottom = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		# 按数字键盘033   键退出
		elif event.key == pygame.K_KP0:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = False
		elif event.key == pygame.K_UP:
			self.ship.move_top = False
		elif event.key == pygame.K_DOWN:
			self.ship.move_bottom = False


	def _fire_bullet(self):
		"""创建一颗新子弹并加入编组"""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


if __name__ == '__main__':
	# 创建游戏实例并运行游戏
	ai = AlienInvsion()
	ai.run_game()
