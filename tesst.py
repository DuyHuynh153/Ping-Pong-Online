class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Accessing class variable:", )

# Using the class method
MyClass.class_method()

# Creating an instance of MyClass
obj = MyClass("Instance variable")

# Calling the class method through the instance
obj.class_method()
