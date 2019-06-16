def testfile():
    
    with open('../a', 'r') as f1:
        list1 = f1.readlines()
        print(list1)
        
if __name__ == "__main__":
    testfile()