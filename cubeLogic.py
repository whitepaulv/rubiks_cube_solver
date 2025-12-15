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

# -------------------------------------------------------------------------------------------------- 

class CubeRepresentation:
    def __init__(self, cp=None, co=None, ep=None, eo=None):
        self.cp = cp if cp else [0, 1, 2, 3, 4, 5, 6, 7]
        self.co = co if co else [0] * 8
        
        self.ep = ep if ep else [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.eo = eo if eo else [0] * 12

    def to_string(self):
        return (f"CP: {self.cp}\nCO: {self.co}\n"
                f"EP: {self.ep}\nEO: {self.eo}") 
        
    # The is_solved function was very useful for testing
    def print_state(self):
        if (
            self.co == [0] * 8 and
            self.cp == [0, 1, 2, 3, 4, 5, 6, 7] and
            self.eo == [0] * 12 and
            self.ep == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        ):
            print("The cube is SOLVED")
        else:
            print("The cube is SCRAMBLED")        
        
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
    
    def U_prime(self): return self.move(SimpleUPrime)
    
    def R_prime(self): return self.move(SimpleRPrime)
    
    def F_prime(self): return self.move(SimpleFPrime)
    
    def D_prime(self): return self.move(SimpleDPrime)
    
    def L_prime(self): return self.move(SimpleLPrime)
    
    def B_prime(self): return self.move(SimpleBPrime)
 
# --------------------------------------------------------------------------------------------------  
    
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
 
SimpleR = CubeRepresentation(
    cp=[Corner.DFR, Corner.UFL, Corner.ULB, Corner.URF, Corner.DRB, Corner.DLF, Corner.DBL, Corner.UBR],
    co=[2, 0, 0, 1, 1, 0, 0, 2],
    ep=[Edge.FR, Edge.UF, Edge.UL, Edge.UB, Edge.BR, Edge.DF, Edge.DL, Edge.DB, Edge.DR, Edge.FL, Edge.BL, Edge.UR],
    eo=[0] * 12
)
 
SimpleF = CubeRepresentation(
    cp=[Corner.UFL, Corner.DLF, Corner.ULB, Corner.UBR, Corner.URF, Corner.DFR, Corner.DBL, Corner.DRB],
    co=[1, 2, 0, 0, 2, 1, 0, 0],
    ep=[Edge.UR, Edge.FL, Edge.UL, Edge.UB, Edge.DR, Edge.FR, Edge.DL, Edge.DB, Edge.UF, Edge.DF, Edge.BL, Edge.BR],
    eo=[0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0] 
)

SimpleD = CubeRepresentation(
    cp=[Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR, Corner.DLF, Corner.DBL, Corner.DRB, Corner.DFR],
    co=[0] * 8,
    ep=[Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DF, Edge.DL, Edge.DB, Edge.DR, Edge.FR, Edge.FL, Edge.BL, Edge.BR],
    eo=[0] * 12
)

SimpleL = CubeRepresentation(
    cp=[Corner.URF, Corner.ULB, Corner.DBL, Corner.UBR, Corner.DFR, Corner.UFL, Corner.DLF, Corner.DRB],
    co=[0, 1, 2, 0, 0, 2, 1, 0],
    ep=[Edge.UR, Edge.UF, Edge.BL, Edge.UB, Edge.DR, Edge.DF, Edge.FL, Edge.DB, Edge.FR, Edge.UL, Edge.DL, Edge.BR],
    eo=[0] * 12
)

SimpleB = CubeRepresentation(
    cp=[Corner.URF, Corner.UFL, Corner.UBR, Corner.DRB, Corner.DFR, Corner.DLF, Corner.ULB, Corner.DBL],
    co=[0, 0, 1, 2, 0, 0, 2, 1],
    ep=[Edge.UR, Edge.UF, Edge.UL, Edge.BR, Edge.DR, Edge.DF, Edge.DL, Edge.BL, Edge.FR, Edge.FL, Edge.UB, Edge.DB],
    eo=[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1] 
)

SimpleUPrime = CubeRepresentation(
    cp=[Corner.UFL, Corner.ULB, Corner.UBR, Corner.URF, Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB],
    co=[0, 0, 0, 0, 0, 0, 0, 0],
    ep=[Edge.UF, Edge.UL, Edge.UB, Edge.UR, Edge.DR, Edge.DF, Edge.DL, Edge.DB, Edge.FR, Edge.FL, Edge.BL, Edge.BR],
    eo=[0] * 12
)

SimpleRPrime = CubeRepresentation(
    cp=[Corner.UBR, Corner.UFL, Corner.ULB, Corner.DRB, Corner.URF, Corner.DLF, Corner.DBL, Corner.DFR],
    co=[2, 0, 0, 1, 1, 0, 0, 2],
    ep=[Edge.BR, Edge.UF, Edge.UL, Edge.UB, Edge.FR, Edge.DF, Edge.DL, Edge.DB, Edge.UR, Edge.FL, Edge.BL, Edge.DR],
    eo=[0] * 12
)

SimpleFPrime = CubeRepresentation(
    cp=[Corner.DFR, Corner.URF, Corner.ULB, Corner.UBR, Corner.DLF, Corner.UFL, Corner.DBL, Corner.DRB],
    co=[1, 2, 0, 0, 2, 1, 0, 0],
    ep=[Edge.UR, Edge.FR, Edge.UL, Edge.UB, Edge.DR, Edge.FL, Edge.DL, Edge.DB, Edge.DF, Edge.UF, Edge.BL, Edge.BR],
    eo=[0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0] 
)

SimpleDPrime = CubeRepresentation(
    cp=[Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR, Corner.DRB, Corner.DFR, Corner.DLF, Corner.DBL],
    co=[0] * 8,
    ep=[Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DB, Edge.DR, Edge.DF, Edge.DL, Edge.FR, Edge.FL, Edge.BL, Edge.BR],
    eo=[0] * 12
)

SimpleLPrime = CubeRepresentation(
    cp=[Corner.URF, Corner.DLF, Corner.UFL, Corner.UBR, Corner.DFR, Corner.DBL, Corner.ULB, Corner.DRB],
    co=[0, 1, 2, 0, 0, 2, 1, 0],
    ep=[Edge.UR, Edge.UF, Edge.FL, Edge.UB, Edge.DR, Edge.DF, Edge.BL, Edge.DB, Edge.FR, Edge.DL, Edge.UL, Edge.BR],
    eo=[0] * 12
)

SimpleBPrime = CubeRepresentation(
    cp=[Corner.URF, Corner.UFL, Corner.DBL, Corner.ULB, Corner.DFR, Corner.DLF, Corner.DRB, Corner.UBR],
    co=[0, 0, 1, 2, 0, 0, 2, 1],
    ep=[Edge.UR, Edge.UF, Edge.UL, Edge.BL, Edge.DR, Edge.DF, Edge.DL, Edge.BR, Edge.FR, Edge.FL, Edge.DB, Edge.UB],
    eo=[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1] 
)
     
# --------------------------------------------------------------------------------------------------   
     
# The main cube object is now declared. It must be declared above the objects for moves
# because the moves create a temporary new version of this initial cube.

cube = CubeRepresentation()
print(cube.to_string())

print()

cube = cube.R()
cube = cube.U()

cube = cube.R_prime()
cube = cube.U_prime()

cube = cube.R_prime()
cube = cube.F()

cube = cube.R()
cube = cube.R()

cube = cube.U_prime()
cube = cube.R_prime()
cube = cube.U_prime()

cube = cube.R()
cube = cube.U()
cube = cube.R_prime()
cube = cube.F_prime()

print()
print(cube.to_string())







