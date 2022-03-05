class Singleton:
	ans = None

	@staticmethod
	def instance():
		if '_instance' not in Singleton.__dict__:
			Singleton._instance = Singleton()
		return Singleton._instance

s1 = Singleton.instance()
s2 = Singleton.instance()
s1.ans = 10

assert s1 is s2
assert s1.ans == s2.ans

print("Test Passed")
