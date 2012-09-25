cdef class Point:

    cdef float x, y
    
    def __init__(self, float x, float y):
        self.x = x
        self.y = y
        
    property x:
        def __get__(self): return self.x
        def __set__(self, x): self.x = x
        
    property y:
        def __get__(self): return self.y
        def __set__(self, y): self.y = y
        
    def __str__(self):
        return "Point({self.x}, {self.y})".format(self=self)
        
cdef class Triangle:
    
    cdef Point a, b, c
    
    def __init__(self, Point a, Point b, Point c):
        self.a = a
        self.b = b
        self.c = c
        
    property a:
        def __get__(self): return self.a
    
    property b:
        def __get__(self): return self.b
    
    property c:
        def __get__(self): return self.c
        
    def __str__(self):
        return "Triangle({self.a}, {self.b}, {self.c})".format(self=self)
        
