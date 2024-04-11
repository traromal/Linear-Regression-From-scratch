# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv('mark.csv')

# plt.scatter(data.time_study, data.Marks)

# plt.show()


# def loss(m, b, points):
#     total_error = 0
#     for i in range(len(points)):
#         x = points.iloc[i].time_study
#         y = points.iloc[i].time_Marks
#         total_error += (y-(m*x + b)) **2
#     total_error/float(len(points))
    
    
# def gradient_descent(m_now, b_now, points, L):
#     m_gradient = 0
#     b_gradient = 0
    
#     n = len(points)
    
#     for i in range(n):
#         x = points.iloc[i].time_study
#         y = points.iloc[i].Marks
        
#         m_gradient += -(2/n) * x * (y-(m_now * x + b_now))
#         b_gradient += -(2/n) *  (y-(m_now * x + b_now))
        
    
    
#     m = m_now - m_gradient * L
#     b = b_now - b_gradient * L
#     return m, b


# m = 0
# b = 0
# L = 0.0001
# epoches = 500

# for i in range(epoches):
#     if i % 50 == 0:
#         print(f"epoch:{i}")
#     m,b = gradient_descent(m,b, data, L)

# print(m,b)


# plt.scatter(data.time_study, data.Mark, color="purple" )
# plt.plot(list(range(20,100)), [m * x+b for x in range(20, 80)], color= "red")
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('mark.csv')

plt.scatter(data.time_study, data.Marks)
plt.show()

def loss(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].time_study
        y = points.iloc[i].Marks
        total_error += (y - (m * x + b)) ** 2
    total_error /= float(len(points))
    return total_error
    
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    
    n = len(points)
    
    for i in range(n):
        x = points.iloc[i].time_study
        y = points.iloc[i].Marks
        
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
        
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.0001
epochs = 100

for i in range(epochs):
    if i % 50 == 0:
        print(f"epoch:{i}")
    m, b = gradient_descent(m, b, data, L)

print("m:", m, "b:", b)

plt.scatter(data.time_study, data.Marks, color="purple" )
plt.plot(data.time_study, [m * x + b for x in data.time_study], color="red")
plt.show()
