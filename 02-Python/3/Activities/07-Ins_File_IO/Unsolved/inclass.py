# #!/usr/bin/env python
# # coding: utf-8

# # Import from the pathlib library, the main class Path
# from pathlib import Path

# # Check the current directory where the Python program is executing from
# print(f"Current Working Directory: {Path.cwd()}")

# # look for the input file input.txt in Resources folder
# filepath = Path("../Resources/input.txt")


# # In[ ]:


# filepath


# # In[ ]:


# #open the file in a read mode
# with open(filepath, 'r') as file:
#     text = file.read()
#     print(text)
#     line_num = 1 
#     for line in file:
#         print(f"line {line_num}: {line}")
#         line_num +=1


# # In[ ]:


# # filepath2 = Path("input_class.txt")


# # In[ ]:


# # #open the file in a read mode
# # with open(filepath2, 'r') as file:
# #     text = file.read()
# #     print(text)


# # In[ ]:


# # Send it to an output file
# output_path = Path("../Resources/output.txt")

# # open this output.txt file and write the content above
# with open(output_path, 'w') as file:
#     file.write("This is the output file executed.\n")
#     file.write(text)


# In[1]:


# Import the pathlib and csv library
from pathlib import Path
import csv


# In[2]:


# Set the file path
csvpath = Path("../Resources/accounting.csv")


# In[3]:


# Initialize line_num variable
line_num = 0
# Initialize variable to hold salaries
salaries = []


# In[4]:


with open(csvpath, 'r') as csvfile:
    
    print(type(csvfile))
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    line_num +=1
    
    print(f"{header}<--- HEADER")
    
    for row in csvreader:
#         print(row)
        salary = int(row[3])
        salaries.append(salary)
    


# In[5]:


salaries


# In[6]:


# Initialize metric variables
max_salary = 0
min_salary = 0
avg_salary = 0
total_salary = 0
count_salary = 0


# In[7]:


# Calculate the max, mean, and average of the list of salaries
for salary in salaries:

    # Sum the total and count variables
    total_salary += salary
    count_salary += 1
    # Logic to determine min and max salaries
    if min_salary == 0:
        min_salary = salary
    elif salary > max_salary:
        max_salary = salary
    elif salary < min_salary:
        min_salary = salary


# In[8]:


# Calculate the average salary, round to the nearest 2 decimal places
avg_salary = round(total_salary / count_salary, 2)

# Print the metrics
print(max_salary, min_salary, avg_salary)


# In[9]:


# Set the output header
header = ["Max_Salary", "Min_Salary", "Avg_Salary"]

# Create a list of metrics
metrics = [max_salary, min_salary, avg_salary]


# In[10]:


metrics


# In[11]:


output_path = Path('output.csv')


# In[12]:


with open(output_path, 'w')as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(header)
    csvwriter.writerow(metrics)


# In[ ]:




