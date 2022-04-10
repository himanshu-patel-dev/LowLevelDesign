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

print(s1 is s2)
print(s1.ans == s2.ans)
