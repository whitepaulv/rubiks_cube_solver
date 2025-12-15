from enum import IntEnum


# All of the possible pieces of the cube must be able to be converted
# to an integer for the algorithm. IntEnum allows these pieces
# to be converted quickly.

class Corner(IntEnum):
    URF = 0; UFL = 1; ULB = 2; UBR = 3
    DFR = 4; DLF = 5; DBL = 6; DRB = 7

class Edge(IntEnum):
    UR = 0; UF = 1; UL = 2; UB = 3
    DR = 4; DF = 5; DL = 6; DB = 7
    FR = 8; FL = 9; BL = 10; BR = 11

class Color(IntEnum):
    U = 0; R = 1; F = 2; D = 3; L = 4; B = 5

# ------------------------------------------------- 

class CubeRepresentation:
    def __init__(self, cp=None, co=None, ep=None, eo=None):
        self.cp = cp if cp else [0, 1, 2, 3, 4, 5, 6, 7]
        self.co = co if co else [0] * 8
        
        self.ep = ep if ep else [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.eo = eo if eo else [0] * 12

    def to_string(self):
        return (f"CP: {self.cp}\nCO: {self.co}\n"
                f"EP: {self.ep}\nEO: {self.eo}") 
        
    # This is a helper function to help any moves that are made.
    # In theory, only F or B moves change orientation of edges,
    # but this 'optimizaiton' would be more inefficient than ignoring
    # such.
    def move(self, move_code):
        new_cp = [0] * 8
        new_co = [0] * 8
        new_ep = [0] * 12
        new_eo = [0] * 12
        
        for i in range(8):
            new_cp[i] = self.cp[move_code.cp[i]]
            new_co[i] = (self.co[move_code.cp[i]] + move_code.co[i]) % 3

        for i in range(12):
            new_ep[i] = self.ep[move_code.ep[i]]
            new_eo[i] = (self.eo[move_code.ep[i]] + move_code.eo[i]) % 2
            
        return CubeRepresentation(new_cp, new_co, new_ep, new_eo)
    
    def U(self): return self.move(SimpleU)
    
    def R(self): return self.move(SimpleR)
    
    def F(self): return self.move(SimpleF)
    
    def D(self): return self.move(SimpleD)
    
    def L(self): return self.move(SimpleL)
    
    def B(self): return self.move(SimpleB)
 
# -------------------------------------------------    
    
# The following functions adjust permutations and orientations, then store that move in a new object
# Remember the intial ordering of corners:
#      URF = 0; UFL = 1; ULB = 2; UBR = 3
#      DFR = 4; DLF = 5; DBL = 6; DRB = 7

# And edges:
#       UR = 0; UF = 1; UL = 2; UB = 3 DR; = 4; DF = 5; 
#       DL = 6; DB = 7 FR = 8; FL = 9; BL = 10; BR = 11

SimpleU = CubeRepresentation(
    cp=[Corner.UBR, Corner.URF, Corner.UFL, Corner.ULB, Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB],
    co=[0, 0, 0, 0, 0, 0, 0, 0],
    ep=[Edge.UB, Edge.UR, Edge.UF, Edge.UL, Edge.DR, Edge.DF, Edge.DL, Edge.DB, Edge.FR, Edge.FL, Edge.BL, Edge.BR],
    eo=[0] * 12
)
     
# ------------------------------------------------- 
     
# The main cube object is now declared. It must be declared above the objects for moves
# because the moves create a temporary new version of this initial cube.

cube = CubeRepresentation()
print(cube.to_string())
cube = cube.U()
print()
print(cube.to_string())






