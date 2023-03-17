import json


class GameStats(object):
	"""跟踪游戏的统计信息"""

	def __init__(self, ai_game):
		"""初始化游戏信息"""
		super(GameStats, self).__init__()
		self.settings = ai_game.settings
		# 让游戏开始前/结束 处于非活动状态
		self.game_active = False
		# 最高分，无需重置
		self._get_high_score()
		self.reset_stats()
		

	def reset_stats(self):
		"""初始化游戏期间可能变化的统计信息"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1


	def _get_high_score(self):
		filename = 'high_score.json'
		try:
			with open(filename, 'r') as file_object:
				self.high_score = json.load(file_object)
		except FileNotFoundError as e:
			self.high_score = 0
			return None
			raise e