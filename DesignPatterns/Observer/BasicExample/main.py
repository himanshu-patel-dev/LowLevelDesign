from observer import ConcreteObserverA, ConcreteObserverB
from subject import ConcreteSubject


if __name__ == "__main__":
	subject = ConcreteSubject()
	
	observer_a = ConcreteObserverA()
	observer_b = ConcreteObserverB()

	subject.attach(observer_a)
	subject.attach(observer_b)

	subject.some_business_logic()
	subject.some_business_logic()

	subject.detach(observer_a)

	subject.some_business_logic()
