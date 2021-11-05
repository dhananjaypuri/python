class vec2d:
    
    def __init__(self , i , j):

        self.i = i;
        self.j = j;
        print(f"{self.i}i + {self.j}j");
        
class vec3d(vec2d):

    def __init__(self,i , j,  k):

        self.k = k;

        super().__init__(i , j);
        print(f"{self.i}i + {self.j}j + {self.k}k");
   

v3 = vec3d(1,2,5);