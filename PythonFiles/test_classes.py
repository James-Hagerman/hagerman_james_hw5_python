from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

ar1 = Arithmetic(20,40)
print(ar1.add())
print(ar1.divide())
print(ar1.remainder())
ar1.print_self()

ar2 = Arithmetic(100,100)
print(ar2.add())
print(ar2.divide())
print(ar2.remainder())
ar2.print_self()

ar3 = Arithmetic(50,100)
print(ar3.add())
print(ar3.divide())
print(ar3.remainder())
ar3.print_self()