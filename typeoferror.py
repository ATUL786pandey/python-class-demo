#WAP FOR TYPE OF ERROR IN PYTHON
#SOME EXAMPLE


def demo(a,b):
    l=[10,20]
    try:
        try:
            x=a/b
            print(x)
        except ZeroDivisionError as zde:
            print(zde)

        try:
           print(l[3])
        except IndexError as ie:
            print(ie)

    except Exception as e:
        print(e)

    print("continue code")

demo(10,0)
