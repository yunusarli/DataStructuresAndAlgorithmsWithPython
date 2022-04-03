"""
Find files disk usages

"""
#os module for file operations
import os

def disk_usage(path):
    total = os.path.getsize(path)

    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total

result = disk_usage("C://python310")

print(result)