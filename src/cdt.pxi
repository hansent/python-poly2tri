cdef class CDT:

    cdef c_CDT *me
    cdef point_vec polyline
    
    def __cinit__(self, list polyline=None):
        self.polyline = pointvec_factory(0)
        if polyline:       
            for point in polyline:
                self.polyline.push_back(new_Point(point.x, point.y))
        self.me = new_CDT(self.polyline)
        
        
    cpdef triangulate(self):
        cdef Point a,b,c
        cdef list triangles = []
        self.me.Triangulate()
        cdef triangle_vec tri_list = self.me.GetTriangles()
        cdef int num_triangles = tri_list.size()
        for i in range(num_triangles):
            a = Point(tri_list.get(i).GetPoint(0).x, tri_list.get(i).GetPoint(0).y)
            b = Point(tri_list.get(i).GetPoint(1).x, tri_list.get(i).GetPoint(1).y)
            c = Point(tri_list.get(i).GetPoint(2).x, tri_list.get(i).GetPoint(2).y)
            triangles.append(Triangle(a, b, c))
        return triangles
    
    cpdef add_hole(self, polyline):
        cdef point_vec hole = pointvec_factory(0)
        for point in polyline:
            hole.push_back(new_Point(point.x, point.y))
        self.me.AddHole(hole)
        
    cpdef add_point(self, point):
        cdef c_Point* p = new_Point(point.x, point.y)
        self.me.AddPoint(p)

    def __dealloc__(self):
        del_CDT(self.me)
