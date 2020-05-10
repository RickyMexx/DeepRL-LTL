import numpy as np
import gym
from gym import spaces
import time
class RAEnv(gym.Env):
	metadata = {
		'render.modes': ['rgb_array'],
		'video.frames_per_second': 50
	}
	def __init__(self):
		self.action_space = spaces.Box(low=np.array([-1., -1.]), high=np.array([1., 1.]), dtype=np.float32)
		self.observation_space = spaces.Box(low=np.array([0., 0., -np.inf, -np.inf, 0., 0.]), high=np.array([1., 1., np.inf, np.inf, 1., 1.]), dtype=np.float32)
		self.viewer = None
		self._max_episode_steps = 1000
	def reset(self):
		self.h = 600
		self.w = 600
		self.r = 10
		self.tr = 30
		self.x = 0.5
		self.y = 1
		self.vx = 0
		self.vy = 0
		self.g = -0.5
		self.dt = 0.05
		self.ground_el = 1.1
		self.t1_x = 0.3
		self.t1_y = 0.3
		self.t2_x = 0.8
		self.t2_y = 0.6
		self.t1_crossed = False
		self.t2_crossed = False
		self.ball_circle = None
		self.ball_trans = None
		self.t1_circle = None
		self.t2_circle = None
		self.done = False
		self.episodes = 0
		if self.viewer  is not None:
			self.viewer.close()
			self.viewer = None
		return np.array([self.x, self.y, self.vx, self.vy, self.t1_crossed, self.t2_crossed])

	def render(self, mode='rgb_array'):
		if self.viewer is None:
			from gym.envs.classic_control import rendering
			self.viewer = rendering.Viewer(self.w, self.h)

			self.t1_circle = rendering.make_circle(self.tr)
			self.t1_circle.set_color(0, 0, 1)
			t1_trans = rendering.Transform(translation=(self.t1_x*self.w, self.t1_y*self.h))
			self.t1_circle.add_attr(t1_trans)
			self.viewer.add_geom(self.t1_circle)

			self.t2_circle = rendering.make_circle(self.tr)
			self.t2_circle.set_color(0, 0, 1)
			t2_trans = rendering.Transform(translation=(self.t2_x*self.w, self.t2_y*self.h))
			self.t2_circle.add_attr(t2_trans)
			self.viewer.add_geom(self.t2_circle)

			self.ball_circle = rendering.make_circle(self.r)
			self.ball_circle.set_color(1, 0, 0)
			self.ball_trans = rendering.Transform(translation=(self.x*self.w, self.y*self.h))
			self.ball_circle.add_attr(self.ball_trans)
			self.viewer.add_geom(self.ball_circle)

		if self.t1_crossed:
			self.t1_circle.set_color(0, 1, 0)
		if self.t2_crossed:
			self.t2_circle.set_color(0, 1, 0)

		self.ball_trans.set_translation(self.x*self.w, self.y*self.h)

		return self.viewer.render(return_rgb_array=mode == 'rgb_array')


	def step(self, a):
		reward = 0

		if not self.done:
			self.episodes += 1
			reward = -1
			ax, ay = np.clip(a, -1, 1)

			self.vx = self.vx + self.dt*ax
			self.vy = self.vy + self.dt*(ay + self.g)

			self.x = self.x + self.vx*self.dt + 0.5 * ax * self.dt**2
			self.y = self.y + self.vy*self.dt + 0.5 * (ay + self.g) * self.dt**2

			if self.episodes == self._max_episode_steps:
				reward = -100
				self.done = True
			if self.x < 0 or self.x > 1:
				reward = -100
				self.done = True
			if self.y < 0 or self.y > 1:
				reward = -100
				self.done = True

			self.y = np.clip(self.y, 0, 1)
			self.x = np.clip(self.x, 0, 1)

			if (self.x - self.t1_x)**2 + (self.y - self.t1_y)**2 <= (self.tr/self.w + self.r/self.w)**2:
				if not self.t1_crossed: reward = 100
				self.t1_crossed = True

			if (self.x - self.t2_x)**2 + (self.y - self.t2_y)**2 <= (self.tr/self.w + self.r/self.w)**2 and self.t1_crossed:
				if not self.t2_crossed: reward = 100
				self.t2_crossed = True

			if self.t1_crossed and self.t2_crossed:
				self.done=True

		return np.array([self.x, self.y, self.vx, self.vy, self.t1_crossed, self.t2_crossed]), reward, self.done, {}

	def close(self):
		if self.viewer  is not None:
			self.viewer.close()
			self.viewer = None