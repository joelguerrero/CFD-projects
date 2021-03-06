import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math


def laplace_iteration2_t(f,r,U_t,dr,dtheta,n,m):
	
	n=int(n)
	m=int(m)
	g=np.zeros((n+1,m));
	
	for j in range(1,int(m-1)): #iteration on the angle
		## Building the matrix A for a given j=2...m-1
		A = np.zeros((n+1,n+1));
		for i in range(1,n):
			A[i,i-1] = (-1/(2*dr)+r[i,j]/(dr**2));
			A[i,i] = -2*(r[i,j]/dr**2 + 1/(r[i,j]*dtheta**2));
			A[i,i+1] = 1/(2*dr)+r[i,j]/dr**2;


		#A[1,1] = -2*(r[1,j]/dr**2 + 1/(r[1,j]*dtheta**2));
		A[0,0] = 1;
		A[0,1] = -1;
		#A[1,2] = r[1,j]/dr**2 + (r[1,j]-dr)/dr**2; 
		A[n,n] = 1;
		
	
		## Building the forcing vector ff
		ff=np.zeros((n+1,1));
		for i in range(1,n):
			ff[i] = -(f[i,j-1]+f[i,j+1])/(r[i,j]*dtheta**2);
	
		ff[n] = r[n,j]*U_t[n,j]; # exact value on the exterior boundary
	
		## Solving for ru_t on the line for a fixed j
	
		g[:,j] = linalg.lstsq(A,ff)[0].reshape(n+1)
	
	
	
		## For j=0
		A1 = np.zeros((n+1,n+1));
		for i in range(1,n):
			A1[i,i-1] = (-1/(2*dr)+r[i,0]/(dr**2));
			A1[i,i] = -2*(r[i,0]/dr**2 + 1/(r[i,0]*dtheta**2));
			A1[i,i+1] = 1/(2*dr)+r[i,0]/dr**2;
	
	
		#A1[1,1] = -2*(r[1,1]/dr**2 + 1/(r[1,1]*dtheta**2));
		#A1[1,2] = r[1,1]/dr**2 + (r[1,1]-dr)/dr**2; 
		A1[0,0]=1;
		A1[0,1]=-1;
		A1[n,n] = 1;
		
		
		## Building the forcing vector ff1
		ff1=np.zeros((n+1,1));
		for i in range(1,n):
			ff1[i] = -(f[i,m-1]+f[i,1])/(r[i,0]*dtheta**2);
	
		ff1[n] = r[n,0]*U_t[n,0]; # exact value on the exterior 	boundary
	
		## Solving for ru_t on the line for j=0
		
		g[:,0] = linalg.lstsq(A1,ff1)[0].reshape(n+1)
		
		## For j=m
		
		## Building the matrix A for j=m-1
		Am = np.zeros((n+1,n+1));
		for i in range(1,n):
			Am[i,i-1] = (-1/(2*dr)+r[i,m-1]/(dr**2));
			Am[i,i] = -2*(r[i,m-1]/dr**2 + 1/(r[i,m-1]*dtheta**2));
			Am[i,i+1] = 1/(2*dr)+r[i,m-1]/dr**2;
	
	
		#An[1,1] = -2*(r(1,n]/dr**2 + 1/(r(1,n]*dtheta**2));
		#An(1,2] = r(1,n]/dr**2 + (r(1,n]-dr)/dr**2; 
		Am[0,0]=1;
		Am[0,1]=-1;
		Am[n,n] = 1;
		
		
		## Building the forcing vector ffm-1
		ffm=np.zeros((n+1,1));
		for i in range(1,n):
			ffm[i] = -(f[i,m-2]+f[i,0])/(r[i,m-1]*dtheta**2);
	
		ffm[n] = r[n,m-1]*U_t[n,m-1]; # exact value on the exterior boundary
	
		## Solving for ru_r on the line j=m-1
	
		g[:,m-1] = linalg.lstsq(Am,ffm)[0].reshape(n+1)
	
	return g
