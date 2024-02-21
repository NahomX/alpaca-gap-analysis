def name_arg(,args,**kwargs):
    for i in args:
        print(i)
    for i in kwargs.values():
        print(i)
name_arg(1,2,3,name="jhon")
